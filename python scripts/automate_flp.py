# Credits to Caylie Cincera
import numpy as np
from ortools.linear_solver import pywraplp
import pandas as pd
from pulp import *


# Capacitated Facility Location Model
def CFL(data):

    # Test Script Speed
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Sets
    CUSTOMERS = data['Destination']
    FACILITY = data['Origin']

    # Parameters
    MD = data['Demand']
    demand = dict(zip(CUSTOMERS, MD))

    # Fixed Costs
    FC = data['Fixed Costs']
    actcosts = dict(zip(FACILITY, FC))

    # Maximum capacity
    Capacity = data['Capacity']
    maxam = dict(zip(FACILITY, Capacity))

    # Transportation Costs
    TransportRates = data['Transport Rates']
    transp = {i:{j:k for j,k in zip(CUSTOMERS,k)} for i,j,k in zip(FACILITY, CUSTOMERS, TransportRates)}  # {outer key: {inner key:inner value}}

    # Set Problem Variable
    prob = LpProblem('CFL', LpMinimize)

    # Decision Variables
    serv_vars = LpVariable.dicts('DestOrigin', 
                                 [(i, j) for i in CUSTOMERS 
                                         for j in FACILITY], 
                                 0)

    use_vars = LpVariable.dicts('UseLocation', FACILITY, 0, 1, LpBinary)

    # Objective Function
    prob += lpSum(actcosts[j]*use_vars[j] for j in FACILITY) + lpSum(transp[j][i]*serv_vars[(i, j)] for j in FACILITY for i in CUSTOMERS)

    # Constraints
    for i in CUSTOMERS:
        prob += lpSum(serv_vars[(i, j)] for j in FACILITY) == demand[i] # Constraint 1

    for j in FACILITY:
        prob += lpSum(serv_vars[(i, j)] for i in CUSTOMERS) <= maxam[j]*use_vars[j]

    for i in CUSTOMERS:
        for j in FACILITY:
            prob += serv_vars[(i, j)] <=  demand[i]*use_vars[j]

    # Verify Optimal Solution
    prob.solve()
    if LpStatus[prob.status] == 'Optimal':
        for v in prob.variables():
            if v.varValue == 1:
                print(f'The {v.name} site should be used for facility construction.')
            elif v.varValue == 0:
                continue
            else:
                print(f'The {v.name} route can transport {int(v.varValue)} products.')
        print(f'The minimum total annual cost is ${value(prob.objective):,.2f}.')
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
