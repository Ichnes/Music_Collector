import random
import csv


with open('music.csv', encoding='utf-8-sig') as csvfile:
    new_split = csvfile.readlines()
    splitted = [line.split(" | ") for line in new_split]
    music_collection = [((line[0].replace('\ufeff', ''), line[1]), (int(line[2]), line[3], line[4].replace('\n', '')))for line in splitted]


def adding():
    '''
    Add new album to csv in defined format
    '''
    print('Enter an artist: ')
    artist = input()
    print('Enter an album: ')
    album = input()
    print('Enter year of release: ')
    year = input()
    if year.isdigit() and len(year) == 4:
        print('Enter type of music: ')
        music_type = input()
        print('Enter time of album in minute:second format: ')
        album_time = input()
        min_sec = album_time.split(":")
        if min_sec[0].isdigit() and min_sec[1].isdigit():
            minutes = min_sec[0]
            seconds = min_sec[1]
            album_time = (':').join([minutes, seconds])
        else:
            print("wrong format! please, give me minutes and seconds.")
        new_song = artist + ' | ' + album + ' | ' + year + ' | ' + music_type + ' | ' + album_time
        with open('music.csv', "a") as add_album:
            add_album.write(new_song + "\n")


def find_by_artist():
    '''
    Function that allows you to find artist from csv
    '''
    search_by = False
    print("Enter name of artist: ")
    name_artist = input()
    print("All albums maked by this artist:" + "\n")
    for prime_tuple in music_collection:
        if name_artist.lower() == prime_tuple[0][0].lower():
            author = prime_tuple[0][0]
            name_alb = prime_tuple[0][1]
            show_author = "Album: " + name_alb + " | Artist: " + author
            print (show_author)
            search_by = True
    if search_by is True:
        print ("\n")
    else:
        print("Not found! Try again.")


def find_by_year():
    '''
    You input a year, and the function shows albums by this year
    '''
    search_by = False
    print("Enter year of album:")
    year_album = input()
    print("All albums maked in this year:" + "\n")
    for prime_tuple in music_collection:
        if year_album.lower() == str(prime_tuple[1][0]).lower():
            author = prime_tuple[0][0]
            name_alb = prime_tuple[0][1]
            show_author = "Album: " + name_alb + " | Artist: " + author
            print(show_author)
            search_by = True
    if search_by is True:
        print("\n")
    else:
        print("Not found! Try again!")


def find_by_letters():
    '''
    Function wants to take letter from you.
    After that it check album name and print you that albums,
     which contain that letter from input
     '''
    search_by = False
    print("Type the letters without space:")
    letters = input()
    print("All albums with typed letters:" + "\n")
    for prime_tuple in music_collection:
        if letters.lower() in str(prime_tuple[0][1]).lower():
            author = prime_tuple[0][0]
            name_alb = prime_tuple[0][1]
            show_author = "Album: " + name_alb + " | Artist: " + author
            print(show_author)
            search_by = True
    if search_by is True:
        print ("\n")
    else:
        print("Not found! Try again!")




def find_by_album():
    '''
    Funcion check your input, then print that album, artist etc.
    '''
    search_by = False
    print("Enter title of album:")
    title_of_album = input()
    print("This album was made by:" + "\n")
    for prime_tuple in music_collection:
        if title_of_album.lower() == str(prime_tuple[0][1]).lower():
            author = prime_tuple[0][0]
            name_alb = prime_tuple[0][1]
            show_author = "Album: " + name_alb + " | Artist: " + author
            print(show_author)
            search_by = True
    if search_by is True:
        print("\n")
    else:
        print("No album in database!")


def find_by_genre():
    '''
    Function shows all albums by genre
    '''
    search_by = False
    print("Enter genre of albums:")
    genre = input()
    print("All albums in this genre:" + "\n")
    for prime_tuple in music_collection:
        if genre.lower() == prime_tuple[1][1].lower():
            author = prime_tuple[0][0]
            name_alb = prime_tuple[0][1]
            show_author = "Album: " + name_alb + " | Artist: " + author
            print(show_author)
            search_by = True
    if search_by is True:
        print("\n")
    else:
        print("Genre not found! Try again!")


def calculate_age():
    '''
    Function that calculate age of albums.
    It takes actual year - album year
    '''
    year = 2017
    age_sum = 0
    for name, information in music_collection:
        album_year = int(information[0])
        calc_age = year - album_year
        age_sum = age_sum + calc_age
    print("Age of all albums: ", age_sum, " years.")


def random_by_genre():
    '''
    Function that take random album from genre
    '''
    random_choice = []
    search_by = False
    print("Enter genre of albums:")
    genre = input()
    print("Random album by genre:" + "\n")
    for prime_tuple in music_collection:
        if genre.lower() == prime_tuple[1][1].lower():
            year = str(prime_tuple[1][0])
            author = prime_tuple[0][0]
            name_alb = prime_tuple[0][1]
            show_author = "Album: " + name_alb + " | Artist: " + author + " | Year: " + year
            random_choice.append(show_author)
            search_by = True
    if search_by is True:
        print(random.choice(random_choice))
    else:
        print("Genre not found! Try again!")


def amount_of_albums():
    '''
    Function that count number of albums which is made by one artist
    '''
    search_by = False
    print("Enter name of artist:")
    name_artist = input()
    amount = 0
    for prime_tuple in music_collection:
        if name_artist.lower() == prime_tuple[0][0].lower():
            amount = amount + 1
            search_by = True
    if search_by is True:
        print("Amount of albums maked by this artist: ", amount)
    else:
        print("Artist not found! Try again!")


def find_the_longest():
    '''
    Function that shows the longest album
    '''
    all_album_times = []
    for prime_tuple in music_collection:
        time = prime_tuple[1][2]
        all_album_times.append(time)
    longest = max(all_album_times)
    for album in music_collection:
        if album[1][2].lower() == longest:
            print("The longest album have: ", album[1][2], " | Author: ", album[0][0], "| Album ", album[0][1])


def main():
    '''
    Main function. It prints whole menu
    '''
    while True:
        print("Welcome in the CoolMusic! Choose the action:")
        print("1) - Add new album")
        print("2) - Find albums by artist")
        print("3) - Find albums by year")
        print("4) - Find musician by album")
        print("5) - Find albums by letter(s)")
        print("6) - Find albums by genre")
        print("7) - Calculate the age of all albums")
        print("8) - Choose a random album by genre")
        print("9) - Show the amount of albums by an artist")
        print("10) - Find the longest-time album")
        print("0) - exit")
        print("Tell me a number from 0 to 10")

        number = input()

        if number == '1':
            adding()
        elif number == '2':
            find_by_artist()
        elif number == '3':
            find_by_year()
        elif number == '4':
            find_by_album()
        elif number == '5':
            find_by_letters()
        elif number == '6':
            find_by_genre()
        elif number == '7':
            calculate_age()
        elif number == '8':
            random_by_genre()
        elif number == '9':
            amount_of_albums()
        elif number == '10':
            find_the_longest()
        elif number == '0':
            break
        else:
            print("Enter only numbers in range <0:10>")

        ask = ""
        while not (ask == 'YES' or ask == 'NO'):
            ask = input("Do you want to try again? (YES/NO) ").upper()
        if ask == 'NO':
            break


main()
