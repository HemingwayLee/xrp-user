from xrpl.account import get_balance
from xrpl.clients import JsonRpcClient
from xrpl.models import Payment, Tx
from xrpl.transaction import submit_and_wait
from xrpl.wallet import generate_faucet_wallet

# Create a client to connect to the test network
client = JsonRpcClient("https://s2.ripple.com:51234/")

print("Balances of wallets before Payment tx")
print(get_balance("rQDKjHYX8tytLNJYY1rkVeqDqRFP1Mxaae", client))



