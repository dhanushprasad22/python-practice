x=89
y=903
name="dhanush"
print(x, type(x))
print(name)

#variable scope
#local variable
def order():
    food= "chicken briyani"
    print("the orderd food:",food )

order()

#enclosing variable
def card():
    discount=26
    

    def checkout():
        print("the discount amount is:",discount)
    checkout()    

card()

#global variable
user_id="DHANUSH22"
user_id2="Manasa"
def homepage():
    print("welcome player:",user_id)
def playername():
    print("the avilavble player right now is:",user_id2) 
homepage()
playername()    

#Built inn variables
print(__file__)





      