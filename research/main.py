import numpy as np
from ortools.linear_solver import pywraplp

clientsCosts = []
openingCosts = []
# table_triee = {}
poids_max = 0

def main():
    readFile('exemple1.txt')
    table_triee = eval(clientsCosts)
    glouton(table_triee, poids_max)

def supprLines(fileName):
    # delete first 2 lines of file (use in main if file contains additionnal lines on top)  
    with open(fileName, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(fileName, 'w') as fout:
        fout.writelines(data[2:])

def readFile(fileName):
    with open(fileName) as file:    
        for line in file:
            line = line.rstrip('\n') #remove retour à la ligne
            a_list = line.split()   #replace spaced string chars with , int
            a_list[0] != 'F'
            map_object = map(int, a_list) #conversion en integer
            list_of_integers = list(map_object) #creation d'une liste d'integer
            linetab = []
            linetab+=list_of_integers #ajout dans tableau de la liste 
            linetab.pop(0)  #delete unused index        
            openingCosts.append(linetab[0]) #on met la premiere valeur dans le tableau openingCosts
            new_a = np.delete(linetab, 0, 0)
            clientsCosts.append(new_a)
            
def eval(O):
    resultat = []
    word_dict = {}
    
    num_suppliers = len(O)
    num_clients = len(O[0]) 
    print(num_clients)
    # Solver
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Variables
    # x[i, j] is an array of 0-1 variables, which will be 1
    # if supplier i is assigned to client j.
    x = {}
    for i in range(num_suppliers):
        for j in range(num_clients):
            x[i, j] = solver.IntVar(0, 1, '')

    # Constraints
    # Each supplier is assigned to at most 1 client.
    for i in range(num_suppliers):
        solver.Add(solver.Sum([x[i, j] for j in range(num_clients)]) <= num_clients)

    # Each client is assigned to exactly one supplier.
    for j in range(num_clients):
        solver.Add(solver.Sum([x[i, j] for i in range(num_suppliers)]) == 1)

    # Objective
    objective_terms = []
    for i in range(num_suppliers):
        for j in range(num_clients):
            objective_terms.append(O[i][j] * x[i, j])
    solver.Minimize(solver.Sum(objective_terms))
    
    # Solve
    status = solver.Solve()
    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        
        print('Total clients cost = ', solver.Objective().Value(), '\n')    
        for i in range(num_suppliers):
            for j in range(num_clients):
                # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                if x[i, j].solution_value() > 0.5:
                    
                    print('supplier %d assigned to client %d.  Cost = %d' %
                        (i, j, O[i][j]))
                    if not i in word_dict:
                        word_dict[i] = openingCosts[i]+O[i][j]
                    else:
                        word_dict[i] += O[i][j]
        poids_max = sum(word_dict.values())
        # poids_max = 8
        print(poids_max)
        table_triee = dict( sorted(word_dict.items(),
                        key=lambda item: item[1],
                        reverse=True))
        print(table_triee)
    return table_triee

def glouton(table_triee, poids_max):
    # https://www.youtube.com/watch?v=Vw_S6X0N9TU&ab_channel=CodeAvecJonathan
    poids_total = 0
    solution_gloutonne = {}
    it = 0
    myKeys = list(table_triee.keys())
    print(myKeys)
    while it < len(table_triee) and poids_total < poids_max:
        # video = table_triee[it]
        poids_video = table_triee.get(myKeys[it])
        if poids_total + poids_video <= poids_max:                    
            # solution_gloutonne.append(table_triee.get(myKeys[it]))
            solution_gloutonne.update({myKeys[it]: table_triee.get(myKeys[it])})
            poids_total = poids_total + poids_video
            
            print(poids_total)
            print(it)
        it = it + 1
    # print(solution_gloutonne)

if __name__ == '__main__':
    main()