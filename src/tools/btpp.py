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
        asm_end=gdb.execute("x/4i "+address,to_string=True).splitlines()
        asm_head=gdb.execute("x/-5i "+address,to_string=True).splitlines()
        #print (asm_end)
        if "=>" not in asm_end[0]:
            if not is_args:
                addr=int(asm_head[-1].split()[0],16)
                asm_head[-1]="=> "+asm_head[-1][3:]
            else:
                # asm_end[0]="=> "+asm_end[0][3:]
                addr=int(asm_head[-1].split()[0],16)
                asm_head[-1]="=> "+asm_head[-1][3:]
        else:
            addr=int(asm_end[0].split()[1],16)
        asm=asm_head+asm_end
        for j in range (len(asm)):
            asm[j]=asm[j].lower()

        pc_line=str(gdb.find_pc_line(addr))
        pc_line=pc_line.replace('symbol and line for ','').replace(', line ',':')
        #print(pc_line)
        code=gdb.execute("list "+pc_line,to_string=True)
        codes=code.splitlines()
        line=pc_line.split(":")[1]
        for j in range(len(codes)):
            if codes[j].startswith(line):
                codes[j]=codes[j]+'   <-<'
                break
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
