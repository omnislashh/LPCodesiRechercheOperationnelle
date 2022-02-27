import numpy as np
from ortools.linear_solver import pywraplp
from collections import OrderedDict

## Refacto
def myFiles():
    # returns file list in array 
    with open('B11.txt') as my_file:
        myFiles = []
        for line in my_file:
            # append line in array
            myFiles.append(line)
    return myFiles

def eval(someFiles):
    testsite_array = []
    O = []
    costEdge = 0
    word_dict = {}
    openingCosts = []
    for item in someFiles:
        # delete first 2 lines of file
    # with open(item, 'r') as fin:
    #     data = fin.read().splitlines(True)
    # with open(item, 'w') as fout:
    #     fout.writelines(data[2:])

    # traitement des fichiers sources 
        with open(item) as my_file:
            for line in my_file:
                line = line.rstrip('\n')
                # line = line[:-1]    #delete last space
                a_list = line.split()   #replace spaced string chars with , int
                map_object = map(int, a_list)
                list_of_integers = list(map_object)
                linetab = []
                linetab+=list_of_integers 
                linetab.pop(0)  #delete unused index        
                                # add item0 just once at the end!
                openingCosts.append(linetab[0])
                # linetabExtract = []
                # linetabExtract = ar        
                # linetabExtract.pop(0)  # eject item0
                new_a = np.delete(linetab, 0, 0)
                testsite_array.append(new_a)
                
            print(testsite_array)
            # eval(O) : Tri des fournisseurs les mieux notés
            # Data
            # costs = [
            #     [90, 80, 75, 70],
            #     [35, 85, 55, 65],
            #     [125, 95, 90, 95],
            #     [45, 110, 95, 115],
            #     [50, 100, 90, 100],
            # ]
            costs = testsite_array
            num_suppliers = len(costs)
            num_clients = len(costs[0]) 
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
                    objective_terms.append(costs[i][j] * x[i, j])
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
                                (i, j, costs[i][j]))
                            if not i in word_dict:
                                word_dict[i] = openingCosts[i]+costs[i][j]
                            else:
                                word_dict[i] += costs[i][j]
                                # if i in dict : 
                                # add costs[i][j] to item 
                                # else dict.update(i: costs[i][j])                               
                            # additionner les coups 
                            # costEdge = costEdge + costs[i][j]
                            # if costEdge < solver.Objective().Value():
                            #     if(i not in O):  #track each cost, if current coast + coast(i) < eval(0) add i in eval
                            #         O.append(i)
                                    # append also value of i -> key value
                poids_max = sum(word_dict.values())
                # chosen?
                # poids_max = 8
                print(poids_max)
                table_triee = dict( sorted(word_dict.items(),
                            key=lambda item: item[1],
                            reverse=True))
                print(table_triee)
                O.append(table_triee)
                print(O)
    return O  

def gloutonne(table_triee, poids_max):
    poids_total = 0
    solution_gloutonne = {}
    # solution_gloutonne = []
    it=0
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
    print(solution_gloutonne)      

## Questions 1, 2 et 3
def main():
    testsite_array = []
    O = []
    costEdge = 0
    word_dict = {}
    openingCosts = []
    # delete first 2 lines of file
    # with open('B11.txt', 'r') as fin:
    #     data = fin.read().splitlines(True)
    # with open('B11.txt', 'w') as fout:
    #     fout.writelines(data[2:])

    # traitement des fichiers sources 
    with open('exemple1.txt') as my_file:
        for line in my_file:
            line = line.rstrip('\n')
            # line = line[:-1]    #delete last space
            a_list = line.split()   #replace spaced string chars with , int
            map_object = map(int, a_list)
            list_of_integers = list(map_object)
            linetab = []
            linetab+=list_of_integers 
            linetab.pop(0)  #delete unused index        
                            # add item0 just once at the end!
            openingCosts.append(linetab[0])
            # linetabExtract = []
            # linetabExtract = ar        
            # linetabExtract.pop(0)  # eject item0
            new_a = np.delete(linetab, 0, 0)
            testsite_array.append(new_a)
            
        print(testsite_array)
        # eval(O) : Tri des fournisseurs les mieux notés
        # Data
        # costs = [
        #     [90, 80, 75, 70],
        #     [35, 85, 55, 65],
        #     [125, 95, 90, 95],
        #     [45, 110, 95, 115],
        #     [50, 100, 90, 100],
        # ]
        costs = testsite_array
        num_suppliers = len(costs)
        num_clients = len(costs[0]) 
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
                objective_terms.append(costs[i][j] * x[i, j])
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
                            (i, j, costs[i][j]))
                        if not i in word_dict:
                            word_dict[i] = openingCosts[i]+costs[i][j]
                        else:
                            word_dict[i] += costs[i][j]
                            # if i in dict : 
                            # add costs[i][j] to item 
                            # else dict.update(i: costs[i][j])
                            
                        # additionner les coups 
                        # costEdge = costEdge + costs[i][j]
                        # if costEdge < solver.Objective().Value():
                        #     if(i not in O):  #track each cost, if current coast + coast(i) < eval(0) add i in eval
                        #         O.append(i)
                                # append also value of i -> key value
            poids_max = sum(word_dict.values())
            # chosen?
            # poids_max = 8
            print(poids_max)
            table_triee = dict( sorted(word_dict.items(),
                           key=lambda item: item[1],
                           reverse=True))
            print(table_triee)
            O.append(table_triee)
            print(O)
            # https://www.youtube.com/watch?v=Vw_S6X0N9TU&ab_channel=CodeAvecJonathan
            # fonction gloutonne()
            poids_total = 0
            solution_gloutonne = {}
            # solution_gloutonne = []
            it=0
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
            print(solution_gloutonne)
            # return solution_gloutonne           
            # poids_max
            # return(O)         
if __name__ == '__main__':
    main()