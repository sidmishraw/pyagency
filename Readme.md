## Agent Based Architecture Framework
### Agency Platform
[Based on Dr. Pearce's lecture](http://www.cs.sjsu.edu/faculty/pearce/modules/projects/oop/agency/index.htm)

### Motivation
Try and implement the [agency platform](https://github.com/sidmishraw/agency_platform) implemented in Java8 in python and compare 
the ease of programming and design changes etc.

All in all, I'm doing this just for fun!

### The Agent-based Architecture
The Agency is a platform for creating and running agent-based applications. 
It consists of three components: Facilitator, Agent, and Message.

A typical customization would create extensions of all three classes.

#### Facilitator
The facilitator maintains a list of all agents. Agents are added to the list using the add method. This method provides 
an agent with a reference to the facilitator and a unique id number. The facilitator provides synchronized services 
for delivering messages and for finding partners. The facilitator's start method runs 
in two modes: multi-threaded and single-threaded. In multi-threaded mode each agent is started, then joined. 
In single-threaded mode the facilitator repeatedly iterates through the agents, calling each 
ones update method until all of the agents are dead.

#### Agent
The Agent update method is abstract. It must be implemented in an extension. 
Usually the update method doesn't try to do too much: request a partner from the facilitator, 
send a message to a partner, check for incoming messages, etc. (Be careful, most Agent methods need to be synchronized.)

#### Message
The message is just a generic wrapper containing contents.


### Examples:

* [Voting Patterns](http://www.cs.sjsu.edu/faculty/pearce/modules/projects/oop/agency/index.htm)

    A precinct is an NxN grid of voter agents. A voter has a randomly assigned party affiliation (Republican or Democrat) and an address (i.e., its row and column in the precinct). A voter, V, updates itself by asking each of its 3, 5, or 8 neighbors in the precinct what their party affiliation is. If a majority have a different party, the V switches to that party. A settable precinct flag determines what to do in the case of a tie.
    
    Implement precincts and voters as a customization of the agency platform. Display the grid at the beginning of the run as a 2-dimensional array of Rs and Ds. Run the simulation for M cycles (try M = 100). Then display the grid again. What changes do you see? Does this explain the red-state/blue-state phenomenon?
    
    
    
##### Note: This project uses CPython 3.6.1, not tested or developed with other versions in mind 