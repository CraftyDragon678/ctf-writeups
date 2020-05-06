# assembly

## 1. 데이터의 크기

1 bit가 기본  
1 byte = 8bit(ASCII (Char))
- word = 2byte(Unicode)
- double word = 4byte
- quad word = 8byte
- paragraph = 16byte

1KB(kilobyte) = 1024byte
1MB(megabyte) = 1024KB


## 2. 진수

컴퓨터는 2진수로 통신.
표기는 16 진수를 많이 씀.
<hr/>

## 3. 레지스터 (register)

레지스터(extended)는 일반적으로 32bit(4byte) 0x00000000 ~ 0xffffffff

| 종류 | 설명 |
| ---- | ---- |
| EAX(=accumulator register) | 수학 연산, I/O연산, INT 21 |
| EBX(=base register) | Base또는 Pointer(index) |
| ECX(=counter register) | 루프 및 반복 |
| EDX(=data register) | EAX 보조 역할 산술 연산에 사용. 곱셈 나눗셈 결과 저장, 문자 출력|

```
|           EAX         |
|      |      |   AX    |
|      |      | AH | AL |
```

E: 32bit, X: 16bit, H: 8bit(high), L: 8bit(low)



**세그먼트 레지스터:**  
CS(Code Segment) – 코드를 저장하는 메모리 블록  
DS(Data Segment) – 데이터를 저장하는 메모리 블록  
EX(Extra Segment) – 비디오와 관련된 것을 위해 사용됨  
SS(Stack Segment) – 루틴으로부터 리턴 어드레스를 저장하기 위해 프로세서에 의해 사용되는 레지스터 

**인덱스 레지스터:**  
ESI(Source Index) – 문자열/배열의 소스를 지정하기 위해 사용됨. 이것이 가리키는 값이 주로 EDI가 가리키는 주소의 값에 복사됨  
EDI(Destination Index) – 문자열/배열의 목적지를 지정하기 위해 사용됨.  
EIP(Instruction Pointer) – 다음 명령의 주소를 저장하고, 그래서 직접적으로 변경될 수 없음. 


**스택 레지스터:**  
EBP(Base Pointer) – 스택 오퍼레이션을 위해 SP 와 연결되어 사용됨. (아래쪽, 높은 주소)  
ESP(Stack Pointer) - 하나의 스택 프레임의 끝 지점 주소가 저장된다. (윗쪽, 낮은 주소)

**특별한 목적을 위한 레지스터:**  
EIP(Instruction Pointer) – 실행된 명령의 offset 를 가지고 있음.  
Flag – 분기(branching)를 위해 사용됨. 플래그 레지스터는 크기가 1 비트이다(Z, P, A, O, S, D, C, T, I)

## 4. 기본 어셈블리(Intel)

### 4.1. MOV
MOV 목적지 값

### 4.2. INC, DEC
INC: 증가  
DEC: 감소

### 4.3. POP, PUSH

POP: 빼내기  
PUSH: 넣기

### 4.4. ADD, SUB, MUL, DIV
ADD reg1, reg2 // reg1 += reg2   
SUB ===  
MUL reg // ax = ax(ah) * reg  
DIV ===

### 4.5 AND, OR, XOR, NOT
AND reg1, reg2 // reg1 & = reg2  
OR ===  
XOR ===  
NOT reg // reg = !reg
