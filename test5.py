import random
Finish, win1, win2, draw1, draw2, see, seu, easydif, sum, sue, smu,shh, cheat= True, False, False, False, False, False, False, 0, False, False, False,False, False


def CheckX():
    global win1, draw1
    for i in range(0, 9, 3):
        if myList2[i] == "X" and myList2[i+1] == "X" and myList2[i+2] == "X":
            win1 = True
    for i in range(3):
        if myList2[i] == "X" and myList2[i+3] == "X" and myList2[i+6] == "X":
            win1 = True
    if myList2[0] == "X" and myList2[4] == "X" and myList2[8] == "X":
        win1 = True
    elif myList2[2] == "X" and myList2[4] == "X" and myList2[6] == "X":
        win1 = True

    if not win1:
        draw1 = True


def CheckY():
    global win2, draw2
    for i in range(3):
        if myList2[i] == "O" and myList2[i + 3] == "O" and myList2[i + 6] == "O":
            win2 = True
    for i in range(0, 9, 3):
        if myList2[i] == "O" and myList2[i+1] == "O" and myList2[i+2] == "O":
            win2 = True
    if myList2[0] == "O" and myList2[4] == "O" and myList2[8] == "O":
        win2 = True
    elif myList2[2] == "O" and myList2[4] == "O" and myList2[6] == "O":
        win2 = True
    if not win2:
        draw2 = True


def checkSpace():
    global Finish
    for i in range(9):
        if myList2[i] == "X" or "O":
            Finish = True
    for i in range(9):
        if myList2[i] == " ":
            Finish = False


xc, yc = 0, 0


def whichone():
    global xc, yc
    for i in range(9):
        if myList2[i] == "X":
            xc += 1

    for i in range(9):
        if myList2[i] == "O":
            yc += 1


xoo, wrong, pez = False, False, True


def check(x, y, index):
    global wrong, easydif, pez
    if x > 3 or y > 3:
        print("Coordinates should be from 1 to 3!")
        wrong = True
    elif myList2[index] == "x" or "X" and myList2[index] != "_" and myList2[index] != " ":
        print("This cell is occupied! Choose another one!1")
        if pez:
            print("This cell is occupied! Choose another one!")
        wrong = True
    elif myList2[index] == "o" or "O" and myList2[index] != "_" and myList2[index] != " ":
        print("This cell is occupied! Choose another one!2")
        if pez:
            print("This cell is occupied! Choose another one!")
        wrong = True
    else:
        wrong = False

def easy():
    global pez, easydif,wrong,draw1,draw2
    pez = False
    while wrong == True:
        easydif = random.randrange(9)
        pez = False
        check(2, 2, easydif)
        pez = True
index = 0

def checkindex(index1):
    global index
    index1 = index
    if index1 == 6 or index1 == 7 or index1 == 8:
        index = index1 - 6
    elif index == 0 or index == 1 or index == 2:
        index = index1 + 6

def playerpick():
    global xoo, index
    while True and not xoo:
        try:
            y, x = input("Enter the coordinates: ").split()
            x = int(x)
            y = int(y)
            break
        except ValueError:
            print("You should enter numbers!")

    index = (x - 1) + (9 - (3 * y))
    checkindex(index)
    check(x, y, index)



myList = " "*9
myList2 = [myList[0], myList[1], myList[2], myList[3], myList[4], myList[5], myList[6], myList[7],
            myList[8]]



def AskXorY():
    global see, seu, wrong, myList2, xoo, easydif, myList,shh
    myList = " "*9
    myList2 = [myList[0], myList[1], myList[2], myList[3], myList[4], myList[5], myList[6], myList[7],
            myList[8]]

    while True:
        if sue == True:
            UserVsEasy()
        elif see == True:
            easyVseasy()
        elif sum == True:
            UserVsMedium()
        elif shh == True:
            mediumVsmedium()
        if wrong == False:
            print("---------")
            for i in range(0, 9, 3):
                print("|" + " " + myList2[i] + " " + myList2[i+1] +   " " + myList2[i+2] + " " + "|")
            print("---------")
            CheckX()
            CheckY()
            checkSpace()
            if win1:
                print("X wins")
                resetValor()
                break
            elif win2:
                print("O wins")
                resetValor()
                break
            elif draw1 and draw2 and Finish:
                print("Draw")
                resetValor()
                break


