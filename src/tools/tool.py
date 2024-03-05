import hashlib
import os
import shutil
import subprocess
import multiprocessing
from time import sleep
import tools.hangs as hangs
import re
from colormath.color_objects import sRGBColor
from colormath.color_conversions import convert_color
import psutil

tools_path=os.path.dirname(os.path.abspath(__file__))
current_dir = os.getcwd()

def proc(cmd:list):
    result = subprocess.run(cmd, capture_output=True, text=True).stdout
    return result

def get_list():
    command = ['tmux', 'ls']
    result = proc(command)
    # 将结果写入文件
    test_list = result.split("\n")[:-1]
    # print(test_list)
    for i in range(0, len(test_list)):
        test_list[i] = test_list[i].split(":", 1)[0]
    return test_list

def get_name(directory='out'):
    os.makedirs(directory, exist_ok=True)
    directory_names = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            directory_names.append(item)
    return directory_names

def get_md(directory):
    directory_names = []
    for item in os.listdir(directory):
        if item.endswith(".md"):
            directory_names.append(item)
    return directory_names

def get_pid(cmd):
    result1 = subprocess.Popen(['ps', '-aux'], stdout=subprocess.PIPE)
    result = subprocess.run(['grep', cmd], stdin=result1.stdout,
                            capture_output=True, text=True).stdout
    test_list = result.split("\n")[:-1]
    # print(cmd)
    for cmd_pid in test_list:
        if cmd_pid[67:] == cmd:
            return int(cmd_pid.split()[1])
    return 0

def get_pid1(name, cmd):
    stats = 'out/'+name+'/default/fuzzer_stats'
    try:
        with open(stats, "r") as fd:
            lines = fd.readlines()
            afl_pid = int(lines[3].split(":")[1])
            #print(afl_pid)
        if psutil.pid_exists(int(afl_pid)):
            return afl_pid
        else:
            return 0
    except:
        return get_pid(cmd)

def get_afl_info(cmd):
    result = proc(cmd)
    result = convert_python_colors_to_html(result)
    return result

def convert_python_colors_to_html(text):
    """
    将带有Python颜色标记的文本转换为带有HTML颜色标记的文本
    :param text: 带有Python颜色标记的文本，如'\033[91mHello\033[0m'
    :return: 带有HTML颜色标记的文本，如'<span style="color: #ff0000;">Hello</span>'
    """
    color_regex = re.compile(r'\033\[\d+;+\d+m')  # 匹配Python颜色标记的正则表达式

    html_text = ''
    last_end = 0

    for match in color_regex.finditer(text):
        start = match.start()
        end = match.end()

        color_tag = text[start:end]
        color_code = re.search(r'\[\d+;(\d+)m', color_tag).group(1)
        print(color_code)
        html_text += text[last_end:start]  # 添加颜色标记前的文本

        if color_code.isdigit():
            rgb_color = sRGBColor(int(color_code), int(color_code), int(color_code))  # 灰度颜色
        else:
            rgb_color = sRGBColor(*map(int, color_code.split(';')))  # RGB颜色

        html_color = convert_color(rgb_color, sRGBColor).get_rgb_hex()
        html_text += '<span style="color: {};">'.format(html_color)  # 添加HTML颜色标记的开标签

        last_end = end

    html_text += text[last_end:]  # 添加剩余的文本
    html_text += '</span>'  # 添加HTML颜色标记的闭标签

    return html_text

def cmd(command, size="81"):
    subprocess.call("gnome-terminal --geometry="+size+"x26 -- bash -c \""+command+"\"",
                    stderr=subprocess.DEVNULL, shell=True)

