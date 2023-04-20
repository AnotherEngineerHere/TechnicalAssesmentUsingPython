import random
import sys


steps: int = 0
playerPosition: int = 0
flag: bool = False


def throwDice() -> int:
    return random.randint(1, 6)


def print_grid(arr):
    for i in range(5):
        for j in range(5):
            print(arr[i][j], end=" "),
        print()


cadena = ["1 2 3 4 5", "10 9 8 7 6", "11 12 13 14 15",
    "20 19 18 17 16 15", "21 22 23 24 25"]
matriz = []
for c in cadena:
    numeros = c.split()
    fila = [int(n) for n in numeros]
    matriz.append(fila)
matriz.reverse()


menu_options = {
    1: 'Arrojar dados',
    2: 'Salir',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def movePlayer(arr, value) -> int:
    global playerPosition
    for i in range(5):
        for j in range(5):
            valueSearched = arr[i][j]
            if (valueSearched == value):
                playerPosition = valueSearched
    return playerPosition

def checkSnakes(arr,value:int):
            if(value==24):
                movePlayer(arr,16)
                print("Jugador  desciende al cuadro",16)
            elif(value==22):
                movePlayer(arr,20)
                print("Jugador  desciende al cuadro",20)
            elif(value==19):
                movePlayer(arr,8)
                print("Jugador  desciende al cuadro",8)
            elif(value==14):
                movePlayer(arr,4)
                print("Jugador  desciende al cuadro",4)
                
def checkStairs(arr,value:int):
            if(value==3):
                movePlayer(arr,11)
                print("Jugador  asciende al cuadro",11)
            elif(value==6):
                movePlayer(arr,17)
                print("Jugador  asciende al cuadro",17)
            elif(value==9):
                movePlayer(arr,18)
                print("Jugador  asciende al cuadro",18)
            elif(value==10):
                movePlayer(arr,12)
                print("Jugador  asciende al cuadro",12)

def checkWinCondition(arr,valueToBeSearched,actualDiceVal:int):
    if(valueToBeSearched==25):
        print("Has ganado felicidades")
        sys.exit()
    if(valueToBeSearched>25):
        val = (valueToBeSearched-actualDiceVal)
        valueToSetIfFail = actualDiceVal-val
        movePlayer(arr,valueToSetIfFail)
        print("Jugador ha descendido  al cuadro",valueToSetIfFail)              
def option1():
    global flag
    global playerPosition

    if (not flag):
        valueToBeSearched: int = throwDice()
        print('Dado arroja: ', valueToBeSearched)
        playerPosition = movePlayer(matriz, valueToBeSearched)
        print("Jugador avanzo a", playerPosition)
        flag = True
    else:
        valueToBeSearched: int = throwDice()
        print('Dado arroja: ',valueToBeSearched)
        valueToBeSearched = valueToBeSearched+playerPosition
        playerPosition= movePlayer(matriz,valueToBeSearched)
        print("Jugador avanzo a cuadro",playerPosition)
        checkWinCondition(matriz,valueToBeSearched,playerPosition)
        checkStairs(matriz, playerPosition)
        checkSnakes(matriz, playerPosition)


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            option1()
        elif option == 2:
            print('Thanks message before exiting')
            sys.exit()
        else:
            print('Invalid option. Please enter a number between 1 and 2.')


