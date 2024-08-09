import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWZYZ"
number = "0123456789"
symbol = "!',-.:;?[]_{}­ʻʼʽ‐‒–—―‖‗‘’‚‛“”†‡․‥…‧‰‱′″‴‵‶‷‸‹›"

all = lower + upper + number + symbol
length = 12
password = "".join(random.sample(all,length))
print("Your generated password is: ",password)