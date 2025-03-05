import random 
    
username1 = input("what is your 1st name - ")
username2 = input("what is your  2nd name - ")
    
    
m1 =  username1 + username2 + str(random.randint(10,99))
m2 =  random.choice(username1) + random.choice(username2) + str(random.randint(10,9999)) 
m3 = username2[::-1] + "@" + username1[::-1]
m4 = username2 [-3:-1:1] + username1 [-3:-1:1]
m = [m1,m2,m3,m4]
print(random.choice(m))


