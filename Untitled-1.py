def lang():
    user_text = input("What would you like to text: ") 
    T = 0
    S = 0
    for i in user_text():
        if i.upper() == "S":
            S+=1
        elif i.upper() == "T":
            T+=1
    if S >= T:
        print("French")
    else:
        print("English")
lang()