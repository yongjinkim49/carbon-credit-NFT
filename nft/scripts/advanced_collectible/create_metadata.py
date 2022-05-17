#!/usr/bin/python3
import os
import requests
import json
from brownie import AdvancedCollectible, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_drought, get_fire, get_flood, get_geo, get_soil, get_trees, get_type
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

breed_to_image_uri = {
    'AFORESTATION':"ipfs://QmPtproz2F1WwU1XviQwfYJHNQ28XjtzwZsRR3JdA4zUED?filename=aforestation.png",
    'REFORESTATION':"ipfs://QmQ3rTwxzK4kLRnt3gHgpsMvXm2wD37uSiXn7B5X9RLouA?filename=reforestation.png",
    "AVOIDED_CONVERSION":"ipfs://QmQmU2i5H9bz6VWjUMUJskL9NEmSizQkmjKac29LtBiyXV?filename=avoided-conversion.png"
}


def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_advanced_collectibles)
    )
    write_metadata(number_of_advanced_collectibles, advanced_collectible)


def write_metadata(token_ids, nft_contract):
    for token_id in range(token_ids):
        collectible_metadata = sample_metadata.metadata_template
        typeofasset = get_type(nft_contract.tokenIdToTypeOfAsset(token_id))
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + typeofasset
            + ".json"
        )
        if Path(metadata_file_name).exists():
            print(
                "{} already found, delete it to overwrite!".format(
                    metadata_file_name)
            )
        else:
            print("Creating Metadata file: " + metadata_file_name)
            collectible_metadata["name"] = get_type(
                nft_contract.tokenIdToTypeOfAsset(token_id)
            )
            
            collectible_metadata["geolocation"] = get_geo(
                nft_contract.tokenIdToGeolocation(token_id)
            )
            
            collectible_metadata["type of asset"] = get_type(
                nft_contract.tokenIdToTypeOfAsset(token_id)
            )
            
            collectible_metadata["soil chemical composition"] = get_soil(
                nft_contract.tokenIdToSoil(token_id)
            )
            
            collectible_metadata["main type of trees"] = get_trees(
                nft_contract.tokenIdToTrees(token_id)
            )
            
            collectible_metadata["land riskiness, flood"] = get_flood(
                nft_contract.tokenIdToFloodRisk(token_id)
            )
            
            
            collectible_metadata["land riskiness, fire"] = get_fire(
                nft_contract.tokenIdToFireRisk(token_id)
            )
            
            
            collectible_metadata["land riskiness, drought"] = get_drought(
                nft_contract.tokenIdToDroughtRisk(token_id)
            )
            
            
            collectible_metadata["description"] = "A project of {}".format(
                collectible_metadata["name"]
            )
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(
                    typeofasset.lower().replace('_', '-'))
                image_to_upload = upload_to_ipfs(image_path)
            image_to_upload = (
                breed_to_image_uri[typeofasset] if not image_to_upload else image_to_upload
            )
            collectible_metadata["image"] = image_to_upload
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)

# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = (
            os.getenv("IPFS_URL")
            if os.getenv("IPFS_URL")
            else "http://localhost:5001"
        )
        response = requests.post(ipfs_url + "/api/v0/add",
                                 files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = "ipfs://{}?filename={}".format(
            ipfs_hash, filename)
        print(image_uri)
    return image_uri