def UserVsEasy():
    global xoo, wrong
    if not xoo:
        playerpick()
        if wrong == False:
            myList2[index] = "X"
            xoo = True
    else:
        if wrong == False:
            wrong = True
            easy()
            print('Making move level "easy"')
            print("JODERQIJOGIOekhgp")
            myList2[easydif] = "O"
            xoo = False

O = ""
X = ""
def UserVsMedium():
    global xoo, wrong, smu, sum, pez,index,O,X
    O, X = "O", "X"
    if smu == True:
        O, X = "X", "O"
    if not xoo:
        playerpick()
        if wrong == False:
            myList2[index] = X
            xoo = True
    else:
        medium()

def medium():
    global O,X,xoo,pez,myList2,manuel,wrong
    manuel = False
    if wrong == False:
        for i in range(0, 9, 3):
                if myList2[i] == X and myList2[i+2] == X and myList2[i+1] != "X" and myList2[i+1] != "O":
                    myList2[i+1] = O
                    pez = True
                    manuel = True
                    break
                elif myList2[i] == X and myList2[i+1] == X and myList2[i+2] != "X" and myList2[i+2] != "O":
                    myList2[i+2] = O
                    pez = True
                    manuel = True
                    break
                elif myList2[i+1] == X and myList2[i+2] == X and myList2[i] != "X" and myList2[i] != "O":
                    myList2[i] = O
                    pez = True
                    manuel = True
                    break 
    if manuel:
                xoo = False
                print('Making move level "medium"')
                return
    for i in range(3):
                if myList2[i] == X and myList2[i+3] == X and myList2[i+6] != "X" and myList2[i+6] != "O":
                    myList2[i+6] = O
                    pez = True
                    manuel = True      
                elif myList2[i] == X and myList2[i+6] == X and myList2[i+3] != "X" and myList2[i+3] != "O":
                    myList2[i+3] = O
                    pez = True
                    manuel = True          
                elif myList2[i+3] == X and myList2[i+6] == X and myList2[i] != "X" and myList2[i] != "O":
                    myList2[i] = O
                    pez = True
                    manuel = True
    if manuel:
                xoo = False
                print('Making move level "medium"')
                return 

    if myList2[0] == X and myList2[4] == X and myList2[8] != "X" and myList2[8] != "O":
                myList2[8] = O
                pez = True
                manuel = True                      
    elif myList2[0] == X and myList2[8] == X and myList2[4] != "X" and myList2[4] != "O":
                myList2[4] = O
                pez = True
                manuel = True  
    elif myList2[4] == X and myList2[8] == X and myList2[0] != "X" and myList2[0] != "O":
                myList2[0] = O
                pez = True
                manuel = True  

    if manuel:
                xoo = False
                print('Making move level "medium"')
                return 

    if myList2[2] == X and myList2[4] == X and myList2[6] != "X" and myList2[6] != "O":
                myList2[6] = O
                pez = True
                manuel = True                      
    elif myList2[2] == X and myList2[6] == X and myList2[4] != "X" and myList2[4] != "O":
                myList2[4] = O
                pez = True
                manuel = True  
    elif myList2[4] == X and myList2[6] == X and myList2[2] != "X" and myList2[2] != "O":
                myList2[2] = O
                pez = True
                manuel = True  

    if manuel:
                xoo = False
                print('Making move level "medium"')
                return                
