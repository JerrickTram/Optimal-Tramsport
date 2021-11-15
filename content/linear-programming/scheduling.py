import pandas as pd
from pulp import *
import matplotlib.pyplot as plt
from itertools import chain, repeat

def WarehouseStaffing(constraints):
  def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))
  
  # Staff Needs Per Day
  n_staff = constraints
  
  # Days of Week
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
  # Circular list of days
  n_days = [i for i in range(7)]
  n_days_c = list(ncycles(n_days, 3))
  
  # Working days
  list_in = [[n_days_c[j] for j in range(i, i + 5)] for i in n_days_c]
  
  # Workers off by shift for each day
  list_excl = [[n_days_c[j] for j in range(i + 1, i + 3)] for i in n_days_c]
  
  ## Initialize Model, Define Objective Function, and Add Constraints
  # Initialize Model
  model = LpProblem('Minimize Staffing', LpMinimize)
  
  # Create Decision Variables
  start_days = ['Shift: ' + i for i in days]
  x = LpVariable.dicts('shift', n_days, lowBound = 0, cat = 'Integer' )
  
  # Define Objective Function
  model += lpSum(x[i] for i in n_days)
  
  # Add Constraints
  for d, l_excl, staff in zip(n_days, list_excl, n_staff):
    model += lpSum([x[i] for i in n_days if i not in l_excl]) >= staff
  
  ## Solve Model and Analyze Results
  # Solve Model
  model.solve()
  
  # Status of Solution
  print(f'Status: {LpStatus[model.status]}.')
  
  # How many workers per day?
  dct_work = {}
  for v in model.variables():
      dct_work[int(v.name[-1])] = int(v.varValue)
    
  # Show Detailed Sizing per Day
  dict_sch = {}
  for day in dct_work.keys():
      dict_sch[day] = [dct_work[day] if i in list_in[day] else 0 for i in n_days]
  df_sch = pd.DataFrame(dict_sch).T
  df_sch.columns = days
  df_sch.index = start_days
  
  # Optimized Objective Value
  print(f'Total number of staff: {value(model.objective)}.')
  print(df_sch)
  
staffing = [99, 78, 57, 50, 55, 87, 52]
  
WarehouseStaffing(staffing)
