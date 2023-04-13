import random
import variables 

def run_infec(population):
  for x in population:
      if x.infection_type != "":
        for y in population:
          if random.random() < 1/len(population) * x.infection_type.R and y.immunity_type != x.infection_type and y.infection_type == "":
            if y.immunity_type != "" and random.random() > variables.immunity_infec:
              y.infection_type = x.infection_type 
            elif y.immunity_type == "":
              y.infection_type = x.infection_type

def update_infec(population):
  newpop = []
  for x in population:
    if x.infection_type != "":
      x.length += 1
      if random.random() > x.infection_type.deadliness:
        newpop.append(x)
    else:
      newpop.append(x)
    if x.length > 2:
      x.immunity_type = x.infection_type
      x.infection_type = ""
      x.length = 0
  return newpop

def infec_pop(number, population, array):
  count = 0
  for x in range(number):
    for y in range(len(array)):
      population[count].infection_type = array[y]
      count += 1
  return population
