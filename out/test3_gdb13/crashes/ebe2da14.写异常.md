复线命令:
```json
/home/tianmai/workspace/tmp/test1 out/test3_gdb13/crashes/crashes/crash_000005

```
分析结果:
```json

Description: 写异常
Hash: a682746ad3ed601690ada323dd1d174c.a682746ad3ed601690ada323dd1d174c
Exploitability Classification: 可能可利用

```
栈回溯:
```json

#0  0x000055555555535b in testBlockMoveAv () at test.c:29 objfile: /home/tianmai/workspace/tmp/test1 offset: 0x135b
#1  0x0000555555555933 in main (argc=2, argv=0x7fffffffdd38) at test.c:303 objfile: /home/tianmai/workspace/tmp/test1 offset: 0x1933

```
崩溃点汇编:
```json

   0x55555555534d <testabortsignal+20>:	ret
   0x55555555534e <testblockmoveav>:	endbr64
   0x555555555352 <testblockmoveav+4>:	push   rbp
   0x555555555353 <testblockmoveav+5>:	mov    rbp,rsp
   0x555555555356 <testblockmoveav+8>:	mov    ecx,0x200
=> 0x55555555535b <testblockmoveav+13>:	rep movs qword ptr es:[rdi],qword ptr ds:[rsi]
   0x55555555535e <testblockmoveav+16>:	nop
   0x55555555535f <testblockmoveav+17>:	pop    rbp
   0x555555555360 <testblockmoveav+18>:	ret

```
崩溃点源代码:
```json
test.c:29

24	}
25	
26	int testBlockMoveAv() {
27	#if defined (__x86_64__)
28	    asm ("mov $512,%ecx");
29	    asm ("rep movsq");   <-<
30	#else
31	    asm ("mov $512,%ecx");
32	    asm ("rep movsd");
33	#endif

```
