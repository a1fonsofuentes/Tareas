import random
"""
You are responsible for writing a program that plays a word guessing game with a user. Your
program will provide a category of words to the user and a string of dashes “-----” that represent
the length of the word. The user will guess the word and with each incorrect guess, your
program will reveal a letter at random, “-a---”. Upon guessing the word correctly, your program
will then inform the user how many guesses they took.
"""
print('\n Welcome to the Guess My world app.')

juego = {
    'sports':['basketball', 'baseball', 'cricket', 'football', 'golf', 'tennis', 'hockey'],
    'colors':['blue', 'red', 'yellow', 'violet', 'magenta', 'green'],
    'movies':['it', 'gladiator', 'speed', 'nightcrawler', '300', 'lost', 'focus'],
    'fruits':['apple', 'banana', 'orange', 'mango', 'strawberry', 'kiwi', 'grapes']
}

keys_juego = list(juego.keys())
active = True

while active:
    categoria_juego = keys_juego[random.randint(0,len(keys_juego)-1)]
    palabra_juego = juego[categoria_juego][random.randint(0,len(juego[categoria_juego])-1)]
    longitud_juego = len(list(palabra_juego))
    palabra_blanco = list()
    for i in range(0, longitud_juego):
        palabra_blanco.append('-')
    print(f'\n Guess the word which belongs to {categoria_juego} category and has {longitud_juego} letters')
    adivinar=""
    adivinar_contador = 0
    aciertos = 0

    while adivinar != palabra_juego:
        palabra_blanco_list = ' '.join(palabra_blanco)
        print(f'\n Word to guess {palabra_blanco_list}')
        adivinar = input('\n make a guess :').lower()
        adivinar_contador +=1

        file_name="intentos" + '.txt'
        file=open(file_name,"w") 
        file.write(str(adivinar_contador)+ "- intentos" + "\n")
        file.close()

        if adivinar_contador == longitud_juego - 2:
            print(f'\n Too many guesses. correct word is {palabra_juego}. Thank you for playing with us.')
            break

        if adivinar ==  palabra_juego:
            
            print(f'\n You won the game!! You took {adivinar_contador} chances.')
            aciertos +=1

            file_name="intentos" + '.txt'
            file=open(file_name,"a") 
            file.write(str(aciertos)+ "- aciertos" + "\n")
            file.close()
            break
        else:
            print('\n Oops! That\'s a wrong guess. Try Again. ')
            running=True
            while running:
                indice_letras = random.randint(0,longitud_juego-1)
                if palabra_blanco[indice_letras] == '-':
                    palabra_blanco[indice_letras] = palabra_juego[indice_letras]
                    running=False

        continuar_programa = input('\n Do you want to try again ? (y/n) : ').lower().strip()
        if continuar_programa.startswith('n'):
            active = False
            file= open("intentos.txt","r")
            linea = file.readline()
            while(linea):
                linea = file.readline()
            print('\n Have a nice day!')            

    continuar_programa = input('\n Do you want to play again ? (y/n) : ').lower().strip()
    if continuar_programa.startswith('n'):
        active = False
        file= open("intentos.txt","r")
        linea = file.readline()
        while(linea):
            linea = file.readline()
            print('\n Have a nice day!')