import numpy as np 

import matplotlib.pyplot as plt 

states = [

"First State",

"Second State",

"Third State",

"Fourth State",

"Fith State",

]

#each row describes probalities of the next state 
P = np.array([

[0.1, 0.4, 0.3, 0.2, 0.0],
    [0.2, 0.2, 0.4, 0.1, 0.1],
    [0.3, 0.1, 0.1, 0.3, 0.2],
    [0.2, 0.1, 0.2, 0.2, 0.3],
    [0.1, 0.1, 0.1, 0.5, 0.2]

])

current = 0 

history = [current]

# Evolve the system

# Evolve the system
for t in range(300):
    current = np.random.choice(
        len(states), p=P[current]
    )
    history.append(current)

# Visualise the sequence of states
plt.figure(figsize=(12, 5))
plt.plot(history, alpha=0.7)
plt.yticks(range(len(states)), states)
plt.xlabel("Time")
plt.ylabel("System state")
plt.title("Probabilistic State Machine")
plt.grid(alpha=0.2)
plt.show()
