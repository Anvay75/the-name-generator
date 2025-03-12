import random 
print("Username generator, do what is said and if you wan to stop doing it then the break option will come to get out of the loop")
while True:
    
    username1 = input("what is your 1st name - ")
    username2 = input("what is your  2nd name - ")
    
    joiners = ["@","*","%","^",]    
    m1 =  username1 + username2 + str(random.randint(10,99))
    m2 =  random.choice(username1) + random.choice(username2) + str(random.randint(10,9999)) 
    m3 = username2[::-1] + "@" + username1[::-1]
    m4 = username2 [-3:-1:1] + username1 [-3:-1:1]
    m5 = username1,random.choice(joiners),username2
    m = [m1,m2,m3,m4,m5]
    print(random.choice(m))
    Choice = input("do you want to break out of the loop? - ")
    if Choice == "yes":
            print("thank you for playing ths game")
            break
    

    

