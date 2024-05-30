import os
from random import *

backMessage = "To go back Press anything"

N1 = "1"
N2 = "2"
N3 = "3"
N4 = "4"
N5 = "5"
N6 = "6"
N7 = "7"
N8 = "8"
N9 = "9"

def clear():
    os.system('cls')
#                   Option 3

def secret1():
    clear()
    print("Nothings here")
    option = input()
    if option == "Secret":
        secret2()
    intro()

def secret2():
    clear()
    print("No seriously theres nothing here")
    option = input()
    if option == "Secret":
        secret3()
    intro()
    
def secret3():
    clear()
    print("ok, maybe theres something")
    option = input()
    if option == "Secret":
        secret4()
    intro()

def secret4():
    clear()
    print("I lied there is nothing")
    option = input()
    if option == "Secret":
        secret5()
    intro()

def secret5():
    clear()
    print("Ok you have some dedication")
    option = input()
    if option == "Secret":
        secret6()
    intro()


def secret6():
    clear()
    print("Nothings here")
    option = input()
    if option == "Secret":
        secret7()
    intro()

def secret7():
    clear()
    print("No seriously theres nothing here")
    option = input()
    if option == "Secret":
        secret8()
    intro()
    
def secret8():
    clear()
    print("ok, maybe theres something")
    option = input()
    if option == "Secret":
        secret9()
    intro()

def secret9():
    clear()
    print("I lied there is nothing")
    option = input()
    if option == "Secret":
        secret10()
    intro()

def secret10():
    clear()
    print("Wow You Have ALOT of dedication")
    option = input()
    if option == "Secret":
        secret6()
    intro()

def secret11():
    clear()
    print("""Fine i give up heres the secret Ok heres the secret:
^ ^
| |
___/""")
    option = input()
    if option == """^ ^
| |
___/""":
        secret12()
    intro()

def secret12():
    clear()
    print("""Ok Hears the Real Secret:
Potatoe""")
    option = input()
    if option == "Secret":
        intro()
    intro()

def registers():
    clear()
    print("""
Registers are temporary data storage that the instructions; set, modify and move around""")
    print(backMessage)
    pause = input()
    computer_instructions()

def ram():
    clear()
    print("""
How a genral instruction would look like for 8bit ram and 16bit registers is the first 3 bits would be used to
say what register the following data should be inputed into. The remaining 5bits will be used for declearing what instruction it is. 
The following ram will be the instructions for the intruction. Here is an example for the const instruction putting 5 into register 1:
00001001 00000000 00000101
since its a 16bit number but we have 8bit ram for const we need to use three ram adresses for a const instruction. 
You do not need to do it this way this is a way I have found to do instructions in a clean way""")
    print(backMessage)
    pause = input()
    computer_instructions()

def computer_instructions():
    clear()
    print("""
To start building a cpu first we have to understand what instructions we need for this computer to be 
turing complete(can create its self)

first im going to create the ALU
	The ALU will read from 1 register at a time and store it in its own cach

it will have 5 intstructions
	ADD
	SUB(Ran out of time to explain)
	MULT

we have 9 instructions
	Const(load data into one register)

	ADD(adds two registers)

	SUB(subtacts two registers)

	MULT(multiplys two registers)

	Copy(copys the data from oen register to another)

	Conditional copy(copys the data from oen register to
	another if another register is ether: zero, non
	zero,positive or negative)
	
	Jump(Moves the instruction point(where the
	computere is reading from ram)

	Load(loads some ram at the address of a register into
	a register)

	Store(Stores a register to ram at the adress of another 	register)

How the Load and Store functions is dependant on wether you have the Von Neumann or the Harvard architecture

When i was creating my own CPU in Logic World(logic simulating game) I Chose to go with the Von Nuemann
archietecture. Instead of having a dedicated instruction pointer i just dedicated register 7 to the instruction pointer.

Press 1 for what Registers are
          
Press 2 for what does the ram instructions look like in ram
          
Press 3 to return""")
    option = input()
    if option == N1:
        registers()
    elif option == N2:
        ram()
    elif option == N3:
        intro()
    else:
        clear()
        print("Not an Option")
        print(backMessage)
        pause = input()
        computer_instructions()

#                   Option 2

