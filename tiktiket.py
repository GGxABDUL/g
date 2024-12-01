#Process bertindak atau bertindak
#Procedure Pengenalan
def kenal():
    print("- Selamat datang ke TGV Cinemas!   -")
    print("- Kami sedia berkhidmat untuk anda -")


def menu():
    x = str(input('Tekan "y" untuk teruskan, "n" untuk batal\n'))
    if x == "y":
        print("oo")
    elif x == "n":
        process = False
        print("kk")
    else:
        print("ong")
kenal()
menu()

while process == True:
    kenal()
    menu()
