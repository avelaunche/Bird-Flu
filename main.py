import matplotlib.pyplot as plt
import maintenance as mt
import infec as inf
import variables
from classes import virus
import count as cnt

bird_pop = mt.gen_pop()

virus1 = virus(variables.R1, variables.deadliness1)
virus2 = virus(variables.R2, variables.deadliness2)

virus_array = [virus1, virus2]

infection_container = []
for x in virus_array:
  infection_container.append([])

bird_pop = inf.infec_pop(10, bird_pop, virus_array)

for x in bird_pop:
  print(x.infection_type)

time = range(0, variables.length)
infec = []
life = []
immunity = []

for x in range(variables.length):
  print(x)
  
  population = mt.total("B", bird_pop)
  
  mt.move_pop("W", bird_pop)
  bird_pop = mt.winter(bird_pop)
  print("W")
  inf.run_infec(bird_pop)

  count1, count2, infection_container = cnt.final_count(bird_pop, virus_array, infection_container)
  infec.append(count1)
  life.append(len(bird_pop))
  immunity.append(count2)
  bird_pop = inf.update_infec(bird_pop)

  print()

print(virus_array)
for x in range(len(bird_pop)):
  print(bird_pop[x].immunity_type)

plt.plot(time, infec)
plt.plot(time, life)
for x in range(len(virus_array)):
  plt.plot(time, infection_container[x])
plt.plot(time, immunity)
plt.show()


#description of current model: breeding grounds, wintering grounds, 
