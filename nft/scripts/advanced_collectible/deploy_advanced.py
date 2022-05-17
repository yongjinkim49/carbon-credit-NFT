#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, network, config, Settings, ERC721VaultFactory
from scripts.helpful_scripts import fund_with_link, get_publish_source

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    advanced_collectible = AdvancedCollectible.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link_token"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": dev},
        publish_source=get_publish_source(),
    )
    fund_with_link(advanced_collectible.address)

    Settings.deploy({"from": dev})
    ERC721VaultFactory.deploy(Settings[0], {"from": dev})

    # print("print Balance")
    # print(AdvancedCollectible[0].balance())

    

    return advanced_collectible
