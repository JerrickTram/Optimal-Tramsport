def create_lp_data_model(constraints, cont_coeffs, obj_coeffs, signs):
    data = {}
    data['constraint_coeffs'] = cont_coeffs
    data['constraints'] = constraints
    data['obj_coeffs'] = obj_coeffs
    data['num_vars'] = len(obj_coeffs)
    data['signs'] = signs
    
    def countList(lst):
        return len(lst)
    
    data['num_constraints'] = countList(cont_coeffs)
    return data

def create_ip_data_model(Destination, Origin, Demand, FixedCosts, Capacity, TransportRates):
    data = {}
    data['Destination'] = Destination
    data['Origin'] = Origin
    data['Demand'] = Demand
    data['Fixed Costs'] = FixedCosts
    data['Capacity'] = Capacity
    data['Transport Rates'] = TransportRates

    return data
    
    
         