def run(name, program, testcase, coverage_enabled, src, isfirst=True):
    if not src:
        src = '.'
    afl_cov = ''
    #cov_cmd=[]
    size = '81'

    if not (program and testcase):
        return ("信息不全")
    test_list = get_list()
    # if name in test_list:
    #     return ("测试名称重复")
    target=program.split()[0]
    target1=os.path.abspath(target)
    if not os.path.isfile(target1):
        return ("执行命令中测试目标不是文件或者文件不存在")
    if "@@" not in program:
        return ("执行命令中请输入@@")
    if isfirst:
        if not os.path.isdir(testcase):
            return ("确保测试用例是个文件夹并且存在")
    if len(program.split())<2:
        return ("执行命令参数过少")
    program=program.replace(target, target1)
    os.makedirs("out",exist_ok=True)
    # if os.path.exists('out/'+name):
    #     shutil.rmtree('out/'+name)
    is_cov,is_chazhuang=file_analyzed(target)
    
    if coverage_enabled :
        if not is_cov:
            return("编译时请加上'-fprofile-arcs -ftest-coverage'")
        size = '162'
        cov_cmd = [tools_path+"/cov/afl-cov", "-d", 'out/'+name, "--live", "--sleep", "2",
                   "--coverage-cmd=\'"+program.replace("@@", "AFL_FILE")+"\'",
                   "--code-dir="+src]
        afl_cov = " \\\""+(" ").join(cov_cmd)+"\\\" \; split-window -h"
        print ("cov_cmd: "+(" ").join(cov_cmd))
    afl_cmd_list = [tools_path+'/fuzz/afl-fuzz','-i',
                    testcase, '-o', 'out/'+name, '--', program]
    if not is_chazhuang:
        afl_cmd_list = [tools_path+'/fuzz/afl-fuzz','-Q','-i',
                        testcase, '-o', 'out/'+name, '--', program]
        
    afl_cmd = (" ").join(afl_cmd_list)
    command = "tmux new -s "+name+afl_cov+" \\\""+afl_cmd+"\\\""
    
    print (f"afl_cmd: {afl_cmd}\n")
    # print ("gnome-terminal --geometry="+size+"x26 -- bash -c \""+command+"\'\'\'")
    # error_info=get_afl_info(afl_cmd_list)
    cmd(command, size)
    sleep(1)
    if isfirst:
        afl_pid = get_pid1(name, afl_cmd)
        # print(afl_pid)
        if not afl_pid:
            error_info = get_afl_info(afl_cmd_list)
            if os.path.exists('out/'+name):
                try:
                    shutil.rmtree('out/'+name)
                except Exception as e:
                    shutil.rmtree('out/'+name)
                    return (e)
            return (error_info)

    return ""

def file_analyzed(program):
    is_cov=False
    is_chazhuang=False
    command=['nm',program]
    nm=proc(command)
    if "afl" in nm:
        is_chazhuang=True
    if "gcov" in nm:
        is_cov=True
    return is_cov,is_chazhuang

def crash_analyzed(name,num,default="crashes"):
    num=int(num)
    stats_path = current_dir+"/out/"+name+"/default/fuzzer_stats"
    crashes_path = current_dir+"/out/"+name+"/default/"+default
    crash_analyzed_path = current_dir+"/out/"+name+"/"+default
    new_crashes_path = current_dir+"/out/"+name+"/"+default+"/"+default
    is_crash=False
    if os.path.exists(stats_path) and len(os.listdir(crashes_path))!=0 :
        os.makedirs(crash_analyzed_path,exist_ok=True)
        i=1
        while True:
            if os.path.exists(new_crashes_path):
                new_crashes_path=crash_analyzed_path+"/"+default+"_"+str(i)
                i+=1
            else:
                break
        shutil.copytree(crashes_path, new_crashes_path)
        with open(stats_path, "r") as fd:
            lines = fd.readlines()
        cmd = lines[-1].split(" -- ")[1]
        if default=="crashes":
            command = get_files_with_id_prefix(cmd, new_crashes_path, "crash_")
            is_crash=True
        else :
            command = get_files_with_id_prefix(cmd, new_crashes_path, "hang_")
        is_ok,e=run_process(command,crash_analyzed_path,is_crash,num)
        if is_ok:
            return "成功",(f"测试{name} {default}分析结束!")
        else:
            return "错误",e
    else:
        return "提示",(f"测试{name}不存在或者没有{default}")

def get_files_with_id_prefix(cmd:str, folder_path, id_prefix):
    command=[]
    for filename in os.listdir(folder_path):
    # 检查文件名是否以'id'开头
        
        if filename.startswith("id"):
            #print(filename)
            # 构建新的文件名
            new_filename = filename.split(",",1)[0].replace("id:",id_prefix)  # 在原文件名前加上 'new_'

            # 构建文件的完整路径
            file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            # 重命名文件
            if os.path.exists(new_file_path):
                continue
            os.rename(file_path, new_file_path)
            command.append(cmd.replace("@@",new_file_path))
    return command

def run_process(cmd: list,crash_analyzed_path: str,is_crash: bool = True , num: int=4):
    try:
        pool = multiprocessing.Pool(processes=num)
        if is_crash:
            pool.starmap(crash_run_analyzed, [(item, crash_analyzed_path) for item in cmd])
        else:
            pool.starmap(hangs_run_analyzed, [(item, crash_analyzed_path) for item in cmd])
        pool.close()
        pool.join()
        print("分析完成!")
        return True,''
    except Exception as e:
        return False,e

