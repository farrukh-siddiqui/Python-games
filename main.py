import sys
import random
# This list is for words in hangman
list1 = ['serious', 'able', 'fiction', 'argument', 'like', 'little', 'old', 'smell', 'than', 'disease', 'fertile', 'taste', 'train', 'manager', 'living', 'education', 'development', 'gun', 'paper', 'ear', 'boy', 'behaviour', 'grey', 'other', 'act', 'view', 'connection', 'day', 'transport', 'nose', 'weight', 'colour', 'sign', 'at', 'cart', 'happy', 'money', 'sugar', 'base', 'from', 'liquid', 'almost', 'first', 'hope', 'servant', 'wine', 'again', 'electric', 'green', 'number', 'look', 'chin', 'blood', 'father', 'space', 'chain', 'kiss', 'keep', 'distribution', 'measure', 'science', 'knife', 'use', 'sock', 'memory', 'south', 'wide', 'angle', 'enough', 'no', 'record', 'property', 'coal', 'silk', 'heart', 'he', 'to', 'up', 'year', 'needle', 'woman', 'sex', 'thick', 'list', 'much', 'paint', 'smile', 'protest', 'note', 'experience', 'limit', 'lead', 'long', 'spoon', 'week', 'kick', 'debt', 'family', 'present', 'steam']

# These variable are for Tic Tac Toe ####
board = [" " for x in range(10)]        #
Running = 0                             #
Win = 1                                 #
Draw = 2                                #
game = Running                          #
mark = "X"                              #
player = 1                              #
#\/\/\/\/\/\/\/\/\//\/\/\/\//\/\/\/\/\/\#

welcome_message = ("""Hello and welcome to our project
This project has been made by:
Abdullah Shabir 
Farukh Ahmed 
-----------------------------------------------------------------------------------------
 
First you have to login or signup to play some of the games we have made for you.
Thanks we hope you will enjoy
            o
            o
     //@@  o
    @@ ")
   @@@ - @   _____
  /  \ / \  |\____\
 /  ( X ) | | |   |
<___=\      | |   |
    \======\ \|_"_|
                (____



                                    __________
                           ________|          |________
                          |       /   ||||||   \       |
                          |     ,'              `.     |
                          |   ,'                  `.   |
                          | ,'   ||||||||||||||||   `. |
                          ,'  /____________________\  `.
                         /______________________________\
                        |                                |
                        |                                |
                        |                                |
                        |________________________________|
     _ Seal _             |____________________------__|

              ,----------------------------------------------------,
              | [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |
              |                                                    |
              |  [][][][][][][][][][][][][][_]    [][][]  [][][][] |
              |  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |
              | [][_][][][][][][][][][][][][]||     []    [][][][] |
              | [__][][][][][][][][][][][][__]    [][][]  [][][]|| |
              |   [__][________________][__]              [__][]|| |
              `----------------------------------------------------'



                                 .........
                               .'------.' |       Plug and Play
                              | .-----. | |
                              | |     | | |
                            __| |     | | |;. _______________
                           /  |*`-----'.|.' `;              //
                          /   `---------' .;'              //
                    /|   /  .''''////////;'               //
                   |=|  .../ ######### /;/               //|
                   |/  /  / ######### //                //||
                      /   `-----------'                // ||
                     /________________________________//| ||
                     `--------------------------------' | ||
                      : | ||      | || |__LL__|| ||     | ||
                      : | ||      | ||         | ||     `""'
                      n | ||      `""'         | ||
                      M | ||                   | ||
                        | ||                   | ||
                        `""'                   `""'
""")

def games(user):
    prompt = "which games do you want to play: \n 1) Hangman \n 2) Rock Papaper scissor \n 3) TicTactoe \n To exit enter \"q\" \n "
    while user != 'q':      
        user = input(prompt)
        if user == 'q':
            print("Good bye see you later ")
        if user == '1':
            hangmanf('user')
        if user == '2':
            rockpaperscissor('user')
        if user == '3':
            tictactoe('user')
        else:
            continue

