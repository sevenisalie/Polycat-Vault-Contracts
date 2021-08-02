from brownie import *
import os

def main():
    myaccount = accounts.add(os.getenv("PRIVATE_KEY"))
    dev = accounts.at(myaccount)
    Operators.deploy({'from': dev})