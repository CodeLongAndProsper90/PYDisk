from playsound import playsound as play
from sys import argv
if argv[1] == '0' : play('i.wav')
elif argv[1] == '1' : play('E.wav')
elif argv[1] == '2' : play('ue.wav')
elif argv[1] == '3' : play('Hal.wav')
else: exit()
