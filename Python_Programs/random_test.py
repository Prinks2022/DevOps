import random

mylist = ['R', 'S', 'P', 'D', 'W'] 
mylist2 = ['R', 'S', 'P', 'W'] 

def make_move(rounds):
    dyna = 10
    #print(rounds)
    for r in range(1,int(rounds)):
        # mychoice = random.choice(mylist)
        # print(mychoice)
        # if mychoice == 'D':
        #     count = count +1
        #     if count == 5:
        #         break
        #     else:
        #         mychoice = random.choice(mylist2)
        #     print(count)
        #print(r)
        #dyna = 10
        if dyna > 0:
            dyna -= 1
            print(dyna)
            ch ='D'
    
        else:
            options = ['R', 'P', 'S']
            ch = random.choice(options)
    return ch

print(make_move(20))
