> Update: You should use `ipfs://` instead of `https://ipfs.io/` for your tokenURI

# C-Block: Marketplace for carbon-credit NFTs from forestry projects

<h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1t5-R_76JmHLmhAaG2n9Sf1ApvbymEyog)
  <a name="logo" href="https://drive.google.com/file/d/1t5-R_76JmHLmhAaG2n9Sf1ApvbymEyog/view?usp=sharing" alt="Carbon Credit Marketplace" width="200"></a>
  <br>
  C-Block: Decentralised Carbon Credit Marketplace
  </h4>
</div>
<p><font size="3">
This Repo is desgiend to serve as a platform for the development of a decentralised market place for Carbon Credit transactions. Our aim behind the project is to have a decentralised, democratic and transparent platform where farmrers, landowners may interact with Large industries and institutional investors interested in the voluntary carbon capture projects.  
  
  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1WoPft4sMm-cRpxaCM3tY7Ure2ErbIXOa)

  </h4>
</div>
<p><font size="3">
Carbon offsets in a Nut Shell, is the reduction or removal of emissions of carbon dioxide or other greenhouse gases made in order to compensate for emissions made elsewhere. Broad Picture, it allows industries to reduce their overall carbon footprint by investing in projects that can offer measurable Carbon Capture from the environment. 
    
  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1MHjvzIQZmmL7kvVh5ai3JE52hOukQEzo)

## Infrastructure / Solution / Approach
    
  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1T0axKQpcUirAld_vUQIfSO8_8ow3myJM)

  </h4>
</div>
<p><font size="3">

Our solution to challnge the existing highly centralised marketplace is to implement a decentralised protocol as shown above. THe landowners could come to our platform with their projects. A DAO of auditors and domain experts would analyse the credibility of the project. Once a significant majority is reached, the project would be minted as a ERC 721 NFT compatible with the Ethereum blockchain. A deterministic (decided by the DAO) number of ERC 20 tokens would be minted for each project. These ERC 20 token would represent a unit portion of the Carbon Capturd by the Project. Industries / Institutions / Individuals would then b able to buy these ERC20 tokens represnting a unit of Carbon Offset.  
  
    
## Prerequisites

Please install or have installed the following:

- Nodejs and npm
- Python
- Brownie 


# Usage / Implementation
  
There are 2 types of NFTs here. 
1. `SimpleCollectibles.sol`
2. `AdvancedCollectibles.sol`

The simple collectibles work on a local network,  however the advanced requires a testnet. We default to rinkeby since that seems to be the testing standard for NFT platforms. You will need testnet rinkeby ETH and testnet Rinkeby LINK. You can find faucets for both in the [Chainlink documentation](https://docs.chain.link/docs/link-token-contracts#rinkeby). 

# We will use the Advanced Collections contract implementation. 

You'll need [testnet Rinkeby](https://faucet.rinkeby.io/) and [testnet LINK](https://rinkeby.chain.link/) in the wallet associated with your private key. 

```
brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby
brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby
```
Then:
```
brownie run scripts/advanced_collectible/create_metadata.py --network rinkeby
brownie run scripts/advanced_collectible/set_tokenuri.py --network rinkeby
```

## Resources Used

The project is created in parts towards the submission for the Chainlink Hackathon. A great thanks to Patrick Collins and the whole Chainlink Hackathon team for the essential tutorials and support provided during the project execution. 

* [Chainlink Documentation](https://docs.chain.link/docs)
* [Chainlink Hackathon Discord](https://discord.gg/2YHSAey
* Check out the [Chainlink documentation](https://docs.chain.link/docs) to get started from any level of smart contract engineering. 
* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).

## License

This project is licensed under the [MIT license](LICENSE).

