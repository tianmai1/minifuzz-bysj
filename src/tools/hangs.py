from subprocess import Popen, PIPE, DEVNULL, TimeoutExpired
import os
import sys
import psutil
import time
import signal

class hangs_analysis:
 
    def __init__(self, name):
        self.name = name
        self.cmd = None
        self.bt = []
        self.gdb_process = None
        self.gdb_pid=None
        self.timeout = 1
        self.target_pid=None

    def gdb_run(self):
        if self.cmd is None:
            print("缺少可执行文件及其执行指令")
            exit()
        else:
            self.cmd = self.cmd.split()
        gdb_command = ['gdb', '-ex', 'start','-ex','info proc','-ex','c','-ex',"echo 'bt-begin\\n'\n",'-ex','btpp 20\n','-ex',"echo 'bt-end\\n'\n",'--args']+self.cmd
        self.gdb_process = Popen(gdb_command, stdin=PIPE,stdout=PIPE,stderr=DEVNULL)
        self.gdb_pid=self.gdb_process.pid
        #获取目标的pid
        while True:
            gdb_output = self.gdb_process.stdout.readline()
            if 'process'in str(gdb_output):
                break

        word_list = gdb_output.split()
        self.target_pid=int(word_list[1])
        time.sleep(self.timeout)

        #监控目标进程状态
        try:
            process = psutil.Process(self.target_pid)
        #如果没有目标进程，则不是超时
        except psutil.NoSuchProcess as e:
            return False,"The program is normal"
        status = process.status()
        #如果状态为运行中则暂停目标程序
        if status=='running':
            os.kill(self.target_pid, signal.SIGINT)
        #其他状态都不是无限循环
        elif status=='tracing-stop':
            return False,"not hangs,maybe crash"
        else :
            return False,"not xunhuan"
        #程序暂停后会继续执行bt并且将调用堆栈记录下来，方便寻找循环点
        while True:
            a = self.gdb_process.stdout.readline()
            if 'bt-end'in str(a):
                break
            if '#' in str(a) and len(str(a).split())>1 and "0x" in str(a):
                self.bt.append(str(a).split("#")[1])

    def find_addr(self):
        #print(self.bt)
        if not len(self.bt):
            return [],0,False,"no stack"
        for i in range(0,len(self.bt)):
            
            if len(self.bt[i].split())<2:
                continue
            addr=self.bt[i].split()[1]
            if '0x' in addr:
                addr='*'+addr
            gdb_command = 'tb '+str(addr)+'\n'
            gdb_command+='c\n'
            self.gdb_process.stdin.write(gdb_command.encode())
            self.gdb_process.stdin.flush()
            time.sleep(1)
            try:
                process = psutil.Process(self.target_pid)
            except psutil.NoSuchProcess as e:
                return [],0,False,e
            status = process.status()
            if status=='running':
                return self.bt,i,True,""
        return [],0,False,"no stack"        
    def end(self):
        try:
            process = psutil.Process(self.gdb_pid)
        except psutil.NoSuchProcess:
            #print("hhhhhhhh")
            return
        os.kill(self.gdb_pid, signal.SIGINT)



def Searchhangs(name, cmd):
    name.cmd = cmd
    name.gdb_run()
    bts,i,_,_= name.find_addr()
    name.end()
    hangs=False
    addr="0"
    key=""
    if len(bts):
        hangs=True
    if i>0 and i<len(bts):
        if "0x" in bts[i-1]:
            addr=bts[i-1].split()[1]
        key='#'+bts[i-1]
        
    else:
        hangs=False
    a={
        "bt":bts,
        "addr":addr,
        "key":key,
        "hangs":hangs
    }
    #print(a)
    return a


def main():
    b = hangs_analysis('ABC')
    cmd_args = ' '.join(sys.argv[1:])
    Searchhangs(b, cmd_args)


if __name__ == "__main__":
    main()
