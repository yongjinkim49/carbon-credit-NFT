
# C-Block: Marketplace for carbon-credit NFTs Fractions from forestry projects

<h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1t5-R_76JmHLmhAaG2n9Sf1ApvbymEyog)
  <a name="logo" href="https://drive.google.com/file/d/1t5-R_76JmHLmhAaG2n9Sf1ApvbymEyog/view?usp=sharing" alt="Carbon Credit Marketplace" width="200"></a>
  <br>
  C-Block: Decentralised Carbon Credit Marketplace
  </h4>
</div>
<p><font size="3">
This Repository is a platform for the development of a DApp marketplace for Carbon Credit NFT fractions. Our goal is to have a decentralized, trustless, and transparent marketplace where farmers and landowners have access to a bigger market share and more opportunities.
  
  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1WoPft4sMm-cRpxaCM3tY7Ure2ErbIXOa)

  </h4>
</div>
<p><font size="3">
  
In a Nutshell, Carbon offsets is the reduction or removal of emissions of carbon dioxide or other greenhouse gases created in order to compensate for emissions made elsewhere. Broader picture, it allows industries to reduce their overall carbon footprint by investing in projects that can offer measurable Carbon Capture from the environment. 
    
  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1MHjvzIQZmmL7kvVh5ai3JE52hOukQEzo)

## Infrastructure / Solution / Approach
    
We first provide a comparison of the status quo processes and our solution at a high-level. The current process is slow, costly, and limited to a small number of players. There is no set standard of auditing and thereby the process takes months to years until it reaches the end-users (i.e. polluters). The status quo method, even for recent blockchain solutions for this maintain the "offset first & HOPE end-users will by years later" business model. This is a GREAT obstacle in growing the market and allowing it to reach full potential in scale and liquidity. Our blockchain based NFT-fractioning system with a new model tackles this shortcomings effectively. This is elaborated in the following image.
    
  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1csoSuH-r4chefz4xfpMfNUeBXVe0typl)

  </h4>
    
We do maintain the retirement system of carbon-credits. However, we do so in a near-concurrent manner such that the polluters pay for the carbon-credits AT THE SAME TIME, it is being offset. This allows more landlords to take part, creating a positive cycle in growing the market and pulling in more customers into the protocol. As this is concurrent, there is always a moral hazard issue. We effectively tackle this through domain expert opinions on the DAO consensus process and the month-delay payment system to the landlords and auditors. The payment will be held on our protocol for such set time period outlined by our smart contracts and so utimately deliver them the payment once the the landlords have satisfied their contracts in maintaining project integrity.     

  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1wfObw7mFrq9fMmkYQ7E9CVGaqOYF3v4Z)

  </h4>
</div>
<p><font size="3">


To summarzie our solution is to challenge the existing market players and eliminate intermediaries. This is done by the creation of a decentralized marketplace as demonstrated above. With this project, we have the current protocol players:
  - The farmers/ landowners will have a go-to protocol to present their lots
  - A decentralized autonomous organizations (DAO) will be formed by set of auditors in order to present, find, propose, and vote for lots
  - Pollutors are the actual end-users who will demand/ buy carbon credits as fractions of NFTs
  
Based on the above, the project will be minted as a ERC 721 NFT compatible with the Ethereum blockchain. A deterministic (decided by the DAO) number of ERC 20 tokens will be minted for each project. These ERC20 tokens would represent a unit portion of the Carbon Capturd by the Project. Industries / Institutions / Individuals will be able to buy these ERC20 tokens representing a unit of Carbon Offset.  

    
## Prerequisites

Install the following:

- Nodejs, npm, pipx, yarn, and hardhat
- Python
- Brownie 


# Usage / Implementation
  
There are 2 types of NFTs here. 
1. `SimpleCollectibles.sol`
2. `AdvancedCollectibles.sol`

