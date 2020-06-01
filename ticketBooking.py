films = {
    "Finding Dory": [3,2],
    "Ghoul" : [18,1],
    "Texas":[32,1]
    }
while True:
    choice= input("What film do you want to watch?: ").strip().title()
    if choice in films:
        age = int (input ("How old are you?: ").strip())
        
        if age>= films[choice][0] :
                seats= films[choice][1]
                if seats> 0:  
                    print ("Enjoy the film!")
                    films[choice][1] = films[choice][1] -1
                else:
                    print("Sorry no seats left!")
        else:
            print ("You're too young to watch this movie!")
    else :
            print ("Sorry!We don't have that film.")

