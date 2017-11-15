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
      #### it would be cool to write all the wrong answers onto the study list!!! #####
      ### at the end I could easily divide len(studylist)/len(masterlist) to give the grade!
      time.sleep(1)
      attempt = value
    else: 
      print("Good Job! Advance to the next round!")
  
#note, I don't use umlauts in the preposition field so that it'll be easier for the users to type input. This can easily be changed.

masterlist = [['achten','auf'],['fragen','nach'],['denken','an'],['sich bewerben','um'],['bitten','um'],['abhängen','von'],['gehören','zu'],['es fehlt (D)','an'],['leiden(D)','an'],['es liegt (D)','an'],['sterben','an'],['teilnehmen (D)','an'],['zweifeln(D)','an','[denken(AKK)','an'],['sich errinern (akk)','an'],['sich gewöhnen (+akk)','an'],['glauben (+akk)','an'],['sich wenden(a)(nicht Gegen)','an'],['achten','auf'],['antworten','auf'],['sich freuen (etwas im Futur)','auf'],['hoffen','auf'],['es kommt an','auf'],['sich konzentrieren','auf'],['sich spezialisieren','auf'],['stoßen','auf'],['sich verlassen','auf'],['versichten','auf'],['sich vorbereiten','auf'],['warten','auf'],['bestehen','aus'],['sich bedanken (für)','bei'],['sich beschweren (über)','bei'],['sich entschuldigen (für)','bei'],['sich bedanken(bei)','fur'],['danken(D)','fur'],['eintreten','fur'],['sich entscheiden','fur'],['sich entscheiden (bei)','fur'],['halten(A)','fur'],['sich interessieren','fur'],['kämpfen (aber nicht gegen)','fur'],['sorgen','fur'],['kämpfen (aber nicht für)','gegen'],['protestieren','gegen'],['verstoßen','gegen'],['sich wenden','gegen'],['sich irren (Dat)','in'],['anfangen','mit'],['aufhören','mit'],['sich befassen','mit'],['beginnen','mit'],['sich beschäftigen','mit'],['handeln','mit'],['vergleichen(A)','mit'],['verwechseln (A)','mit'],['zusammenstoßen','mit'],['sich erkundigen','nach'],['fragen (A)','nach'],['sich ärgern','uber'],['sich aufregen','uber'],['berichten','uber'],['sich beschweren (bei)','uber'],['diskutieren (mit)','uber'],['sich freuen (nicht auf)','uber'],['sich infomieren','uber'],['klagen','uber'],['lachen','uber'],['nachdenken','uber'],['sprechen (mit)','uber'],['sich unterhalten','uber'],['sich wundern','uber'],['sich bemühen','um'],['sich bewerben','um'],['bitten (A)','um'],['es geht','um'],['es handelt sich','um'],['sich sorgen','um'],['trauern','um'],['leiden','unter'],['abhängen','von'],['sich trennen','von'],['sich interscheiden','von'],['sich verabschieden','von'],['fliehen','vor'],['sich fürchten','vor'],['schützen A','vor'],['warnen A','vor'],['sich entschließen','zu'],['gehören','zu'],['gratulieren(D)','zu'],['überreden A','zu']]

mixed = random.sample(masterlist, len(masterlist))

#([['achten','auf'],['fragen','nach'],['denken','an'],['sich bewerben','um'],['bitten','um'],['abhängen','von'],['gehören','zu']])

#print(mixed)

for i in range(len(mixed)):
  riddle(mixed[i][0],mixed[i][1])

#for i in range(len(masterlist)):
#  quiz = random.randint(0, len(masterlist))
#  riddle(masterlist[quiz][0],masterlist[quiz][1])
  
  


#i= 0
#for i in range(len(masterlist)):
#    riddle(masterlist[i][0],masterlist[i][1])
#    i = i+1
