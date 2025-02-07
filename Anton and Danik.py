num1=int(input("Enter the number of game:"))
txt1=input('Enter the Game Won sequancen as A or B:').lower()

if len(txt1)==num1:
    countedtxtA=txt1.count('a')
    countedtxtB=txt1.count('d')
    if countedtxtA>countedtxtB:
        print("Anton")
    elif countedtxtA<countedtxtB:
        print('Danik')
    else:
        print('Friendship')
else:
    print('The Amount of the game and letter must be the same.')


