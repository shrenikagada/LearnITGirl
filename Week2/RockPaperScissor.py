def rock_paper_scissor(num1,num2,bit1,bit2):
    p1s=int(num1[bit1])%3
    p2s=int(num2[bit2])%3
    if(p1[p1s]==p2[p2s]):
        print("Draw")
    elif(p1[p1s]=="Rock" and p2[p2s]=="Scissor"):
        print("Player 1 wins")
    elif (p1[p1s] == "Rock" and p2[p2s] == "Paper"):
        print("Player 2 wins")
    elif (p1[p1s] == "Paper" and p2[p2s] == "Rock"):
        print("Player 1 wins")
    elif (p1[p1s] == "Paper" and p2[p2s] == "Scissor"):
        print("Player 2 wins")
    elif (p1[p1s] == "Scissor" and p2[p2s] == "Paper"):
        print("Player 1 wins")
    elif (p1[p1s] == "Scissor" and p2[p2s] == "Rock"):
        print("Player 2 wins")

p1={0:'Rock',1:"Paper",2:"Scissor"}
p2={0:"Paper",1:"Rock",2:"Scissor"}
while(1):
    num1=input("Player 1, Enter your choice  : ")
    num2 = input("Player 2, Enter your choice  : ")
    bit1=int(input("Player 1, Enter your secret bit position  : "))
    bit2 = int(input("Player 2, Enter your secret bit position  : "))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n")
    if(ch=='n'):
        break