#------------------------------------O-------O------------------------------------------------------------------------------
    for i in range(0, 9, 3):
                if myList2[i] == O and myList2[i+2] == O and myList2[i+1] != "X" and myList2[i+1] != "O":
                    myList2[i+1] = O
                    pez = True
                    manuel = True 
                    break
                elif myList2[i] == O and myList2[i+1] == O and myList2[i+2] != "X" and myList2[i+2] != "O":
                    myList2[i+2] = O
                    pez = True
                    manuel = True
                    break
                elif myList2[i+1] == O and myList2[i+2] == O and myList2[i] != "X" and myList2[i] != "O":
                    myList2[i] = O
                    pez = True
                    manuel = True
                    break 
    if manuel:
                xoo = False
                print('Making move level "medium"')
                return
    for i in range(3):
                if myList2[i] == O and myList2[i+3] == O and myList2[i+6] != "X" and myList2[i+6] != "O":
                    myList2[i+6] = O
                    pez = True
                    manuel = True      
                elif myList2[i] == O and myList2[i+6] == O and myList2[i+3] != "X" and myList2[i+3] != "O":
                    myList2[i+3] = O
                    pez = True
                    manuel = True          
                elif myList2[i+3] == O and myList2[i+6] == O and myList2[i] != "X" and myList2[i] != "O":
                    myList2[i] = O
                    pez = True
                    manuel = True
    if manuel:
                xoo = False
                print('Making move level "medium"')
                return 

    if myList2[0] == O and myList2[4] == O and myList2[8] != "X" and myList2[8] != "O":
                myList2[8] = O
                pez = True
                manuel = True                      
    elif myList2[0] == O and myList2[8] == O and myList2[4] != "X" and myList2[4] != "O":
                myList2[4] = O
                pez = True
                manuel = True  
    elif myList2[4] == O and myList2[8] == O and myList2[0] != "X" and myList2[0] != "O":
                myList2[0] = O
                pez = True
                manuel = True  

    if manuel:
                xoo = False
                print('Making move level "medium"')
                return 

    if myList2[2] == O and myList2[4] == O and myList2[6] != "X" and myList2[6] != "O":
                myList2[6] = O
                pez = True
                manuel = True                      
    elif myList2[2] == O and myList2[6] == O and myList2[4] != "X" and myList2[4] != "O":
                myList2[4] = O
                pez = True
                manuel = True  
    elif myList2[4] == O and myList2[6] == O and myList2[2] != "X" and myList2[2] != "O":
                myList2[2] = O
                pez = True
                manuel = True  

    if manuel:
                xoo = False
                print('Making move level "medium"')
                return 

    wrong = True
    easy()
    myList2[easydif] = O
    print('Making move level "medium"')
    xoo = False

def mediumVsmedium():
    global xoo, wrong, smu, sum, pez,index,O,X,myList2,manuel
    O, X = "O", "X"
    if not xoo:
        O, X = "X", "O"
        if wrong == False:
            medium()
            xoo = True
    else:
        medium()
        xoo = False


def easyVseasy():
    global xoo, wrong
    if not xoo:
        if wrong == False:
            wrong = True
            easy()
            print('Making move level "easy"')
            myList2[easydif] = "X"
            xoo = True
    else:
        if wrong == False:
            wrong = True
            easy()
            print('Making move level "easy"')
            myList2[easydif] = "O"
            xoo = False


def resetValor():
    global see, seu, win1, win2, draw1, draw2, Finish,xoo,sum,smu,shh
    win1, win2, draw1, draw2, see, seu, Finish,xoo,sum,smu,shh = False, False, False, False, False, False, True, False, False, False, False


def menu():
    global see, sue, sum, smu, xoo,shh
    while True:
        election = input("Input command: ")
        if election == "exit":
            break
        elif election == "start easy easy":
            see = True
            printempty()
            AskXorY()
        elif election == "start user easy":
            sue = True
            printempty()
            AskXorY()
        elif election == "start user medium":
            sum , xoo = True,False
            printempty()
            AskXorY()
        elif election == "start medium user":
            sum, smu, xoo = True, True, True
            printempty()
            AskXorY()
        elif election == "start hard user":
            sum,smu, xoo, True, True, True
            printempty()
            AskXorY()
        elif election == "start medium medium":
            shh = True
            printempty()
            AskXorY()            
        else:
            print("Bad parameters!")



def printempty():
    print("---------")
    for i in range(0, 9, 3):
        print("|" + " " + myList[i] + " " +
              myList[i+1] + " " + myList[i+2] + " " + "|")
    print("---------")


menu()
#-------------------------------------------------------------------------------------------------------------------------------------------
#First part of this proyect, using my logic to create a tic tac toe 
