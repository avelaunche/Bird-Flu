import infec as inf
import random
import variables
import count
from classes import bird1
    
def gen_pop():
  population = []
  for x in range(variables.startpop):
    population.append(bird1("B", ""))
  return population

def move_pop(loc,population):
  for x in population:
    x.loc = loc
  return population

def breeding(population):
  dead = variables.startpop - len(population)
  for x in range(dead):
    population.append(bird1(population[0].loc, ""))
  return population

def winter(population):
  newpop = []
  for x in population:
    if random.random() < 0.8:
      newpop.append(x)
  return newpop

def total(season, population, count = False, virus_array = [], infection_container = []):
  count1 = 0
  count2 = 0
  infection_container = []
  move_pop(season, population)
  if season == "B":
    population = breeding(population)
  elif season == "W":
    population = winter(population)
  inf.run_infec(population)
  if count == True:
    count1, count2, infection_container = count.final_count(population, virus_array, infection_container)
  population = inf.update_infec(population)
  return population, count1, count2, infection_container