def hangmanf(user):
    print('''
    ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \
    | |          ||  `/,|
    | |          (\\`_.'
    | |         .-`--'.
    | |        /Y . . Y\
    | |       // |   | \\
    | |      //  | . |  \\
    | |     ')   |   |   (`
    | |          ||'||
    | |          || ||
    | |          || ||
    | |          || ||
    | |         / | | \
    """"""""""|_`-' `-' |"""|
    |"|"""""""\ \       '"|"|
    | |        \ \        | |
    : :         \ \       : :  sk
    . .          `'       . .
    ''')
    play = True
    # We set a loop to let the user play again and again until he quits
    while play:
        word = random.choice(list1)           #This will chose a word from list1    
        # welcome message
        message = """ Welcome to the hangman you have to guess the word that is in my mind
        you have to guess the word before your lives are finished.
        enjoy."""
        print(message ,'\n')    
        letter_word = set(word)         #set of letters in choosed word
        correct_letter = set()          # it will store correctly guessd letter by the user
        used_letter = set()             # it will store the letter guessed by user so the user wont guess again same
        use_letter = []
        word_letter = set(word) 
        print("---------------------- Guess this letter-------------------------- ")
        for x in word: 
            print("-",end=" ")
        print() 
        lives = 7                       # user got 7 lives  
        while letter_word and lives > 0: #This loop will end when all the letters are guessed or lives are finished
            print(f"you have {lives} lives left and you have used following letter {use_letter}")
            print('----------------------------------------------------------------------------------------------------------------')
            print()
            user = input("Enter a letter :")
            use_letter.append(user)
            if user in used_letter:         #This will check if the user has already used that letter
                print("You have already used this letter : ")   
            elif user in letter_word:   #This will check if the letter guessd is in word
                correct_letter.add(user)    #This will add correct letter to set storing corrct letters
                used_letter.add(user)       #This will add correct letter to set storing used letters
                letter_word.remove(user) # This will remove letters that are guessed from word
            else:
                lives -= 1
                used_letter.add(user)   
            for letter in word:             # This for loop will either print corrct letter or -
                if user==letter:            # This will check if guessed letter == letters in word one by one
                    print(letter,end=" ")
                else:
                    if letter in correct_letter: # This will check if user has already guessed that letter 
                        print(letter,end=" ")    # This will print the previously guessed letters
                    else:
                        print('-',end=" ")  
            print() 
        # The loop ends and this section would check that the user has won or lost
        if correct_letter == word_letter:
            print("you have guessed the letter")
            user = eval(input("Do you want to play again : 1)Play again 2)exit:"))
            if user == 2:
                play = False
        else:
            print(f"you lose the word was {word}")
            user = eval(input("Do you want to play again : 1)Play again 2)exit:"))
            if user == 2:
                play = False
def rockpaperscissor(user):
    while True:
        userwin = 0
        computerwin = 0
        import random
        rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''

        paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

        scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''


        computer  = random.randint(1,3)
        user = int(input("Chose 1) for rock 2) for paper 3) for scissor"))

        if user == 1:
          print(rock)
        elif user == 2:
          print(paper)
        else:
          print(scissors)
        print()
        print("Computer choose:")
        if computer == 1:
          print(rock)
        elif computer == 2:
          print(paper)
        else:
          print(scissors)


        if user == computer:
          print("It's a Draw")
        if user == 1 and computer == 2 or user == 2 and computer == 3 or user ==3 and computer == 1:
          print("YOu  lose")
          computerwin += 1

        if user == 2 and computer == 1 or user == 3 and computer == 2 or user ==1 and computer ==3:
          print("You won")
          userwin += 1
        user = input("Do you  want to play : Enter 'p' for play and 'q' to qiut : ")
        if user == 'p':
            continue
        elif user == 'q':
            print(f"You won {userwin} and computer won {computerwin}|times")
            break
        else:
            print("Can't under stand that")

user_data = {}

