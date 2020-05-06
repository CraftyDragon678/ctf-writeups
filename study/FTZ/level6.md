PW : `what the hell`

```bash
$ ssh level6@192.168.5.28
level6@192.168.5.28's password: 


hint - 인포샵 bbs의 텔넷 접속 메뉴에서 많이 사용되던 해킹 방법이다.


```

접속을 하자마자 이렇게 뜬다.  
엔터를 누르면 접속 메뉴가 뜬다.
```bash

  #####################################
  ##                                 ##
  ##         텔넷 접속 서비스        ##
  ##                                 ##
  ##                                 ##
  ##     1. 하이텔     2. 나우누리   ##
  ##     3. 천리안                   ##
  ##                                 ##
  #####################################

접속하고 싶은 bbs를 선택하세요 : 
```

`Ctrl+c`를 쓰려 했지만 쓰지 못한다.
```bash
접속하고 싶은 bbs를 선택하세요 : Can't use ctrl+c
Can't use ctrl+c
Can't use ctrl+c
Can't use ctrl+c
Can't use ctrl+c
```

항상 힌트 파일이 존재 했었으니 텔넷 또는 ssh 접속을 하면  
우선 cat hint를 해주고 텔넷 접속 서비스 프로그램을 실행하는 것 같다  
그럼 프로그램에서 `Ctrl+C`를 막았다고 생각을 하면  
힌트가 떴을 때 `SIGINT`를 보내주면 될 것이다.

```bash
hint - 인포샵 bbs의 텔넷 접속 메뉴에서 많이 사용되던 해킹 방법이다.


[level6@ftz level6]$ ls -al
total 104
drwxr-xr-x    4 root     level6       4096 Mar  5  2003 .
drwxr-xr-x   34 root     root         4096 Sep 10  2011 ..
-rw-------    1 root     root            1 Jan 15  2010 .bash_history
-rw-r--r--    1 root     root           12 Nov 24  2000 .bash_login
-rw-r--r--    1 root     root           24 Feb 24  2002 .bash_logout
-rw-r--r--    1 root     root          224 Feb 24  2002 .bash_profile
-rw-r--r--    1 root     root          163 Mar  5  2003 .bashrc
-rw-r--r--    1 root     root          400 Sep 24  2000 .cshrc
-rw-r--r--    1 root     root         4742 Sep 24  2000 .emacs
-r--r--r--    1 root     root          319 Sep 24  2000 .gtkrc
-rw-r--r--    1 root     root          100 Sep 24  2000 .gvimrc
-rw-r--r--    1 root     root           72 Nov 23  2000 hint
-rw-r--r--    1 root     root          226 Sep 24  2000 .muttrc
-rw-r-----    1 root     level6         36 Mar 24  2000 password
-rw-r--r--    1 root     root          367 Sep 24  2000 .profile
drwxr-xr-x    2 root     level6       4096 May 16  2005 public_html
drwxrwxr-x    2 root     level6       4096 Jan 14  2009 tmp
-rwxr-x---    1 root     level6      14910 Mar  5  2003 tn
-rw-r--r--    1 root     root            1 May  7  2002 .viminfo
-rw-r--r--    1 root     root         4145 Sep 24  2000 .vimrc
-rw-r--r--    1 root     root          245 Sep 24  2000 .Xdefaults
[level6@ftz level6]$ cat password 
Level7 password is "come together".
```
레벨7의 패스워드는 `come together`이다.