The simple collectibles work on a local network, however the advanced requires a testnet. We default to rinkeby since that seems to be the testing standard for NFT platforms. You will need testnet rinkeby ETH and testnet Rinkeby LINK. You can find faucets for both in the [Chainlink documentation](https://docs.chain.link/docs/link-token-contracts#rinkeby). 

We will use the Advanced Collections contract implementation. Each project is associated with an NFT, containing an image and a json file. This json file contains:
  - informations relative to the asset: 
    - geolocation
    - type of project 
    - soil main composition
    - main type of trees
    - ...
  
  - informations relative to the ERC20 tokens that will be traded as "shares" of this asset:
    - ERC20 token address
    - ERC20 token total supply
    - ERC20 token decimals

Inforamtions relative to the asset are randomly generated from a database of event we have build. They will be expanded with the addition of real projects.
  
---
  
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

# DAO-C-Block: Marketplace for carbon-credit NFTs Fractions from forestry projects

 Link for our C-Block DAO github repository:  [DAO Code](https://github.com/TarekMohammad1/DAO-ESG-Chainlink)
  
As Web3 and the blockchain bleed more and more into the mainstream, new acronyms get thrown around regularly with little explanation as to what they mean, including this one: DAO.    

Decentralized autonomous organizations (DAOs) are kind of like clubs for crypto enthusiasts, only they typically operate under a shared goal, give each member equal say in making decisions, and can potentially have more money than most clubs would ever know what to do with. 

Within C-Block Chainlink project, the DAO plays an indipensable role in creating a healthy environment for voting to different proposals including but not limited to lots proposols.

In this repository, we are introducing a DAO that will be formed by auditors who are responsible to create proposals and push them for voting.

# Usage / Implementation

There is one smart contract that is needed to be governed:
1. `Proposals.sol`

This contract allows auditors to create new proposals and push them for voting. 


You'll need [testnet Rinkeby](https://faucet.rinkeby.io/) and [testnet LINK](https://rinkeby.chain.link/) in the wallet associated with your private key. 

```
brownie run scripts/governance_standard/deploy_and_run_for_proposals.py --network rinkeby
```

# Front-end UI for DAO members / Protocol managers / End-users (pollutors)
We also created an interface to provide a high-level overview of the innerworkings of our protocol. We have three interfaces intended for three differen players (participants) of our protocol. We list them in order: t
  
- Interface 1: intended for DAO members' decision making process and consensus, 
- Interface 2: for the protocol managers to observe and assess the decisions from DAO
- Interface 3: a marketplace interface for the end-users for our protocol, i.e. polluters such as Microsoft, Google, etc
  
 Please refer to our repository below for more detail: [Interface Base] https://github.com/XiaorenY/carbon_block_dapp

 The interface will be extended to incorporate more user-friendly features and functionalities.
  
  
# The Path Ahead
Though, we have made substantial progress towards our end goal of a decentralised Carbon Credit Marketplace, there is still 'Miles to go'. Some of the updates / initiatives that we have in the works - 
* Implementing collaboration with off chain and other on chain Carbon Credit Marketplace to further improve the liquidity within the Market. 
* To plan for the future - We understand the current voluntary Carbon Credit Market will grow substantially if not exponentially in the coming future. This would call for the current model to expnand to ther avenues of Carbon Capture, say industrial carbon capture, renewable energy projects, advanced technological projects.
* Since, the active Carbon Capture projects could be highly volatile in terms of actual output. We need to implement a methodology to source, manage and create a pool or repository of Carbon Credits to cover any potential shortfall in production. 

  <h1 align="center">
  
  ![image](https://drive.google.com/uc?export=view&id=1UCpQn7Cb-843Uiwee69sD6rwGlGlLTHz)

  </h4>  
  
# Resources Used

The project is created in parts for the submission of the Chainlink Hackathon. A great thanks to Patrick Collins and the whole Chainlink Hackathon team for the essential tutorials and support provided during the project execution. 

* [Chainlink Documentation](https://docs.chain.link/docs)
* [Chainlink Hackathon Discord](https://discord.gg/2YHSAey
* Check out the [Chainlink documentation](https://docs.chain.link/docs) to get started from any level of smart contract engineering. 
* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie.
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/).

## License

This project is licensed under the [MIT license](LICENSE).

