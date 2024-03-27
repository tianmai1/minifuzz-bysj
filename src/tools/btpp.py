import gdb


class GdbWrapperError(RuntimeError):
    '''
    Base class for errors in this module
    '''
    pass


class BtppCommand(gdb.Command):
    def __init__(self):
        super(BtppCommand, self).__init__("btpp", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):

        # 解析参数，如果没有指定帧数，则默认为0
        try:
            if arg:
                bt_info = gdb.execute(
                    "bt -frame-info location-and-address "+str(arg), to_string=True)
            else:
                bt_info = gdb.execute(
                    "bt -frame-info location-and-address ", to_string=True)
            btes = bt_info.splitlines()
            vmmap_info = str(gdb.execute("info proc mapping", to_string=True))
        except Exception as e:
            print(e)
            return
        header_pos = vmmap_info.find("Start Addr")
        if header_pos == -1:
            raise GdbWrapperError("Unable to parse \"info proc map\" string")

        vmmapes = vmmap_info[header_pos:].splitlines()
        map = {}
        key = ""
        indx=0
        for file in vmmapes[0].split():
            indx+=1
            if "objfile"==file:
                break
        if "objfile" in vmmapes[0]:
            indx=indx-2
        else:
            indx=20
        #print(indx)
        for vmmap in vmmapes[1:]:
            list_vmmap = vmmap.split()
            if len(list_vmmap) < indx:
                continue
            start_addr = int(list_vmmap[0], 16)
            end_addr = int(list_vmmap[1], 16)
            objfile = list_vmmap[indx-1]
            if "/" not in objfile:
                continue
            if objfile in map:
                base = map[objfile]["start_addr"]
                if objfile+key in map:
                    if start_addr == map[objfile+key]["end_addr"]:
                        map[objfile+key]["end_addr"] = end_addr
                    else:
                        while True:
                            key += "1"
                            if objfile+key not in map:
                                break
                        map[objfile+key] = {"base": base,
                                            "start_addr": start_addr,
                                            "end_addr": end_addr,
                                            "objfile":objfile}
                else:
                    map[objfile+key] = {"base": base,
                                        "start_addr": start_addr,
                                        "end_addr": end_addr,
                                        "objfile":objfile}
            else:
                key = ""
                map[objfile+key] = {"base": start_addr,
                                    "start_addr": start_addr,
                                    "end_addr": end_addr,
                                    "objfile":objfile}

        if not map:
            for bt in btes:
                if "#" not in bt:
                    continue
                print(bt)
            return
        for i in range(0, len(btes)):
            # if frame:
            if "#" not in btes[i]:
                continue
            addr = int(btes[i].split()[1], 16)
            for name, value in map.items():
                if addr > map[name]["start_addr"] and addr < map[name]["end_addr"]:
                    btes[i] = btes[i]+" objfile: "+map[name]["objfile"]+" offset: " + \
                        str(hex(addr-map[name]["base"]))
            # frame=frame.older()
            print(btes[i])
            # level=btes[i].split()[0].replace("#","")
            # if not level.isdigit():
            #      continue
            # bt_address=btes[i].split()[1]
            # if "0x" not in bt_address:
            #     function=bt_address
            #     info_frame=gdb.execute("info frame "+str(level), to_string=True)
            #     bt_address=info_frame.splitlines()[1].split()[2]
            #     btes[i]=btes[i].replace(function,bt_address+" in "+function)

            # print (btes[i])

class InfoppCommand(gdb.Command):
    def __init__(self):
        super(InfoppCommand, self).__init__("infopp", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        if arg:
            try:    
                arg=int(gdb.execute("p "+arg,to_string=True).split("= ")[1])
                infopp_fx(arg,True)
            except Exception as e:
                print(e)
            return
        try:
            frame=gdb.selected_frame()
        except:
            infopp_fx(0)
            return
        while frame:
            address=frame.pc()
            addr=str(hex(address))
            if frame.name()==None or addr[0:4]=='0x7f' or frame.type()==2:
                frame=frame.older()
                continue
            infopp_fx(address)
            break
        

def infopp_fx(addr:int,is_args:bool=False):
    address=str(hex(addr))
    #print(address)
    asm=[]
    codes=[]
    pc_line=''
    try:
        gdb.execute("set disassembly-flavor intel",to_string=True)        
        _asm=gdb.execute("disassemble "+hex(addr),to_string=True).splitlines()     
        if len(_asm)>2:
            for i,value in enumerate(_asm[1:-1]):
                i+=1
                if not is_args:
                    if '=>' in value :
                        asm=_asm[max(i-5,1):min(len(_asm)-1,i+6)]
                        break
                    if addr==int(value.split()[0],16):
                        addr=int(_asm[max(1,i-1)].split()[0],16)
                        _asm[max(1,i-1)]='=> '+_asm[max(1,i-1)][3:]
                        asm=_asm[max(i-6,1):min(len(_asm)-1,i+5)]
                        break
                else :
                    if '=>' in value:
                        value='   '+value[3:]
                        _asm[i]='   '+_asm[i][3:]
                    if addr==int(value.split()[0],16):
                        _asm[i]='=> '+_asm[i][3:]
                        for j in range (len(_asm[i+1:min(len(_asm)-1,i+6)])):
                            _asm[j+i+1]='   '+_asm[j+i+1][3:]
                        asm=_asm[max(i-5,1):min(len(_asm)-1,i+6)]
                        break

        pc_line=str(gdb.find_pc_line(addr))
        # print(pc_lines)
        if '<unknown>' not in pc_line:
            pc_lines=pc_line.replace('symbol and line for ','').replace(', line ',':')
            code=gdb.execute("list "+pc_lines,to_string=True)
            codes=code.splitlines()
            if len(codes)>2:
                line=pc_lines.split(":")[1]
                for j in range(len(codes)):
                    if codes[j].startswith(line):
                        codes[j]=codes[j]+'   <-<'
        else:
            pc_line=''
    except Exception as e:
        print(e)
    #return asm,codes
    infopp="----asm----\n"
    infopp+=("\n").join(asm)
    infopp+="\n----code----\n"
    infopp+=pc_line+"\n\n"
    infopp+=("\n").join(codes)
    infopp+="\n----end----\n"
    print(infopp)


BtppCommand()
InfoppCommand()
