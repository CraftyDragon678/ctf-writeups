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
