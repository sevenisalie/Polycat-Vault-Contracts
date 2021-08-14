from brownie import *
import os


def main():
    WETH = "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    forkeddev = accounts.at('0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE', force=True)
    vaultChefAddress = config["Deployed"]["VaultChef"]
    masterchefAddress = config["Deployed"]["DinoSwapMasterChef"]
    uniRouterAddress = config["Deployed"]["QuickSwapV2Router"]
    pid = config["PoolID"]["DinoSwap"]["USDC_DINO"]
    wantAddress = config["Tokens"]["USDC_DINO_LP"]
    earnedAddress = config["Tokens"]["DINO"]
    WMATIC = config["Tokens"]["WMATIC"]
    USDC = config["Tokens"]["USDC"]
    earnedToWmaticPath = [earnedAddress, WMATIC]
    earnedToToken0Path = [earnedAddress, USDC]
    earnedToToken1Path = [earnedAddress, earnedAddress]
    token0ToEarnedPath = [USDC, earnedAddress]
    token1ToEarnedPath = [earnedAddress, earnedAddress]

    StrategyDinochef.deploy(
        WETH,
        vaultChefAddress,
        masterchefAddress,
        uniRouterAddress,
        pid,
        wantAddress,
        earnedAddress,
        earnedToWmaticPath,
        earnedToToken0Path,
        earnedToToken1Path,
        token0ToEarnedPath,
        token1ToEarnedPath,
        {"from": dev}
    )
