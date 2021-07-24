# Polycat-Vault-Contracts

PolyCat Vault Contracts Readme

These are the official polycat finance vault contracts forked from https://github.com/polycatfi

These contracts are written in solidity version ^0.6.0 and compiled/deployed using brownie.  Brownie is the python world’s Truffle. https://eth-brownie.readthedocs.io/en/stable/install.html

Install the dependencies
``` 
pip install eth-brownie
``` 

While inside main directory Polycat-Vault-Contracts, compile the contracts with
``` 
brownie compile
``` 

Add a new network (matic) to brownie networks config
``` 
brownie networks add matic matic-mainnet host=https://rpc-mainnet.maticvigil.com/v1/4b331c188697971af1cd6f05bb7065bc358b7e89 chainid=137 explorer=https://polygonscan.com/
``` 

store your key in an environment variable (use a throwaway wallet when testing).  By storing it in an env variable and calling it with os.getenv() in python, we are able to prevent exposing our private key in our code.
``` 
export PRIVATE_KEY=0xsdoi485jfoq3409t834p3n9jy4tf834iweqior234809
``` 

To deploy to mainnet run
``` 
brownie run scripts/deploy.py --network matic-mainnet
``` 

TODO:
Recreate mocks/mumbai addresses in QuickSwapStrategy.sol for testnet deployment
