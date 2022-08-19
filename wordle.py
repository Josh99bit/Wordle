# import random
# from colorama import Back, Style

# allowedWords=open("./wordle-allowed-guesses.txt")
# answersWords=open("./wordle-answers-alphabetical.txt")
# answersList=[n.rstrip() for n in answersWords.readlines()]
# allowedList=[n.rstrip() for n in allowedWords.readlines()]
# word=random.choice(answersList).rstrip()
# triesLeft=6
# found=False
# print(word)
# while True:
#     if triesLeft==0:
#         print("OUT OF TRIES")
#         print(Back.GREEN+word)
#         break
#     print(str(triesLeft)+" tries left.")
#     attempt=input().lower()
#     allowed=False
#     if len(attempt)==5:
#         if word in allowedList:
#             allowed=True
#     output=["N"]*5
#     foundLetters=[]
#     if allowed:
#         wordList=[n for n in word]
#         attemptList=[n for n in attempt]
#         for k in range(0,5):
#             if wordList[k]==attemptList[k]:
#                 output[k]="Y"
#                 foundLetters.append(attemptList[k])
#         for k in range(0,5):
#             if attemptList[k] in wordList:
#                 if attemptList[k] not in foundLetters:
#                     if attemptList[k] != "Y":
#                         output[k]="C"
#         if output==["Y"]*5:
#             found=True
#         string=""
#         for n,k in enumerate(output):
#             if k=="N":
#                 string=string+str(Back.RED+attempt[n])
#             elif k=="Y":
#                 string=string+str(Back.GREEN+attempt[n])
#             elif k=="C":
#                 string=string+str(Back.YELLOW+attempt[n])
#         print(string+Style.RESET_ALL)
#         triesLeft-=1
            
#     else:
#         print("INVALID INPUT")

#     if found:
#         break

 