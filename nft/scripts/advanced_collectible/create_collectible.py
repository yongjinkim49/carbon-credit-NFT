#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, config, ERC721VaultFactory
from scripts.helpful_scripts import get_drought, get_fire, get_flood, get_geo, get_soil, get_trees, get_type, fund_with_link, listen_for_event
import time


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    #advanced_collectible = dev
    # For it to focus the most recent one!
    fund_with_link(advanced_collectible.address)
    
    print('voici le dev :',dev)
    print('voici advanced collectible :', advanced_collectible)
    transaction = advanced_collectible.createCollectible("None", {"from": dev})
    
    #advanced_collectible.approve(dev,0,{'from': advanced_collectible})
    #tx = dev[0].mint("Brazil", "B", advanced_collectible, 0, 100, 20000, 10, {"from": dev})
    
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    # time.sleep(35)
    listen_for_event(
        advanced_collectible, "ReturnedCollectible", timeout=200, poll_interval=10
    )
    requestId = transaction.events["RequestedCollectible"]["requestId"]
    token_id = advanced_collectible.requestIdToTokenId(requestId)
    typeofasset = get_type(advanced_collectible.tokenIdToTypeOfAsset(token_id))
    geolocation = get_geo(advanced_collectible.tokenIdToGeolocation(token_id))
    soil = get_soil(advanced_collectible.tokenIdToSoil(token_id))
    trees = get_trees(advanced_collectible.tokenIdToTrees(token_id))
    floodrisk = get_flood(advanced_collectible.tokenIdToFloodRisk(token_id))
    firerisk = get_fire(advanced_collectible.tokenIdToFireRisk(token_id))
    droughtrisk = get_drought(advanced_collectible.tokenIdToDroughtRisk(token_id))
    
    print("Type of project of tokenId {} is {}".format(token_id, typeofasset))
    print("Geolocation of tokenId {} is {}".format(token_id, geolocation))
    print("Soil of tokenId {} is {}".format(token_id, soil))
    print("Trees of tokenId {} is {}".format(token_id, trees))
    print("Exposure to flood Risk of tokenId {} is {}".format(token_id, floodrisk))
    print("Exposure to fire risk of tokenId {} is {}".format(token_id, firerisk))
    print("Exposure to drought risk of tokenId {} is {}".format(token_id, droughtrisk))
    
