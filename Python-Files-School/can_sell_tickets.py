from collections import deque

def can_sell_tickets(zakaznici):
    twentyfive=0
    fifty=0
    hundred=0
    vysledek=True
    for x in zakaznici:
        if(x==25):
            twentyfive+=1
        elif(x==50):
            if(twentyfive>0):
                twentyfive-=1
                fifty+=1
            else:
                vysledek=False
        else:
            if(fifty>0 and twentyfive>0):
                fifty-=1
                twentyfive-=1
                hundred+=1
            elif(twentyfive>2):
                twentyfive-=3
                hundred+=1
            else:
                vysledek=False
    print(vysledek)


can_sell_tickets(deque([25,25,50]))
can_sell_tickets(deque([25,100]))
can_sell_tickets(deque([25,25,50,50,100]))
