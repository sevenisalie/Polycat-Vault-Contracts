from brownie import *
import os

#---------------------------------------------------------
# Function:  deploy
#
# Description:
#   Deploy contract for a Sushiswap lp token.
#
# Parameters:
#   _VaultChef - VaultChef contract address
#   _pid - Vault pool ID
#   _wantAddr - Want lp token address
#   _token0 - Token 0 address
#   _token1 - Token 1 address
#   _dev - Deploy address
#---------------------------------------------------------
def deploy(_VaultChef, _pid, _wantAddr, _dev):
    VaultChef = _VaultChef
    pid = _pid
    wantAddr = _wantAddr
    token0 = interface.IUniPair(wantAddr).token0()
    token1 = interface.IUniPair(wantAddr).token1()
    dev = _dev
    

    QuickswapRouter = '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff'
    USDC = '0x2791bca1f2de4661ed88a30c99a7a9449aa84174'
    QUICK = '0x831753dd7087cac61ab5644b308642cc1c33dc13'
    FISH = '0x3a3df212b7aa91aa0402b9035b098891d276572b'
    WMATIC = '0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270'
    SUSHI = '0x0b3f868e0be5597d5db7feb59e1cadbb0fdda50a'

    StrategySushiSwap.deploy(
        VaultChef,          # Vault Chef address
        pid,                # Pool ID
        wantAddr,           # Want lp token address
        SUSHI,              # Earned address (SUSHI)
        [SUSHI, WMATIC],    # SUSHI -> WMATIC
        [SUSHI, USDC],      # SUSHI -> USDC
        [SUSHI, FISH],      # SUSHI -> FISH
        [WMATIC, USDC],     # WMATIC -> USDC
        [WMATIC, FISH],     # WMATIC -> FISH
        [SUSHI, token0],    # SUSHI -> Token 0
        [SUSHI, token1],    # SUSHI -> Token 1
        [WMATIC, token0],   # WMATIC -> Token 0
        [WMATIC, token1],   # WMATIC -> Token 1
        [token0, SUSHI],    # Token 0 -> SUSHI
        [token1, SUSHI],    # Token 1 -> SUSHI
        {'from': dev}       # Deploying address
    )


def deployTest(_VaultChef, _pid, _wantAddr):
    VaultChef = _VaultChef
    pid = _pid
    wantAddr = _wantAddr
    token0 = interface.IUniPair(wantAddr).token0()
    token1 = interface.IUniPair(wantAddr).token1()

    forkeddev = accounts.at('0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE', force=True)
    

    QuickswapRouter = '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff'
    USDC = '0x2791bca1f2de4661ed88a30c99a7a9449aa84174'
    QUICK = '0x831753dd7087cac61ab5644b308642cc1c33dc13'
    FISH = '0x3a3df212b7aa91aa0402b9035b098891d276572b'
    WMATIC = '0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270'
    SUSHI = '0x0b3f868e0be5597d5db7feb59e1cadbb0fdda50a'

    StrategySushiSwap.deploy(
        VaultChef,          # Vault Chef address
        pid,                # Pool ID
        wantAddr,           # Want lp token address
        SUSHI,              # Earned address (SUSHI)
        [SUSHI, WMATIC],    # SUSHI -> WMATIC
        [SUSHI, USDC],      # SUSHI -> USDC
        [SUSHI, FISH],      # SUSHI -> FISH
        [WMATIC, USDC],     # WMATIC -> USDC
        [WMATIC, FISH],     # WMATIC -> FISH
        [SUSHI, token0],    # SUSHI -> Token 0
        [SUSHI, token1],    # SUSHI -> Token 1
        [WMATIC, token0],   # WMATIC -> Token 0
        [WMATIC, token1],   # WMATIC -> Token 1
        [token0, SUSHI],    # Token 0 -> SUSHI
        [token1, SUSHI],    # Token 1 -> SUSHI
        {'from': dev}       # Deploying address
    )
  

