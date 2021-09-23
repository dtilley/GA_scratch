"""DEAP tutorial based on fitting a polynomial of unknown coefficients
to a natural process governed by a cubic equation."""

import numpy as np
#import array as arr
import pandas as pd
#import matplotlib.pyplot as plt
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

###########  This models the natural process.       ########
##    This underlying process is not known to the GA      ##
## I think of x as a membrane voltage and y as current    ##


def nat_process(x):
    y = 5.0*x**0 + 1.3*x**1 + 1.9*x**2 + 4.2*x**3
    return y


def sample_natpro(x):
    # A noise term is added to determine noise sensitivity
    y_real = nat_process(x) + np.random.normal(loc=0, scale=0.25, size=len(x))
    return y_real


x = np.arange(-3.0, 3.1, 0.1)
y = sample_natpro(x)
fit_data = {'x': x, 'y': y}
del x, y
fit_data = pd.DataFrame(fit_data)

###########  End of  natural process.       ########

##  Define classes for the GA with DEAP libaries ###


"""Defines a fitness class called FitnessMin.
FitnessMin inherits from the base.Fitness object."""
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

"""Define Individual: Uses the creator library to define an
object called Individual that inherits from np.ndarray."""
creator.create("Individual", np.ndarray, fitness=creator.FitnessMin, strategy=None)

"""Define Strategy: Uses the creator library to define an
object called Strategy containing a ndarray."""
creator.create("Strategy", np.ndarray)

##  End class creation of FitnessMin, Individual, Strategy ##


"""Define some DEAP functions to generate individuals."""
def generateES(ind_clss, strg_clss, size):
    ind = ind_clss(np.random.normal(size=size))
    ind.strategy = strg_clss(np.random.normal(size=size))
    return ind


# Create toolbox
toolbox = base.Toolbox()
IND_SIZE = 5

toolbox.register("individual", generateES, creator.Individual, creator.Strategy, IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


"""Define functions to evaluate individual models."""


def run_individual(ind, x):
    # The inductive bias in this GA is that the natural process is governed
    #  by a polynomial of the 4th degree or less.
    y = ind[0]*x**0 + ind[1]*x**1 + ind[2]*x**2 + ind[3]*x**3 + ind[4]*x**4
    return y


def fitness(ind, fit_data):
    y_ind = run_individual(ind, fit_data.x)
    mse = ((sum((y_ind - fit_data.y)**2))/float(len(fit_data.y)),)
    return mse


# Register the fitness function in the toolbox.
# The 'evaluate' is a DEAP keyword for determining fitness.
toolbox.register("evaluate", fitness, fit_data=fit_data)


"""Register some ES functions to the toolbox.
The 'mate', 'mutate', and 'select' are keyword functions
in DEAP."""
toolbox.register("mate", tools.cxESBlend, alpha=0.1)
toolbox.register("mutate", tools.mutESLogNormal, c=1.0, indpb=0.3)
toolbox.register("select", tools.selTournament, tournsize=3)


"""Register some statistical functions to the toolbox."""
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)

hof = tools.HallOfFame(1, similar=np.array_equal) # Keep the best (1) individual

#######   Run the GA   #######
MU = 4
LAMBDA = 8
pop = toolbox.population(n=MU)

pop, logbook = algorithms.eaMuCommaLambda(pop, toolbox, mu=MU, lambda_=LAMBDA,
                                          cxpb=0.6, mutpb=0.3, ngen=10, stats=stats,
                                          halloffame=hof, verbose=False)
