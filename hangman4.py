#importowanie
import random
from random import randint
import time
import datetime

#Listy
capital_name = []
countries = []
#Import z pliku
text_file = open('countries_and_capitals.txt')
text_score_file = open('FAME.txt', 'a+')
countries_capitals = text_file.read()
countries_capitals = countries_capitals.splitlines()
life = 5

#Data
now = datetime.datetime.now()
actual_time = now.strftime("%Y-%m-%d %H:%M")
print (now.strftime("%Y-%m-%d %H:%M"))

#definicje
def wygrana():
    '''Function which shows you string with congratulation print.
    It shows you game time and country
    '''
    print (bcolors.YELLOW +
    "Congratulations ! You are a hangman master ! You solve it in",
    end-start-2,"seconds" + bcolors.ENDC)
    print(city,"Capital of ", country)

def restart():
    '''
    Function to restart whole game.
    You can choose to play again, or close aplication.
    '''
    game_restart = input("Do you want to play again?(yes/no):")
    if game_restart == "yes" or game_restart == "Yes":
        print(bcolors.HEADER + "Let's continue !" + bcolors.ENDC)
    else:
        print(bcolors.HEADER + "Thank you for playing HangMan! Bye" + bcolors.ENDC)
        exit()

def game_over():
    '''
    Function that shows a game over screen, time and city
    '''
    print(HANGMAN[5])
    print(bcolors.YELLOW + "GAME OVER! Game tooks",end-start,"seconds" + bcolors.ENDC)
    print(steps, "-steps")
    print(city,"it was that capital !")

def save_score():
    '''
    Function that saves your score into a fame.txt
    Score is : name + data + game time + steps and city
    '''
    with open("FAME.txt", "a") as f:
        f.write(name + "|" + actual_time + "|" + str(end-start) + "|"
        + str(steps) + "|" + city + "\n" )

def hangman_print():
    '''
    Function that shows one picture of hangman. It depends on life argument
    '''
    if life == 4:
        print(HANGMAN[1])
    elif life == 3:
        print(HANGMAN[2])
    elif life == 2:
        print(HANGMAN[3])
    elif life == 1:
        print(country)
        print(HANGMAN[4])

def print_whole_word():
    print (bcolors.HEADER +
    "You decide to quess whole word. Please use capital letters" + bcolors.ENDC)

def choose_by_letter():
    print(bcolors.HEADER + "You decide to quess by using letters" + bcolors.ENDC)

def wrong_answer():
    print(bcolors.HEADER + "Wrong answer" + bcolors.ENDC)

def letter_used_already():
    print("You used that letter already !")

def city_country():
    '''
    Function that converts every letter into capital letter.
    It also add country and city to empty list (capital_name and countries)
    '''
    global city, country
    country = country.upper()
    city = city.upper()
    capital_name.append(city)
    countries.append(country)

def input_name():
    name = input("What's your name?: ")
    print (HANGMAN[0])
    print (life, "-liczba żyć")
    return name

def input_game_type():
    print(dash)
    choose = input(bcolors.HEADER +
    "Do you want to quess whole word, or only letter (write: word or letter)?: " +
    bcolors.ENDC)
    return choose

def life_letter_dash_show():
    print(dash)
    print(used_letters)
    print(life , "-number of lives")
#Wisielec lista
HANGMAN = [
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  | |
|
--------
"""]

#zmienne kolorów
class bcolors:
    HEADER = '\033[95m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

#Komunikat o liczbie żyć
print (bcolors.RED + "You have 5 lives" + bcolors.ENDC)

#Pętla
while True:
    name = input_name()

    #Rozdzielenie i wybór stolicy
    random_countries_capitals = countries_capitals[randint(0,len(countries_capitals))]
    random_countries_capitals = random_countries_capitals.split(' | ')
    country = random_countries_capitals[0]
    city = random_countries_capitals[1]
    city_country()

    #Rozdzielenie stolicy na pojedyncze litery
    correct_letters = list(city)
    dash = '_' * len(city)
    used_letters = []
    used_correct = []
    choose = input_game_type()
    steps = 0

    #Czas start
    start = time.time()

    #wybieramy że chcemy zgadnąc cały wyraz:
    if choose == "word" or choose == "Word":
        print_whole_word()
        while True:

            #Do wyboru wyrazu:
            if life > 0 and choose == "word" or choose == "Word":
                answer = input("Write Capital name: ").upper()

                #Warunek do wygrania:
                if answer == city:
                    end = time.time()
                    wygrana()
                    #Tworzy i zapisuje zmienne w pliku tekstowym
                    save_score()

                    #Czy chcesz zagrać od początku ?
                    restart()
                    life = 5
                    break

                #Zła odpowiedź!
                else:
                    wrong_answer()
                    life -= 2
                    steps += 1
                    hangman_print()

            #Jeśli przegrasz:
            else:
                end = time.time()
                game_over()

                #Czy chcesz zagrać od początku ?
                restart()
                life = 5
                break

    #wybieramy czy chcemy zgadywać literka po literce
    elif choose == "Letter" or choose == "letter":
        choose_by_letter()
        while True:

            #do wyboru literek
            if life > 0 and choose == "letter" or choose == "Letter":
                answer_dwa = input("Write a letter: ").upper()
                if len(answer_dwa) == 1 and answer_dwa.isalpha() and answer_dwa in correct_letters:
                    used_letters.append(answer_dwa)
                    used_correct.append(answer_dwa)

                    #Zastępowanie podłóg wybranymi literkami
                    for i in range(len(city)):
                        if city[i] in answer_dwa:
                            dash = dash[:i] + city[i] + dash[i+1:]
                            correct_letters.remove(answer_dwa)
                    steps += 1
                    life_letter_dash_show()

                    #Warunek do wygrania
                    if len(correct_letters) == 0:
                        end = time.time()
                        wygrana()

                        #Tworzy i zapisuje zmienne w pliku tekstowym
                        save_score()

                        #Czy chcesz zagrać od początku ?
                        restart()
                        life = 5
                        break
                    else:
                        continue

                #Jeśli wpiszesz cały wyraz zamiast literki:
                elif answer_dwa == city:
                    end = time.time()
                    wygrana()
                    #Tworzy i zapisuje zmienne w pliku tekstowym
                    save_score()

                    #Czy chcesz zagrać od początku ?
                    restart()
                    life = 5
                    break

                #Jeśli powtórzysz dobrą literkę:
                elif len(answer_dwa) == 1 and answer_dwa.isalpha() and answer_dwa in used_correct:
                    letter_used_already()
                    continue

                #Jeśli powtórzysz użytą literkę
                elif len(answer_dwa) == 1 and answer_dwa.isalpha() and answer_dwa in used_letters:
                    letter_used_already()
                    continue

                #Jeśli źle wpiszesz literkę:
                else:
                    print("Wrong letter")
                    used_letters.append(answer_dwa)
                    life -= 1
                    steps += 1
                    life_letter_dash_show()
                    hangman_print()

            #Jeśli przegrasz:
            else:
                end = time.time()
                game_over()

                #Czy chcesz zagrać od początku ?
                restart()
                life = 5
                break

    #Jeśli nie wpiszemy word lub letter:
    else:
        wrong_answer()
        end = time.time()
        continue
