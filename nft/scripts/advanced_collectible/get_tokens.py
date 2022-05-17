#!/usr/bin/python3
from brownie import SimpleCollectible, AdvancedCollectible, accounts, network, config
from metadata import sample_metadata


def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(SimpleCollectible) - 1]
    breakpoint()
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(number_of_advanced_collectibles)
