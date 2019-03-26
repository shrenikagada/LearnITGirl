import random

doors=[0]*3
goatdoors=[0]*2
swap=0 #no.of swap wins
dont_swap=0 #no.of dont swap wins
j=0
while(j<10):
    x=random.randint(0,2) #xth door will comprise of BMW
    doors[x]="BMW"
    for i in range(3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoors.append(i)
    choice=int(input("Enter your choice : "))
    door_open=random.choice(goatdoors) #Open a door that comprises of goat
    while(door_open==choice): #door_open should not be equal to choice made by the participant
        door_open=random.choice(goatdoors)
    ch=input("Do you want to swap ? ")
    if(ch=='y'):
        if(doors[choice]=="Goat"):
            print(("Player Wins"))
            swap=swap+1
        else:
            print(("Player Lost"))
    else:
        if(doors[choice]=='Goat'):
            print("Player Lost")
        else:
            print("Player Wins")
            dont_swap+=1
    j+=1
print(swap,dont_swap)