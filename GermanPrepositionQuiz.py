import random
import time

#I have a working function for riddles where i only need to pass the keys and values as arguments!
def riddle(key, value):
  attempt = input("What preposition goes with: %s  ?\n>>>" % (key)) 
  while attempt != value:
    print("Wrong! Try again.(or press s to skip)")
    attempt = input("What's the answer? : ")
    if attempt == "s":
      print("okay, fine, but FYI, the preposition for %s is >>>%s" %(key, value))
      time.sleep(1)
      attempt = value
    else: 
      print("Good Job! Advance to the next round!")

#### This Master List can be filled with any items you wish to quiz the user on ####################
masterlist = [['achten','auf'],['fragen','nach'],['denken','an'],['sich bewerben','um'],['bitten','um'],['abhängen','von'],['gehören','zu']]

mixed = random.sample(masterlist, len(masterlist))

for i in range(len(mixed)):
  riddle(mixed[i][0],mixed[i][1])
