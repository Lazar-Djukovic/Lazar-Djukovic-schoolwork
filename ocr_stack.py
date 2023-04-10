import random
stack_data = [random.randint(1,10) for _ in range(10)]
stack_size = 10
sp = -1

def isEmpty():
    

def stack_push(item):
    if sp == stack_size - 1:
        print('stack is full')
    else:
        sp += 1
        stack_data[sp] = item
  
def stack_pop():
    if sp == -1:
        print('stack is empty')
    else:
        x = stack_data[sp+1]
        sp -= 1
    return[x]
