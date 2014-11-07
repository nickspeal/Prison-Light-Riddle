Prison-Light-Riddle
===================

A quick python script to simulate the scenario described in a riddle

One afternoon I was on vacation with a few friends, and Joe told us all a fun little riddle. After we eventually solved the riddle, I was fascinated by its algorithmic solution and decided to code up a simulation of the situation.

## The Riddle

Here is a version of the riddle, as told by this website: http://www.cut-the-knot.org/Probability/LightBulbs.shtml


There are 100 prisoners in solitary cells. There's a central living room with one light bulb; this bulb is initially off. No prisoner can see the light bulb from his or her own cell. Everyday, the warden picks a prisoner equally at random, and that prisoner visits the living room. While there,the prisoner can toggle the bulb if he or she wishes. Also, the prisoner has the option of asserting that all 100 prisoners have been to the living room by now. If this assertion is false, all 100 prisoners are shot. However, if it is indeed true, all prisoners are set free and inducted into MENSA, since the world could always use more smart people. Thus, the assertion should only be made if the prisoner is 100% certain of its validity. The prisoners are allowed to get together one night in the courtyard, to discuss a plan. What plan should they agree on, so that eventually, someone will make a correct assertion?

## The Solution

In their one meeting, the group elects a leader who keeps count. Everybody else must walk into the living room following the same rule:
* Never turn the lightswitch off
* If the light switch is off and you have never turned it on before, turn it on.
* If the light switch is off and you have turned it on before, leave it off.

The leader is the only person who can turn it off. Each time they turn off the lightswitch, they increase a mental counter. Once they have turned off the light switch 99 times, they are 100% certain that everybody has been in the room at least once.

Of course, many of the prisoners will have entered the room many times, and this simulation represents an effort to explore the statistics of the situation.

## Authorship

This program was written by Nick Speal in Puerto Plata, Dominican Rebublic on Feb 23, 2012
