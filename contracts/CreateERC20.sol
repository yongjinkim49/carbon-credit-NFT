// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../openZeppelin/token/ERC20/ERC20.sol";

contract EasyToken is ERC20 {

    uint256 numTokensGwei;

    constructor(string memory tokenName, string memory tokenSymbol) public ERC20(tokenName, tokenSymbol){}

    
    function mintERC20(address walletAddress, uint256 numTokens) public {

        numTokensGwei = 1000000000000000000000000 * numTokens;

        _mint(walletAddress, numTokensGwei);
    }

}