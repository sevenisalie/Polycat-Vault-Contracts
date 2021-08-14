from brownie import *
from os

def main():
    WETH = "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    forkeddev = accounts.at('0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE', force=True)
    vaultChefAddress = config["Deployed"]["VaultChef3"]
    masterchefAddress = config["Deployed"]["DinoSwapMasterChef"]
    uniRouterAddress = config["Deployed"]["SushiSwapV2Router"]
    pid = config["PoolID"]["DinoSwap"]["USDC_DINO"]
    wantAddress = config["Tokens"]["USDC_DINO_LP"]
    newWantAddress = config["Tokens"]["MiMATIC"]
    earnedAddress = config["Tokens"]["DINO"]
    WMATIC = config["Tokens"]["WMATIC"]
    USDC = config["Tokens"]["USDC"]
    earnedToWmaticPath = [earnedAddress, WMATIC]
    earnedToNewWantPath = [earnedAddress, newWantAddress]


    StrategyShortDinochef.deploy(
        WETH,
        vaultChefAddress,
        masterchefAddress,
        uniRouterAddress,
        pid,
        wantAddress,
        newWantAddress,
        earnedAddress,
        earnedToWmaticPath,
        earnedToNewWantPath,
        {"from": dev}
    )
    