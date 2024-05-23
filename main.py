backMessage = "To go back Press anything"

def lsb():
    print("""
    LSB is the least significant bit in a binary number
	press 1 to go back
	press 2 to go back to the start""")
    print(backMessage)
    option = input()
    if option:
        binarybaiscs()


def multiplication():
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
            Shift Righ               |
               N - 1                 |
                |     != 0           |
                n--------------------|
                | = 0
            Result is
              In AQ
                |
              Stop""")
    print(backMessage)
    option = input()
    if option:
        binarybaiscs()


def bitshifting():
    print("Bitshifting is when you shift the bits in a binary number. say you got 01100(12) if you bitshift it 1 to the right it becomes 00110(6), shifting it to the left you get 11000(24). Notice that when you bitshift you ether double or half the value. using this we can use this to multiply using the shift and add method.")
    print(backMessage)
    option = input()
    if option:
        binarybaiscs()

def andoperator():
    print("The And operator compares to numbers and gives a new number witch only has the bits that are on for both e.g.\n   1101110\n& 0110010\nwill give you 0100010.")
    print(backMessage)
    option = input()
    if option:
        binarybaiscs()

def binarybaiscs():
    print("The usual number system that you use for english base 10 but computers use base 2(Binary) so all data is represented by on and off. For this I will represent 1           as on and 0 as off. Ten is represented like this 10 in base 10 but in base 2(Binary) Ten is represented as 1010. To covert base 2 to base 10. you multiply the digits like this\n(8*1)+(4*0)+(2*1)+(1*0)\n=(8*1)+(2*1)\n=8+2\n=10.\nevery Digit in base 2 is 2 times the amout as the last digit. the formula would be(starting at 0) 2^d to get how much that digit contributes in base 10.\nThats the basics of binary\nFor what bitshifting is Press 1\nFor what the AND operator is press 2\nFor how to multiply two numbers press 3\nFor LSB press 4\nTo go back press 5")
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
        option = input()
        print("Not an Option")
        print(backMessage)
        if option:
            binarybaiscs()

def intro():
    print("Intro: What do you want to Learn About\nPress 1 for : How Binary works and various binary operations\nPress 2 for : For the two types of Computer Architure(CISC,RISC)\nPress 3 for : Going About Creating Your Own CPU")
    option = input()
    if option == "1":
        binarybaiscs()



intro()