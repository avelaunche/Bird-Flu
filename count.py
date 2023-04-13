def count_infec(population):
  count = 0
  for x in population:
    if x.infection_type != "":
      count += 1
  print(count)
  return count

def count_specific_infec(population, virus):
  count = 0
  for x in population: 
    if x.infection_type == virus:
      count += 1
  return count

def count_immun(population):
  count = 0
  for x in population:
    if x.immunity_type != "":
      count += 1
  return count

def final_count(population, virus_array, infection_container):
  count1 = count_infec(population)
  count2 = count_immun(population)
  for x in range(len(virus_array)):
    count = count_specific_infec(population, virus_array[x])
    infection_container[x].append(count)
  return count1, count2, infection_container

  
