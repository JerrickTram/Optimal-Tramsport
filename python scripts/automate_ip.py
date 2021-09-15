from ortools.linear_solver import pywraplp

def automate_ipMax(data):
    # Create solver with SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Decision variables
    infinity = solver.infinity()
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, infinity, 'x[%i]' % j) # NumVar computes faster than IntVar
    print(f'Number of variables = {solver.NumVariables()}')
        
    # Constraints
    for i,k in zip(range(data['num_constraints']), data['signs']):
        constraint = solver.RowConstraint(0, data['constraints'][i], '{k}')   # May have to experiment when inequalities change
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])
    print(f'Number of constraints = {solver.NumConstraints()}')
    
    # Objective Function
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMaximization()

    # Verify solution is optimal
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'Objective value = {int(solver.Objective().Value())}')
        for j in range(data['num_vars']):
            print(f'{x[j].name()} = {int(x[j].solution_value())}')
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')
        
def automate_ipMin(data):
    # Create solver with SCIP backend
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Decision variables
    infinity = solver.infinity()
    x = {}
    for j in range(data['num_vars']):
        x[j] = solver.NumVar(0, infinity, 'x[%i]' % j) # NumVar computes faster than IntVar
    print(f'Number of variables = {solver.NumVariables()}')
        
    # Constraints
    for i,k in zip(range(data['num_constraints']), data['signs']):
        constraint = solver.RowConstraint(data['constraints'][i], infinity, '{k}')   # May have to experiment when inequalities change
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])
    print(f'Number of constraints = {solver.NumConstraints()}')
    
    # Objective Function
    objective = solver.Objective()
    for j in range(data['num_vars']):
        objective.SetCoefficient(x[j], data['obj_coeffs'][j])
    objective.SetMinimization()

    # Verify solution is optimal
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(f'Objective value = {int(solver.Objective().Value())}')
        for j in range(data['num_vars']):
            print(f'{x[j].name()} = {int(x[j].solution_value())}')
        print()
        print('Problem solved in %f milliseconds' % solver.wall_time())
        print('Problem solved in %d iterations' % solver.iterations())
        print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
    else:
        print('The problem does not have an optimal solution.')