def tictactoe(user):
    while True:
        print('''

        _   _      _             _             
        | | (_)    | |           | |            
        | |_ _  ___| |_ __ _  ___| |_ ___   ___ 
        | __| |/ __| __/ _` |/ __| __/ _ \ / _ \
        | |_| | (__| || (_| | (__| || (_) |  __/
         \__|_|\___|\__\__,_|\___|\__\___/ \___|



                     .--
               ==-   .\#\
                  ,-._\\ \=- .
                  |#___"\ \_);
           =--      '  \\\#\
              ==--      \`--'
                         ""         .--
                             ==--   .\#\
                                 ,-._\\ \=- .               )
                          ==-    |#___"\ \_);              (
                                   '  \\\#\                 ))
                                ==-    \`--'               ((
                                        ""                  ))
              ______________                __              (  __
            ,'              `.            ('__`>           , ) __`.
           /                  \____       /==(^)     ______ ( -'_--`.
          |     All right!     ,-'        `\_-/    |()|::::)= '_`.  .
          |     All right!     |     _____ / /\  /)____||____\_-``.
          |   You guys win!    |          `-------'            \-`   ,
           \                  /      &  ,   .  &  ,   .  &  ,   | '
            `.______________,'       _\'     `/_\'     `/_\'    |
                                     _|`.   ,'|_|`.   ,'|_|`.   |
                                                                |\
                                     __________________________/__\
                                                             .`.-_-\
                                                            `_`.'_-_\
                                                               -- -
        ''')
        def draw_board():  # this function draws the board
            print(" {} | {} | {}".format(board[1],board[2],board[3]))
            print("___|___|___")
            print(" {} | {} | {}".format(board[4],board[5],board[6]))
            print("___|___|___")
            print("   |   |   ")
            print(" {} | {} | {}".format(board[7],board[8],board[9]))

        def check_win(): # This function check for win
            global game   # This is global variabe so you can modify it in a function
                           #This check for win in rows
            if board[1] == board[2] and board[2] == board[3] and board[1] != " ":
                game = Win
            elif board[4] == board[5] and board[5] == board[6] and board[4] != " ":
                game = Win
            elif board[7] == board[8] and board[8] == board[9] and board[7] != " ":
                game = Win
                        #This check for win in diagonal
            elif board[1] == board[5] and board[5] == board[9] and board[1] != " ":
                game = Win
            elif board[7] == board[5] and board[5] == board[3] and board[7] != " ":
                game = Win
                        # This check for win in Columns
            elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
                game = Win
            elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
                game = Win
            elif board[3] == board[6] and board[6] == board[9] and board[3] != " ":
                game = Win
                        # This check for draw
            elif board[1] != " " and board[2] != ' ' and board[3] != " " and board[4] != ' ' and board[5] != " " and board[6] != ' ' and board[7] != " " and board[8] != ' ' and board[9] != ' ':
                game = Draw
            else:
                game = Running

        def check_position(x):  # This function check for empty space
            if board[x] == " ":  # Here board[x] is the position where player want to insert mark
                return True       # This function will return True if that space is empty or false if it is occupied
            else:
                return False

        while game == Running:      #This loop will run the game untill check win is executed
            global player             #player is made global to modify it in a function
            draw_board()
            if player % 2 != 0:         #This if condition will decide the players turn and will set the mark X or O
                print("It's player 1 turn ")
                mark = "X"
            else:
                print("It's player 2 Turn ")
                mark = "O"
            x = eval(input(" chose the option :")) # user input
            if (check_position(x)):     # This will check the function check_position by providing user input as argument 
                player += 1               # If the space is empty function will return True and if condition will execute
                board[x] = mark             # This will replace the empty space with X or O 
                check_win()

        draw_board()
        if game == Win:
            if player % 2 != 0:
                print("Player 2 wins")
            else:
                print("Player 1 wins ")
        else:
            print("It's a Draw")
        print("Do you wanna play again : ")
        user = input("Enter 'y' for yes and 'N' for No: ").lower()
        if user == 'y':
            tictactoe(user)
        elif user == 'n':
            break
        else:
            print("Can't understand that ")


def introduction(name,age,password):
    user_name = input("Please Enter your name:")
    user_password = input("Please Enter your password: ")
    user_data.update({'name':user_name,'passord':user_password})
    return user_data


def sign_up(password):
    print(" You have to login agan before playing the game:")
    x = 0
    while x < 5:
        user_pas = input("Please again enter the password to continue :")
        if user_pas == user_data["passord"]:
            print(" Congratulations you can now play the game")
            move = True
            break
        else:
            print(f"Please try again you have {4-x} tries left ")
            x += 1
            if x == 5:
                print("Good bye")
                sys.exit(0)
    print("It's done")

print(welcome_message)
introduction('name','age','pass') 
sign_up('password')
games('user')
