from collections import deque

def queue_time(zakaznici, n):
    x = [0] * n 
    
    zakaznici = deque(zakaznici)
    
    while zakaznici:
        lowest_index = x.index(min(x)) 
        x[lowest_index] += zakaznici.popleft()
    
    print(max(x))

queue_time([2, 3, 10], 2)
