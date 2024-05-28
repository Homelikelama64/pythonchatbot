import os

backMessage = "To go back Press anything"

def clear():
    os.system('cls')
#                   Option 2

def computerArchitecture():
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
    print("Bitshifting is when you shift the bits in a binary number. say you got 01100(12) if you bitshift it 1 to the right it becomes 00110(6), shifting it to the left you get 11000(24). Notice that when you bitshift you ether double or half the value. using this we can use this to multiply using the shift and add method.")
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

Thats the basics of binary
	For what bitshifting is Press 1
	For what the AND operator is press 2
	For how to multiply two numbers press 3
	For LSB press 4
	To go back press 5""")
    option = input()
    if option == "1":
        bitshifting()
    elif option == "2":
        andoperator()
    elif option == "3":
        multiplication()
    elif option == "4":
        lsb()
    elif option == "5":
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
    print("""
Intro: What do you want to Learn About

Press 1 for : How Binary works and various binary operations

Press 2 for : For the two types of Computer Architure(CISC,RISC)

Press 3 for : Going About Creating Your Own CPU""")
    option = input()
    if option == "1":
        binarybaiscs()
    elif option == "2":
        computerArchitecture()
    else:
        clear()
        print("Not an Option")
        print(backMessage)
        pause = input()
        intro()
intro()
