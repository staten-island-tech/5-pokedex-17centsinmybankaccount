import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list

def choose_lang():
    x = input("What language are you playing?")
    x = x.upper()
    if x == "ENGLISH":
        print("language set as English")
    elif x == "JAPANESE":
        print("Japanese")
    elif x == "CHINESE":
        print("language set as Chinese")
    elif x == "FRENCH":
        print("language set as French")
    else:
        print("Bad spelling or we dont have that language. We have english japanese chinese and french")





# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input
def choose_lang():
    x = input("What language are you playing?")
    x = x.upper()
    if x == "ENGLISH":
        print("language set as English")
        pokedex.english
    elif x == "JAPANESE":
        print("Japanese")
        y = "japanese"
    elif x == "CHINESE":
        print("language set as Chinese")
        y = "chinese"
    elif x == "FRENCH":
        print("language set as French")
        y = "french"
    else:
        print("Bad spelling or we dont have that language. We have english japanese chinese and french")
choose_lang()
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def searchasssist():
    search = input("What pokemon are youy trying to find?")
    for search in pokedex:
        print(pokedex.name)

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

