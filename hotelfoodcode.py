name=input("enter ur name:")
phone_no=int(input("enter ur mobile number:"))


menu ={
    1.:"DOSA",
    2.:"PONGAL",
    3.:"IDILY"
}

def show_menu():
    print(f"welcome to the canten {name}")
    print(menu)
    for key, value in menu.items():
        print(f"{key},{value}")

while True:
    show_menu()
    choice=int(input("enter the number of food:"))

    if choice<=4:
        break
    else:
        print(f"your orderd has been succfuclly placed{name}")