def crash_run_analyzed(cmd: str,crash_analyzed_path:str):
    _cmd = cmd.split()
    print(f"[*]开始分析{cmd}")
    command = ["gdb",
               "-ex", "run",
               "-ex","echo ----bt----\\n",
               "-ex", "btpp -100",
               "-ex","echo ----exploitable----\\n",
               "-ex", "exploitable",
               "-ex", "infopp",
               "-ex","quit",
               "--args"]+_cmd
    #print(command)
    try:
        out = subprocess.run(command,capture_output=True, text=True).stdout
        bt=out.split("----bt----\n",1)[1].split("\n----exploitable----",1)[0]
        exploitable=out.split("----exploitable----\n",1)[1].split("\n----asm----",1)[0]
        asm=out.split("----asm----\n",1)[1].split("\n----code----",1)[0]
        code=out.split("----code----\n",1)[1].split("\n----end----",1)[0]
        log="复现命令:\n```\n"
        log+=cmd+"\n```\n\n"
        log+="分析结果:\n```\n"
        log+=exploitable+"\n```\n\n"
        log+="栈回溯:\n```\n"
        log+=bt+"\n```\n\n"
        is_loop=False
        if len(bt.split("\n"))>99 and "offset" in bt.split("\n")[1]:
            btes=bt.split("\n")[1:][:-1]
            for i in range (len(btes)):
                btes[i]=btes[i].split(" ",1)[1]
            #print(btes)
            loop_data=find_loop(btes)
            is_loop=loop_data["is_loop"]
            block=loop_data["loop_block"]
            if is_loop:
                log+="递归块:\n```\n"
                log+=("\n").join(block)+"\n```\n\n"
                hash=str(hashlib.md5(str(block).encode()).hexdigest())[:8]
                name=hash+"."+"无限递归"
        if not is_loop:
            if "#" in bt and "=>" in asm :
                hash=str(hashlib.md5(str(asm).encode()).hexdigest())[:8]
                Description=exploitable.split("Description: ")[1].split("\n")[0]
                name=hash+"."+Description
                #print(name)
            else:
                name="未知"
            log+="崩溃点汇编:\n```\n"
            log+=asm+"\n```\n\n"
            log+="崩溃点源代码:\n```\n"
            log+=code+"\n```\n\n"
        name=name+".md"
        if not os.path.exists(crash_analyzed_path+"/"+name):
            with open(crash_analyzed_path+"/"+name, "w") as fd:
                fd.write(log)
            print("分析成功"+cmd+"[+]新缺陷: "+name+"\n保存目录: "+crash_analyzed_path+"\n")
        else:
            print("分析成功"+cmd+"[.]重复缺陷: "+name+"\n")
        
    except Exception as e:
        print(f"[-]分析失败\n{cmd}错误原因: {e}\n")
        pass

def find_loop(data):
        key1 = 0
        key2 = 0
        count=1
        str_find = ['']
        str_find[0] = data[0]
        for i in range(1, len(data)):
            if (len(str_find) * (count + 1)) > len(data):
                break
            if str_find == data[count * len(str_find):len(str_find) * (count + 1)]:
                key1 = i + 1
                if key1 % len(str_find) == 0:
                    loop_block = str_find
                    count += 1
            else:
                key2 = i + 1
                str_find = data[0:len(str_find) + 1]
        if count > 4:
            loop = True
        else:
            loop = False
        _log = {
            "loop_block": loop_block,
            "count":count,
            "is_loop": loop
        }
        return _log
    # print(out)

def find_loop1(date):
    pass

def hangs_run_analyzed(cmd: str,hangs_analyzed_path:str):
    print(f"[*]开始分析{cmd}")
    _cmd = cmd.split()
    a=hangs.hangs_analysis('ABC')
    hangs_d=hangs.Searchhangs(a, cmd)
    if hangs_d["hangs"]:
        bt=("\n").join(hangs_d["bt"])
        loop_point=hangs_d["key"]
        addr="0"
        if "0x" in hangs_d["addr"]:
            addr=hangs_d["addr"]
            # print(addr)
        command = ["gdb",
                   "-ex", "start",
                   "-ex", "infopp "+addr,
                   "-ex","quit",
                   "--args"]+_cmd
        try:
            out = subprocess.run(command,capture_output=True, text=True).stdout
            asm=out.split("----asm----\n",1)[1].split("\n----code----",1)[0]
            code=out.split("----code----\n",1)[1].split("\n----end----",1)[0]
            hash=str(hashlib.md5(str(asm).encode()).hexdigest())[:8]
            name=hash+'.无限循环.md'
            log="复现命令:\n```\n"
            log+=cmd+"\n```\n\n"
            log+="栈回溯:\n```\n"
            log+=bt+"\n```\n\n"
            log+="循环点:\n```\n"
            log+=loop_point+"\n```\n\n"
            log+="循环点汇编:\n```\n"
            log+=asm+"\n```\n\n"
            log+="循环点源代码:\n```\n"
            log+=code+"\n```\n\n"
            if not os.path.exists(hangs_analyzed_path+"/"+name):
                with open(hangs_analyzed_path+"/"+name, "w") as fd:
                    fd.write(log)
                print("分析成功"+cmd+"[+]新循环: "+name+"\n保存目录: "+hangs_analyzed_path+"\n")
            else:
                print("分析成功"+cmd+"[.]重复循环: "+name+"\n")
        except Exception as e:
            print(f"[-]分析失败\n{cmd}错误原因: {e}\n")
            pass
    else:
        print(f"{cmd}不是无限循环\n")

def crash_show(name,crashes="crashes"):
    crash_analyzed_path="out/"+name+"/"+crashes
    proc(['xdg-open',crash_analyzed_path])
    