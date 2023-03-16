stack1 = []
stack2 = []
stack3 = []

import random
candidates = ["B","C","D"]
stacks = [["X" for _ in range(100)],[],[]]
for i in range(52):
    done = False
    while not done:
        rnd=random.randint(0,99)
        if stacks[0][rnd] == "X":
            stacks[0][rnd] = "A"
            done = True
for i in range(100):
    if stacks[0][i] == "X":
        stacks[0][i] = random.choice(candidates)
    
#print(stacks[0])
#print(stacks[0][-1]) #peek


for i in range(len(stack1)):
    stack2.append(stack1.pop())

print(stack2)


for i in range(len(stack2)):
    stack3.append(stack2.pop())

print(stack3)


