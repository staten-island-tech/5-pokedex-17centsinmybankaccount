import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)




# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# Add a language choice feature and print the pokemons name based on the user input
def choose_lang():
    x = input("What language are you playing?: ")
    x = x.upper()
    if x == "ENGLISH":
        print("language set as English")
        for pokemon in data:
            print(pokemon["name"]["english"])
    elif x == "JAPANESE":
        print("language set as Japanese")
        for pokemon in data:
            print(pokemon["name"]["japanese"])        
    elif x == "CHINESE":
        print("language set as Chinese")
        for pokemon in data:
            print(pokemon["name"]["chinese"])        
    elif x == "FRENCH":
        print("language set as French")
        for pokemon in data:
            print(pokemon["name"]["french"])        
    else:
        print("Bad spelling or we dont have that language. We have english japanese chinese and french")
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def searchasssist():
    search = input("What pokemon are youy trying to find?")
    for search in data():
        print(search)
searchasssist()
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

