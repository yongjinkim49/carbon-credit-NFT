#!/usr/bin/python3
from brownie import SimpleCollectible, AdvancedCollectible, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_type, OPENSEA_FORMAT


proj_metadata_dic = {
    "REFORESTATION": "https://ipfs.io/ipfs/QmQTRZhz8CTSSxsU4RtxpnwPyf735hUZL3xKY6M29Ajc7t?filename=0-REFORESTATION.json",
    "AFORESTATION": "https://ipfs.io/ipfs/QmcadZ8YwPT7qLVG6xpjWTNwFx5tSdbr94tWXeGzSnksus?filename=0-AFORESTATION.json",
    "AVOIDED_CONVERSION":"ipfs://QmYDxQYa6d1ywGn1AhPtnQZ6TH8YhvE7dtrxJy5KLGT3C1?filename=0-AVOIDED_CONVERSION.json",
    "LAND_CONSERVATION":"ipfs://QmXFVwb9yfLvFk6QMVKs8YffbbDc6FuSMC55TpfJqyNVq2?filename=1-LAND_CONSERVATION.json"
}

def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_advanced_collectibles)
    )
    for token_id in range(number_of_advanced_collectibles):
        typeofasset = get_type(advanced_collectible.tokenIdToTypeOfAsset(token_id))
        print('typeofasset :',typeofasset)
        print("proj_metadata_dic",proj_metadata_dic)
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            set_tokenURI(token_id, advanced_collectible,
                         proj_metadata_dic[typeofasset])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
