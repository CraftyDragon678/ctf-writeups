# SharkyCTF writeup

[Blockchain](#blockchain-2)

- [Warmup](#warmup97)
- [Logic](#logic195)

[Misc](#misc-1)

[Network](#net-1)

[Pwnable](#pwn-1)

[Reversing](#rev-3)

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

ethereum IDE에서 컴파일을 한 후, contract를 추가 해주면 다음과 같이 뜬다
![warmup](Blockchain/warmup.png)

위쪽 value에 다음과 같이 0.005 ether를 넣어주고 unlock을다누른다
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

## Net (1)

## Pwn (1)

## Rev (3)

## Steganography (0)

:\

## Web (3)
