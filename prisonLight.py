#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
	This code was written to simulate a scenario described in a riddle:
	
	
	There are 100 prisoners in solitary cells. 
	There's a central living room with one light bulb; 
	this bulb is initially off. No prisoner can see the 
	light bulb from his or her own cell. 
	Everyday, the warden picks a prisoner equally at random, 
	and that prisoner visits the living room. While there,
	the prisoner can toggle the bulb if he or she wishes. 
	Also, the prisoner has the option of asserting that all 100 prisoners 
	have been to the living room by now. If this assertion is false, 
	all 100 prisoners are shot. However, if it is indeed true, 
	all prisoners are set free and inducted into MENSA, 
	since the world could always use more smart people.
	Thus, the assertion should only be made if the
	prisoner is 100% certain of its validity. 
	The prisoners are allowed to get together 
	one night in the courtyard, to discuss a plan. 
	What plan should they agree on, so that eventually, 
	someone will make a correct assertion?
	<http://www.cut-the-knot.org/Probability/LightBulbs.shtml>
	
	Written by Nick Speal in Puerto Plata, Dominican Rebublic on Feb 23, 2012.						      
	Nick can be contacted at nick@speal.ca
"""




import random
import os	#for clear

#parameters:
numberOfPrisoners = 100	
lightPosition = False
guessAttempted = False
keepGoing = True

leaderID = 0	
countVisits = 0
maxNumberOfVisits = 10
totalNumberOfVisits = 0		#overwritten later before while loop
person = 0	#global idNumber



#arrays:
numberOfVisits = [0]*numberOfPrisoners
numberOfFlicks = [0]*numberOfPrisoners


#Functions

def visit(idNumber):
	global lightPosition
	global countVisits
	
	numberOfVisits[idNumber] += 1

	if idNumber != leaderID:
		
		if numberOfFlicks[idNumber] > 0:
			#leave the room
			pass
		elif numberOfFlicks[idNumber] == 0:
			if lightPosition == True:
				#leave the room
				pass
			else:	#if lightPosition == False
				#turn on the light
				lightPosition = True
				numberOfFlicks[idNumber] +=1
			
			
	else:	#if idNumber == leaderID
		if lightPosition == True:
			#turn the light off and augment the count
			lightPosition = False
			countVisits += 1
			numberOfFlicks[leaderID] += 1
			
		else: #if lightPosition == False
			#leave the room	
			pass

def outputResults():
	
	os.system('clear')
	print "SIMULATION COMPLETE"
	print "-------------------"
	print "The room was entered %g times." %totalNumberOfVisits
	print "At 1 person per day, this would take %f years!" %(totalNumberOfVisits/365.25)
	if guessAttempted == True:
		print "The leader thinks that everybody has been in the room."
	else:	#guessAttempted == False:
		print "The leader can only be sure that %g distinct people have entered the room" %(countVisits +1)	#+1 to count the leader
	
	#add an output statement that indicates how many distinct
	#people have entered the room, and how many have turned on the light
	#This statement would use the values in the 2 arrays, but would this 
	#be a legit validation??
	
	
	print "The number of times that each person entered the room, and flicked the light are tabulated below."
	print "People who did not enter the room are excluded from the table."
	
	num = 0
	numSkipped = 0
	for (v,f) in zip(numberOfVisits, numberOfFlicks):
		if v != 0:
			print "%3g | %3g | %3g" %(num, v, f)
		else:
			numSkipped +=1
		num +=1
	
	print "%g people never entered the room" %numSkipped



os.system('clear')
print "Welcome to the Prison Riddle Simulator!"
print "---------------------------------------\n"

numberOfPrisoners = int(raw_input('How many prisoners are there?'))
maxNumberOfVisits = int(raw_input('What is the upper limit on the number of visits?'))
if maxNumberOfVisits == 0:
	maxNumberOfVisits =999999

while keepGoing == True and guessAttempted == False:
	while totalNumberOfVisits < maxNumberOfVisits:
		person = random.randint(0,numberOfPrisoners-1)
		visit(person)
		totalNumberOfVisits += 1
		if countVisits == numberOfPrisoners - 1:
			guessAttempted = True
			break
	
	outputResults()
	if not guessAttempted:
		keepGoing = bool(int(raw_input('Keep going?(1/0)')))
	if keepGoing:
		while maxNumberOfVisits <= totalNumberOfVisits:
			maxNumberOfVisits = int(raw_input("What's the max number of visits?"))

print "\n\nThanks for playing!\n\n"
			

