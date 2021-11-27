import random
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def welcome():
     print(""" 
 --------------------------------------------------------------------------
  ___   _          _     _  _    ___    ___    ___     _     ___     ___  
 | __| | |        /_\   | || |  / _ \  | _ \  / __|   /_\   |   \   / _ \ 
 | _|  | |__     / _ \  | __ | | (_) | |   / | (__   / _ \  | |) | | (_) |
 |___| |____|   /_/ \_\ |_||_|  \___/  |_|_\  \___| /_/ \_\ |___/   \___/ 

 --------------------------------------------------------------------------
                           ADIVINA LA PALABRA
 --------------------------------------------------------------------------

        """)



def bye():
    print("""

--------------------------------------------------------------------------

                                ### 
                               ##   
                        ##### ##    
                              ##    
                        ##### ##    
                               ##   
                                ### 

--------------------------------------------------------------------------
                          VUELVE PRONTO
--------------------------------------------------------------------------
    
     """)



def intro():
    option = input("""
    Presione 1 para comenzar.
    Presione 2 para salir.
    """)

    print("elegiste la opción: ", option)

    if int(option) == 1:
        welcome()
        play()
    elif int(option) == 2:
        bye() 
    else:
        print("Comando errado vuelve a intentarlo")
        intro()


def read():
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    return words


# paso 1
def start():
    words = read()
    word = random.choice(words).lower().strip()
    print("La palabra secreta es" , word)
    print("La palabra secreta tiene" , len(word), "letras")
    board = ["_" for i in range(0, len(word)) ]
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    return board, word, []

lives = 10

# paso 2
def show_stage(a):
    error = a
    if error == lives:
        print("No te quedan mas vidas =( ")
    else:
        lives_out = lives - error
        print("Tienes", lives_out, "vidas.")




# paso 3    
def show_board(board, letters_error):
    for space in board:
        print(space, end= ' ')
    print()
    print()
    if len(letters_error) > 0:
        print('Letras incorrectas: ', *letters_error)
        print()


#  paso 4
def get_letter(board, letters_error):
    validate = False
    while not validate:
        l = input("Ingresa una letra: ").lower()
        validate = 'a' <= l <= 'z' and len(l) == 1
        if not validate:
            print('Error, la letra tiene que estar entre la a y z')
        else:
            validate = l not in board + letters_error
            if not validate:
                print('Letra repetida, prueba con otra.')
    return l


#  paso 5
def check_letter(l, word, board, letters_error ):
    if l in word:
        print("¡Genial! Has acertado una letra")
        update_board(l, word, board)
    else:
        print("¡Fallaste!")
        letters_error.append(l)


#  paso 6
def update_board(l, word, board):
    for i, word_sentence in enumerate(word):
         if l == word_sentence:
            board[i] = l

#  paso 7
def check_word(board):
    return '_' not in board
        


def play():
    board, word, letters_error = start()
    while len(letters_error) < lives:
        show_stage(len(letters_error))
        show_board(board, letters_error)
        l = get_letter(board, letters_error)
        check_letter(l, word, board, letters_error)
        if check_word(board):
            print(" ")
            print("*" * 48)
            print("*"* 16, "¡Haz ganado!", "*"* 16,)
            print("*" * 48)
            play_again()
    else:
        print(" ")
        print("*" * 48)
        print(f'¡Haz perdido! La palabra a adivinar era {word}.')
        print("*" * 48)
        show_stage(len(letters_error))
        
    show_board(board, letters_error)


def play_again():
    option = input("Deseas jugar otra vez (precione S para sí o cualquier otra tecla para salir: ")
    if option != 's': 
        clearConsole()
        bye()  
        exit()
    else:
        run()


def run():
    intro()
    while True:
        play()
    bye()  
  
    

if __name__ == '__main__':
    run()