from brownie import *
import os

#VaultChefAddr = '0xFfAD7ef599B22674D141b24285D81246D82f283c' disregard this for now.


def addPool(_strategy):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))

    tx = VaultChef[0].addPool(_strategy, {'from': dev})
    return tx


def addPoolTest():
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    forkeddev = accounts.at('0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE', force=True)
    tx = VaultChef[0].addPool(config["deployed"]["StrategyMainnetFork"], {"from": forkeddev})
    return tx

def withdraw():
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    _pid = 0
    _amount = 200000 #wei
    tx = VaultChef[0].withdraw(_pid, _amount, {"from": dev})
    return tx

def earn(_pid):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    tx = StrategyMasterchef[_pid].earn({"from": dev})
    return tx

