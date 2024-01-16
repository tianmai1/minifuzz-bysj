#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <signal.h>
#include <unistd.h>
int testBenignSignal() {
    raise(SIGQUIT);
}

typedef void(*voidfn)(void);
int testBadInstruction() {
    char *a = valloc(64);
    mprotect(a, 64, PROT_READ | PROT_WRITE | PROT_EXEC);
    voidfn bad_function = (voidfn)a;
    memset(a, 0xff, 64);
    bad_function();
    return 0;
}

void testAbortSignal() {
    raise(SIGABRT);
}

int testBlockMoveAv() {
#if defined (__x86_64__)
    asm ("mov $512,%ecx");
    asm ("rep movsq");
#else
    asm ("mov $512,%ecx");
    asm ("rep movsd");
#endif
}

int testBranchAv() {
#if defined(__arm__)
    void (*p)() = (void*)0xFFFFFFFF;
    p();
    return 0;
#else
    asm ("call *0xFFFFFFF");
#endif
    return 0;
}

int testBranchAvNearNull() {
#if defined(__arm__)
    void (*p)() = (void*)0;
    p();
    return 0;
#else
    asm ("call *0x00");
#endif
    return 0;
}


#if defined (__x86_64__)
    #define WORD_SIZE 8
#else
    #define WORD_SIZE 4
#endif

int i;

int the_overflow() {
    char a[WORD_SIZE];
    the_overflow();
    return 0;
}

int testDeepStack() {
    the_overflow();
    return 0;
}

int testDestAv() {

    char *a;
    a[1024 * 64] = 'A';
}

int testDestAvNearNull() {
    asm ("mov %eax, 0x0");
}


int testFloatingPointException() {

    int a = 0;
    int b = 1;
    a = b/a;
}




typedef void(*voidfn)(void);
int testHeapError() {
    char *a = malloc(64);
    memset(a, 'A', 1024);
    char *b = malloc(64);
    free(a);
    free(b);
    return 0;
}


int i;

void crash() {
    char a[1];
    for (i = 0; i< 20480; i++) {
        a[i] = 'A';
    }
    printf("%s\n", a);
}

int testPossibleStackCorruption() {
    crash();
}


#if defined (__x86_64__)
    #define WORD_SIZE 8
#else
    #define WORD_SIZE 4
#endif

int i;

int the_overflow1() {
    char a[WORD_SIZE];

    for (i = 0; i < WORD_SIZE*4; i++) {
        a[i] = (char)0xff;
    }
    return 0;
}

int testReturnAv() {
    the_overflow1();
    return 0;
}



typedef void(*voidfn)(void);
int testSegFaultOnPc() {
    char *a = valloc(64);
    mprotect(a, 64, PROT_WRITE);
    voidfn bad_function = (voidfn)a;
    memset(a, 0xff, 64);
    bad_function();
    return 0;
}


int testSegFaultOnPcNearNull() {

    char (*a)() = 0;
    (void)(*a)();
    return 0;
}

int testSourceAv() {

    char *a = "xx";
    char b;
    int i;
    for (i = 0; i < 1024 * 1024; i++) {
        b = a[i];
    }
}

int testSourceAvNearNull() {
    asm("mov 0x0F, %eax");
}

int i;

void overflow1() {
    char a[1];
    for (i = 0; i< 16; i++) {
        a[i] = 'A';
    }
    printf("%s\n", a);
}

int testStackBufferOverflow() {
    overflow1();
}


typedef void(*voidfn)(void);
int testStackCodeExecution() {
    char a[12] = "aaaaaaaaaa";
    voidfn bad_function = (voidfn)a;
    bad_function();
    return 0;
}



int testUncategorizedSignal() {
    raise(SIGPIPE);
}


void loop4(){
}


void loop3(){
  loop4();
}

void loop2(){
  loop3();
}

void loop1(){
  loop2();
}


void loop(){
  loop1();
}

static int Infinite_loop()
{  
  printf("this is Infinite_loop");
  while (1)
  {
    loop();
  }
  return 0;
}

static int Infinite_loop1()
{  
  printf("this is Infinite_loop");
  int a=1,b=1;
  a+=1;
  a=a-b;
  Infinite_loop1();
  return 0;
}

static sleep1()
{  
  sleep(1000);
}








int main(int argc, char *argv[]) {
    // 检查命令行参数数量
    if (argc < 2) {
        printf("请提供文件名作为命令行参数\n");
        return 1;
    }

    // 从命令行参数中获取文件名
    char *fileName = argv[1];

    FILE *file;
    char firstChar;

    // 打开文件
    file = fopen(fileName, "r");

    // 检查文件是否成功打开
    if (file == NULL) {
        printf("无法打开文件 %s\n", fileName);
        return 1;
    }

    // 读取第一个字符
    firstChar = fgetc(file);

    // 根据第一个字符跳转到相应的步骤
    switch (firstChar) {
        case 'A':
            testBenignSignal();
            break;
        case 'B':
            testAbortSignal();
            // 执行步骤B的操作
            break;
        case 'C':
            testBadInstruction();
            // 执行步骤C的操作
            break;
        case 'D':
            testBlockMoveAv();
            break;
        case 'E':
            testBranchAv();
            // 执行步骤B的操作
            break;
        case 'F':
            testBranchAvNearNull();
            // 执行步骤C的操作
            break;
        case 'G':
            testDeepStack();
            break;
        case 'H':
            testDestAv();
            // 执行步骤B的操作
            break;
        case 'I':
            testDestAvNearNull();
            // 执行步骤C的操作
            break;
        case 'J':
            testFloatingPointException();
            break;
        case 'K':
            testHeapError();
            // 执行步骤B的操作
            break;
        case 'L':
            testPossibleStackCorruption();
            // 执行步骤C的操作
            break;
        case 'M':
            testReturnAv();
            break;
        case 'N':
            testSegFaultOnPc();
            // 执行步骤B的操作
            break;
        case 'O':
            testSegFaultOnPcNearNull();
            // 执行步骤C的操作
            break;
        case 'P':
            testSourceAv();
            break;
        case 'Q':
            testSourceAvNearNull();
            // 执行步骤B的操作
            break;
        case 'R':
            testStackBufferOverflow();
            // 执行步骤C的操作
            break;
        case 'S':
            testStackCodeExecution();
            // 执行步骤B的操作
            break;
        case 'T':
            testUncategorizedSignal();
            // 执行步骤C的操作
            break;
            
        case 'U':
            Infinite_loop();
            // 执行步骤C的操作
            break;
        case 'Y':
            Infinite_loop1();
            // 执行步骤C的操作
            break;
        case 'Z':
            sleep1();
            // 执行步骤C的操作
            break;
        default:
            printf("未知的字符\n");
            // 处理未知字符的情况
            break;
    }

    // 关闭文件
    fclose(file);

    return 0;
}

