def computerArchitecture():
    clear()
    print("""
There are two types of computer architecture the Von Neumann and the Harvard architecture. 
The Von Nuemann archietecture has the instructions with the data
 storage while the Harvard architecture has them seperate.

Von Nuemann Architecture

                ALU(Math/Data manipulation)
                            |
                            |
Instructions/data  <--> Controll  ---------> out
                        unit(with registers)
                    	    |
                            In

Harvard Architecture

				ALU( Math/Data manipulation)
                      |
                      |
Instructions <------> Controll <---------->  Data
                    Unit(with registers)
                      |
                      |
                      |
                    In / out""")
    print(backMessage)
    pause = input()
    intro()

#                   Option 1


#addition
def addition():
    clear()
    print("""
To Explain how to add two numbers in binary lets take the simplest method
any number plus 1, or counting. for one bit to turn on all prevous bits have to be on when the counter is pulsed. here is an example.
  0001(3)(a)
+0011(b)
---------
	1
 0011

  1
0010
  
0100

------
=0100(4)

here is some sudo code :

add = lambda x, y: x if y == 0 else add(x^y, (x&y) << 1)

}""")
    print(backMessage)
    pause = input()
    binarybaiscs()


# Least signifgant bit
def lsb():
    clear()
    print("""
    LSB is the least significant bit in a binary number
	press 1 to go back""")
    print(backMessage)
    pause = input()
    binarybaiscs()

# binary multiplicaton
def multiplication():
    clear()
    print("""
Multiplication is trivial in binary
using the shift and add method
    110001
      1101
    ------
  00110001
  01100010
  11000100
 ----------
 1001111101

Here is a Diagram For Unsigned multiplication
                  Start
                    |
               Initialise
             M <- Multicand
             Q <- Multiplier
             C <- O,A <- 0000
             n <- no 4 bits
                    |--------------------
            =  1    Q                   |
      A <- A + M---LSB	                 |
      |             | = 0               |
      |-------------|                   |
               Shift Right              |
                  N - 1                 |
                   |     != 0           |
                   n--------------------|
                   | = 0
               Result is
                 In AQ
                   |
                 Stop""")
    print(backMessage)
    pause = input()
    binarybaiscs()

# Bit Sifting
def bitshifting():
    clear()
    print("""Bitshifting is when you shift the bits in a binary number.
say you got 01100(12) if you bitshift it 1 to the right it becomes 00110(6), shifting it to the left you get 11000(24).
Notice that when you bitshift you ether double or half the value. using this we can use this to multiply using the shift and add method.""")
    print(backMessage)
    pause = input()
    binarybaiscs()

# AND binary operator
def andoperator():
    clear()
    print("The And operator compares to numbers and gives a new number witch only has the bits that are on for both e.g.\n   1101110\n& 0110010\nwill give you 0100010.")
    print(backMessage)
    pause = input()
    binarybaiscs()


#The basics of binary
def binarybaiscs():
    clear()
    print("""
The usual number system that you use for english base 10 but computers use base 2(Binary) so all data is represented by on and off. 
For this I will represent 1 as on and 0 as off. 
Ten is represented like this 10 in base 10 but in base 2(Binary) Ten is represented as 1010. To covert base 2 to base 10. you multiply the digits like this
(8*1)+(4*0)+(2*1)+(1*0)
=(8*1)+(2*1)
=8+2
=10.
every Digit in base 2 is 2 times the amout as the last digit. The formula would be(starting at 0) 2^d to get how much that digit contributes in base 10.

Thats the basics of binary""")
    print(" For what bitshifting is Press " + N1)
    print(" For what the AND operator is press " + N2)
    print(" For how to add press " + N3)
    print(" For how to multiply two numbers press " + N4)
    print(" For LSB press " + N5)
    print(" To go back press " + N6)
    option = input()
    if option == N1:
        bitshifting()
    elif option == N2:
        andoperator()
    elif option == N3:
        addition()
    elif option == N4:
        multiplication()
    elif option == N5:
        lsb()
    elif option == N6:
        intro()
    else:
        clear()
        print("Not an Option")
        print(backMessage)
        pause = input()
        binarybaiscs()

#               START

#intro
def intro():
    clear()
    print("Intro: What do you want to Learn About")

    print("\nPress "+ N1 + " for : How Binary works and various binary operations")

    print("\nPress "+ N2 +" for : For the two types of Computer Architure(Von Nuemann,Harvard Architecture)")

    print("\nPress "+ N3 +" for : Final Info need for Creating Your Own CPU")
    option = input()
    if option == N1:
        binarybaiscs()
    elif option == N2:
        computerArchitecture()
    elif option == N3:
        computer_instructions()
    elif option == "Secret":
        secret1()
    else:
        clear()
        print("Not an Option")
        print(backMessage)
        pause = input()
        intro()
intro()
