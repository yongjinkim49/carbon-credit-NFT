from brownie import accounts, config, TokenERC20

initial_supply = 1000000000000000000
token_name = "GREG_CPS"
token_symbol = "CPS"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(initial_supply, token_name, token_symbol, {"from": account})
    print(erc20.address)
    print(erc20.totalSupply())
    print(erc20.decimals())

    