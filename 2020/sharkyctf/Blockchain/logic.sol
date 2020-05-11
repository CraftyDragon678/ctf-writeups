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
