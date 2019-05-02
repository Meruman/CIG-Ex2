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
    return individual, neighbor

def select_individual():
#select individual to be updated you can access all Pokemon with 'setup.poke_list'
    for pokemon in setup.poke_list:
        if (pokemon.fitness >= 12):
            individual = pokemon
    return individual

def select_neighbor(neighbors):
#select one neighbor from the list neighbors
    compare=neighbors[0]
    for neighbor in neighbors:
        if (neighbor.fitness<compare.fitness):
            compare = neighbor
    return compare

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
