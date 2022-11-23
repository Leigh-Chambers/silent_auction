from clear import clear
from art import logo,sold
def next_bid():
  clear()
  print(logo)
next_bid()
print("Welcome to the silent auction, please provide your name and your highest bid.\n\n")
bids = {}
bidding_over = False

while not bidding_over:
  name = input("Please provide your name: \n\n")
  bid = int(input("\n\nPlease enter your highest bid: \n\n£"))
  bids[name] = bid    
  run = input("\n\nAre there any more players? (Y/N)\n\n")
  
  
  if run == 'n':
    bidding_over = True
  else:
    next_bid()
 
highest_bid = max(bids.values())
highest_bidder = (list(bids.keys())[list(bids.values()).index(highest_bid)]) #Go and find out what the list function does and how it makes this work.


clear()
print(sold)
print(f"\n\nCongratulations!!! \033[1m{highest_bidder.upper()}\033[0m has the highest bid with \033[1m£{highest_bid}\033[0m!")
