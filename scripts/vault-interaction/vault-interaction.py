from brownie import *
import os

VaultChefAddr = '0xFfAD7ef599B22674D141b24285D81246D82f283c'

def loadStrategy(_strategy):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    return Contract.from_abi("MCS", _strategy, StrategyShortDinochef.abi)

def loadVault(_vaultchef):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    return Contract.from_abi("Vault", _vaultchef, VaultChef.abi)

#only need to approve once per asset with the below approval pattern. _asset is address of wantToken
def approveVault(_asset, _vaultchef):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    asset = interface.IERC20(_asset)
    vaultchef = loadVault(_vaultchef)
    tx1 = asset.approve(vaultchef.address, (2**256 - 1), {"from": dev})
    return tx1


#this takes the address of the newly deployed strategy
def addPool(_strategy, _vaultchef):
    myaccount = accounts.add(os.getenv("PRIVATE_KEY"))
    dev = accounts.at(myaccount)
    vaultchef = loadVault(_vaultchef)
    tx = vaultchef.addPool(_strategy, {'from': dev})
    return tx

#run this every time you deploy a new strat
def resetPoolAllowances(_strategy):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    strategy = loadStrategy(_strategy)
    tx = strategy.resetAllowances({"from": dev})
    return tx


def deposit(_vaultchef, pid, amount):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    vaultchef = loadVault(_vaultchef)
    tx = vaultchef.deposit(pid, amount, {'from': dev})
    return tx


def withdraw(_vaultchef, pid, amount):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    vaultchef = loadVault(_vaultchef)
    tx = vaultchef.withdraw(pid, amount, {'from': dev,  "gas_price": 5000000000, "gas_limit": 500000, "allow_revert": True})
    return tx


def earn(_strategy):
    dev = accounts.add(os.getenv("PRIVATE_KEY"))
    strategy = loadStrategy(_strategy)
    tx = strategy.earn({"from": dev, "gas_price": 15000000000, "gas_limit": 500000, "allow_revert": True})
    return tx

