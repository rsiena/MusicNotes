# -*- coding: utf-8 -*-
# Created by Richard Siena
# you are free to modify and distribute. 
# please reference that it came from me.
# the Notes.correct.txt has sharp and flat unicode characters which python seems to have issues with.
#import codecs
import os
import sys 
#UTF8Writer = codecs.getwriter('utf8')
#sys.stdout = UTF8Writer(sys.stdout)
import random
accidentals = False
helpoption = True
spellaccidentals =False
message = "         Press Enter to continue, H for help!, Q to quit: "
#command line args
flat= "Flat" #"♭".encode('utf-8')
sharp= "Sharp" #"♯".encode('utf-8')

#print(f"Arguments count: {len(sys.argv)}")
l = range(0,len(sys.argv))
for i in l:
    if sys.argv[i] == "-?":
        print("-? for help")
        print("-a for acidentals")
        print("-h for no help ootion")
        print("-s spell acidentals")
        print("q to quit")
        keystroke = input("Press enter to continue")
        exit()
    elif sys.argv[i] == "-a":
        accidentals = True
    elif sys.argv[i] == "-s":
        spellaccidentals = True
    elif sys.argv[i] == "-h":
        helpoption = False
        message = "            Press Enter to continue: "



#open the file
file = open("Notes.txt", "r")
#store the lines from the file in a list
lines = file.readlines()
#shuffle the list
random.shuffle(lines)
#loop through each line in the list
for line in lines:
    #split the line into two parts
    text, help = line.split(",")
    if not accidentals:
        if sharp in text or flat in text:
            continue
    #if spellaccidentals:
    #    if sharp in text:
    #        test = text.replace(sharp, " sharp")
    #    elif flat in text:
    #        test = text.replace(flat, " flat")
    #print the text
    os.system('cls') # this line does not work in the debugger?
    #you may need to change cls to clear for linux
    print("")
    print("")
    print("")
    print("")
    print("            ",text)
    print("")
    print("")
    #wait for user input
    keystroke = input(message)
    if keystroke == 'q' or keystroke == 'Q':
        break
    if keystroke == 'h' or keystroke == 'H':
        #print('\n')
        print("")
        print("")
        print("")
        print("            ",help)
        print("")
        print("")
        input("         Press Enter to continue...")
        #print('\n') 
#close the file
file.close()





