import random

def choose():
    words=['Computer','Rainbow','Science','Programming','player']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"Your score is",p1)
    print(p2n,"your score is",p2)
    print("Have a nice day")

def play():
    p1name=input("Enter the name 1")
    p2name=input("Enter the name 2 ")
    pp1=0
    pp2=0
    turn=0
    while(1):
            picked_word=choose()
            qn=jumble(picked_word)
            print(qn)
            if turn%2==0:
                print(p1name,"This is your turn")
                ans=input("Whats on my mind?")
                if ans==picked_word:
                    pp1=pp1+1
                    print(pp1,"is your score")
                else:
                    print("Better luck next time,I thought the word :",picked_word)
                c=input("Do you want to continue")
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break
            else:
                print(p2name,"This is your turn")
                ans = input("Whats on my mind?")
                if ans == picked_word:
                    pp2 = pp2 + 1
                    print(pp2, "is your score")
                else:
                    print("Better luck next time,I thought the word :", picked_word)
                c = input("Do you want to continue")
                if c == 0:
                    thank(p1name, p2name, pp1, pp2)
                    break
            turn=turn+1
play()
