import random
def instagram():
    score = 0
    instagram_followers = {
        "Cristiano Ronaldo": 668,
        "Lionel Messi": 510,
        "Selena Gomez": 420,
        "Kylie Jenner": 393,
        "Dwayne Johnson": 392,
        "Ariana Grande": 375,
        "Kim Kardashian": 355,
        "Virat Kohli": 273,
        "Neymar Jr": 222,
        "Kendall Jenner": 217,
        "Justin Bieber": 253,
        "Taylor Swift": 205,
        "Khloé Kardashian": 301,
        "Beyoncé": 310,
        "Kylian Mbappe": 118,
        "Nicki Minaj": 193,
        "LeBron James": 160,
        "Zendaya": 190,
        "Priyanka Chopra": 92,
        "Shraddha Kapoor": 87,
        "Alia Bhatt": 78,
        "Deepika Padukone": 75,
        "Katrina Kaif": 76,
        "Anushka Sharma": 64,
        "Akshay Kumar": 70,
        "Salman Khan": 66,
        "Shah Rukh Khan": 58,
        "Chris Hemsworth": 62,
        "MrBeast": 62,
        "Khaby Lame": 81
    }
    compare1=random.choice(list((instagram_followers)))
    def restart():
        nonlocal compare1
        compare2=random.choice(list((instagram_followers)))
        while compare1 == compare2:
            compare2 = random.choice(list(instagram_followers))
            
        print("Who can be having more followers on instagram")
        user=int(input(f"Enter 1 for {compare1} or 2 for {compare2} : "))
        if user==1:
            user=compare1
        elif user==2:
            user=compare2  
        else:
            print("You selected wrong ")   
        
        c1=instagram_followers[compare1]
        c2=instagram_followers[compare2]
        
        if c1>c2:
            for name,value in instagram_followers.items():
                if c1==value:
                    compare=name                   
        else:
            for name,value in instagram_followers.items():
                if c2==value:
                    compare=name 
        if user==compare:
            nonlocal score
            score+=1
            compare1=compare   
            restart()
        else:
    
            print(f"Your score is {score}")
            print("Thanks,for playing our game")
            
    restart()    

def twitter():
    twitter_followers = {
    "Elon Musk"          : 229.2,
    "Barack Obama"       : 130.5,
    "Cristiano Ronaldo"  : 115.7,
    "Narendra Modi"      : 108.9,
    "Justin Bieber"      : 108.8,
    "Donald Trump"       : 108.0,
    "Rihanna"            : 107.7,
    "Katy Perry"         : 104.5,
    "Taylor Swift"       : 93.6,
    "Kim Kardashian"     : 68.4,
    "Virat Kohli"        : 65.8,
    "Ellen DeGeneres"    : 62.7,
    "Bill Gates"         : 62.4,
    "Selena Gomez"       : 58.1,
    "Neymar Jr"          : 58.0
    } 
    compare3=random.choice(list((twitter_followers)))
    score=0
    def start():
        nonlocal compare3
        compare4=random.choice(list((twitter_followers)))
        while compare3 == compare4:
            compare4 = random.choice(list(twitter_followers))   
        print("Who can be having more followers on twitter")
        user=int(input(f"Enter 1 for {compare3} or 2 for {compare4} : "))
        if user==1:
            user=compare3
        elif user==2:
            user=compare4 
        else:
            print("You selected wrong ")   
                
        c3=twitter_followers[compare3]
        c4=twitter_followers[compare4]
                
        if c3>c4:
            for name,value in twitter_followers.items():
                if c3==value:
                    compare=name                   
        else:
            for name,value in twitter_followers.items():
                if c4==value:
                    compare=name
                     
        if user==compare:
            nonlocal score
            score+=1
            compare3=compare   
            start()
        else:
            
            print(f"Your score is {score}")
            print("Thanks,for playing our game")                
    start()      
   
  

def action():
    print("Type '1' for Instagram or 2'' for Twitter")     
    num =int(input("Enter the platform you want to play :")) 
    if num==1:
        instagram()
    elif num==2:
        twitter()  
    else:
        print("You haven't select correct one")     
        action() 
action()
  
    









