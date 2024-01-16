复线命令:
```json
/home/tianmai/workspace/tmp/test1 out/test3_gdb13/crashes/crashes/crash_000006

```
分析结果:
```json

Description: 程序退出
Hash: 1afad71143b930b8bbafbc4cbdacdb30.cc869007c1da961363608466444008ce
Exploitability Classification: 可能不可利用

```
栈回溯:
```json

#0  0x00007ffff7e0400b in raise () from /lib/x86_64-linux-gnu/libc.so.6 objfile: /usr/lib/x86_64-linux-gnu/libc-2.31.so offset: 0x4300b
#1  0x00005555555552db in testBenignSignal () at test.c:9 objfile: /home/tianmai/workspace/tmp/test1 offset: 0x12db
#2  0x0000555555555906 in main (argc=2, argv=0x7fffffffdd38) at test.c:292 objfile: /home/tianmai/workspace/tmp/test1 offset: 0x1906

```
崩溃点汇编:
```json

   0x5555555552c9 <testbenignsignal>:	endbr64
   0x5555555552cd <testbenignsignal+4>:	push   rbp
   0x5555555552ce <testbenignsignal+5>:	mov    rbp,rsp
   0x5555555552d1 <testbenignsignal+8>:	mov    edi,0x3
=> 0x5555555552d6 <testbenignsignal+13>:	call   0x555555555110 <raise@plt>
   0x5555555552db <testbenignsignal+18>:	nop
   0x5555555552dc <testbenignsignal+19>:	pop    rbp
   0x5555555552dd <testbenignsignal+20>:	ret
   0x5555555552de <testbadinstruction>:	endbr64

```
崩溃点源代码:
```json
test.c:9

4	#include <stdlib.h>
5	#include <sys/mman.h>
6	#include <signal.h>
7	#include <unistd.h>
8	int testBenignSignal() {
9	    raise(SIGQUIT);   <-<
10	}
11	
12	typedef void(*voidfn)(void);
13	int testBadInstruction() {

```
