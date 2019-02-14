# trust ctf

## MISC

### MIC CHECK

![mic check](MISC/MIC&#32;CHECK!/screenshot/check.png)

췌ㅔㅔㄱ

**Flag : TRUST{Welcome_CTF_Have_FUN!}**  
Welcome ~~to~~ CTF, Have FUN!


### Easy Taebo

@==(^0^)@  
@(^0^)==@

넷캣으로 연결하게 되어있다.
간단하게 pwntools를 이용해서 익스플로잇을 짜면 된다.

```py
from pwn import *
import re

list = {'left_jab' : '@==(^0^)@',
    'left_mid_jab' : '@=(^0^)@',
    'mid_jab' : '@(^0^)@',
    'right_mid_jab' : '@(^0^)=@',
    'right_jab' : '@(^0^)==@',
    'left_hook' : '@(^0^)@==',
    'right_hook' : '==@(^0^)@',
    'left_speedball' : '@@@(^0^)',
    'right_speedball' : '(^0^)@@@',
    'left_kick' : '@||(^0^)==@',
    'mid_kick' : '@==(^||^)==@',
    'right_kick' : '@==(^0^)||@'}
```
리스트를 만들어 주고
```py

cn = remote("server.trustctf.com", 44923)

while True:
    prob = cn.recvline()
    print prob
    if prob[0] != "T" or prob[6] == "i":
        continue
    prob = re.sub("Taebo \d* : ", "", prob)
    prob = prob.replace(' >>', '')
    log.info('PROBLEM : ' + prob)
    ans = ""
    a = prob[:-2].split(" + ")
    for b in a:
        ans += list[b] + " "
    log.info('ANSWER : ' + str(ans))
    cn.sendline(ans)
    print '\n'
```
접속해서 해결.

**Flag : TRUST{w0w_y0u_9o7_4_w0nd3rfu1_b0dy_lik3_m3}**  
wow you got a wonderful body like me

### IDENTITY_5

identity_5.apk파일을 다운로드하면 일단 실행하라고 되어있다.

적당히 AVD에다가 넣고 돌리면 QR코드가 하나 등장한다  
하지만 이것은 빙산의 일각.

![i$_7H!s_Qr_C0d3?](MISC/IDENTITY_5/screenshot/qrcode.png)

그 다음 화면에서 남한어 번역기 뭐라고 뜨는데 어딜 클릭할지를 몰라서 그냥 디컴파일 시켰다.

jadx에 넣고 디컴시키면 되게 많은 것이 있는데 전부다 저장시킨 다음에 Visual Studio Code로 불러와서
Visual Studio Code의 검색기능을 활용했다.

![search](MISC/IDENTITY_5/screenshot/search.png)

그러니 `MainActivity.java`와 `secondhacking.java`에 `bit.ly` 주소가 적혀있다. 이렇게 2번 4번이 있고
apk파일 안에 res/drawable로 들어가면 시작화면에 있던 flag.jpg파일 (hex를 읽어보니 확장자는 .jpg가 아니라 .png가 되어야 한다.) 이 있고, 바이너리에 빠진 flag3파일이 나중에 추가로 공개 되었다.

차례대로 QR코드를 읽으면 
+ TRUST{
+ Th1s_1s_
+ fl@g_@nd
+ r0id_@dd_Qr
+ c0d3}   
가 된다.
쭉 이으면 

**Flag : TRUST{Th1s_1s_fl@g_@ndr0id_@dd_Qrc0d3}**  
This is flag android add(and?) qrcode


### Starcraft2

운 좋게도 스타를 좋아하는 유저라서 스타2가 깔려 있다
그래서 10분 만에 풀어 낼 수 있었다.

그냥 파일을 맵 에디터로 열면 미니맵에 플래그가 쓰여있다.

~~(어머나 라업을 써야하는데 셧다운제 때문에 맵 에디터를 쓰질 못한다... 아뿔싸)~~

**Flag : TRUST{FUN}**


### RSA1

RSA 암호문 : 1649729212658550722856763813613372  
암호화에 사용된 소수 1 : 36465956589847261  
암호화에 사용된 소수 2 : 46496464168468673  
복호화 키 : 1275312736838027047985273062147003

문제에는 이렇게 쓰여있다.  
이 문제를 풀기 위해서 공부를 좀 했는데, 우선

C = 암호문  
p = 소수1  
q = 소수2  
d = 개인키(복호화 키)
n = $p × q$

이렇게 하면
$C=1649729212658550722856763813613372$  
$p = 36465956589847261$  
$q = 46496464168468673$  
$d = 1275312736838027047985273062147003$
가 나온다.

복호화 식은 $C^d \: mod \: n$이 되므로 계산해 주면 되는데...
문제는 $C^d$를 계산하기에는 수가 너무 커져 버린다. 그래서 뭔갈 좀 찾아 봤는데 나오는 것이 $a^b\%n$에 관한 글이었다. 

```py
def powermod4(a, b, n):
    if b == 1:
        return a % n
    r = powermod4(a, b / 2, n)
    r = r * r % n
    if (b & 1) == 1:
        r = r * a % n
    return r
```
_from [this](https://helloacm.com/compute-powermod-abn/) site_

```py
powermod4(C, d, n)
```
을 해주니 정상적으로 나머지가 잘 나왔다.

(python3에서 제한이 걸려서 안되니깐 python2로 실행했다.)

**나머지 : 65838295874878759585488995896489**

이제 이 나머지들을 두자리씩 끊어서 ascii로 고치면 된다.

**Flag : ASR_W0NK_U0Y_Y@Y**  
ASR WONK UOY YAY (음? 뒤집으면 된다.)  
YAY YOU KNOW RSA