#Birth- death update

import setup

import random

#Your Implementation of Update Rules goes here

def update_rule():
#select individual and neighbor and return them. If no one shall be updated return None
    individual = select_individual()
    neighbor = None
    if(individual != None):
      neighbors = get_neighbors(individual)
      neighbor = select_neighbor(neighbors)
      
      #------------Imitation------------#
      #if (neighbor.fitness > individual.fitness):
      #  return individual, neighbor
      #else:
      #  return None,None
      #----------------------------------#

#--------------- BD -----------------#
  
  #def select_individual():
#    Hpokemon =[]
#    for pokemon in poke_list:
 #       if (pokemon.fitness >= BREEDING_FITNESS):
  #          Hpokemon.append(pokemon)
   # RChoose=random.randint(0,len(Hpokemon)-1)
        
    #return Hpokemon[RChoose]

#def select_neighbor(neighbors):
 #   rand = random.randint(0,len(neighbors)-1)
  #  return neighbors[rand]
#------------------------------------------#  


#----------------DB-----------------------#
#def select_individual():
 #   RChoose=random.randint(0,len(poke_list)-1)
        
  #  return poke_list[RChoose]

#def select_neighbor(neighbors):
 #   compare=neighbors[0]
  #  for neighbor in neighbors:
   #     if (neighbor.fitness>compare.fitness):
    #        compare = neighbor
    #return compare
#-----------------------------------------#
  
#----------------Imitation----------------#
def select_individual():
    RChoose=random.randint(0,len(poke_list)-1)  
    return poke_list[RChoose]

def select_neighbor(neighbors):
    compare=neighbors[0]
    for neighbor in neighbors:
        if (neighbor.fitness>compare.fitness):
            compare = neighbor
    return compare
#------------------------------------------#

def get_neighbors(individual):
#returns a list of Pokemon who are neighbors of the Pokemon individual
    neighbors = []
    column = int(individual.grid_id % setup.columns)
    row = int(individual.grid_id / setup.columns)
    #left neighbor
    if (row * setup.columns + column - 1) >= 0 and (row * setup.columns + column - 1) <= setup.columns*setup.rows-1 and column != 0:
        neighbors.append(setup.poke_list[row * setup.columns + column - 1])
    #right neighbor
    if (row * setup.columns + column + 1) >= 0 and (row * setup.columns + column + 1) <= setup.columns*setup.rows-1 and column != (setup.columns - 1):
        neighbors.append(setup.poke_list[row * setup.columns + column + 1])
    #upper neighbor
    if ((row - 1) * setup.columns + column) >= 0 and ((row - 1) * setup.columns + column) <= setup.columns*setup.rows-1:
        neighbors.append(setup.poke_list[(row - 1) * setup.columns + column])
    #lower neighbor
    if ((row + 1) * setup.columns + column) >= 0 and ((row + 1) * setup.columns + column) <= setup.columns*setup.rows-1:
        neighbors.append(setup.poke_list[(row + 1) * setup.columns + column])
    return neighbors
