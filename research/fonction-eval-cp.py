from ortools.sat.python import cp_model
import numpy as np

def main():
    testsite_array = []
    # delete first 2 lines of file
    # with open('B11.txt', 'r') as fin:
    #     data = fin.read().splitlines(True)
    # with open('B11.txt', 'w') as fout:
    #     fout.writelines(data[2:])

    with open('B11.txt') as my_file:
        for line in my_file:
            line = line.rstrip('\n')
            line = line[:-1]    #delete last space
            a_list = line.split()   #replace spaced string chars with , int
            map_object = map(int, a_list)
            list_of_integers = list(map_object)
            linetab = []
            linetab+=list_of_integers 
            linetab.pop(0)  #delete unused index        
            ar = np.array(linetab)   # add each item with item0
            ar += linetab[0]
            # linetabExtract = []
            # linetabExtract = ar        
            # linetabExtract.pop(0)  # eject item0
            new_a = np.delete(ar, 0, 0)
            testsite_array.append(new_a)
            
        print(testsite_array)

    # Data
    # costs = [
    #     [90, 80, 75, 70],
    #     [35, 85, 55, 65],
    #     [125, 95, 90, 95],
    #     [45, 110, 95, 115],
    #     [50, 100, 90, 100],
    # ]
    costs = testsite_array
    num_workers = len(costs)
    num_tasks = len(costs[0])

    # Model
    model = cp_model.CpModel()

    # Variables
    x = []
    for i in range(num_workers):
        t = []
        for j in range(num_tasks):
            t.append(model.NewBoolVar(f'x[{i},{j}]'))
        x.append(t)

    # Constraints
    # Each worker is assigned to at most one task.
    for i in range(num_workers):
        model.Add(sum(x[i][j] for j in range(num_tasks)) <= num_tasks)

    # Each task is assigned to exactly one worker.
    for j in range(num_tasks):
        model.Add(sum(x[i][j] for i in range(num_workers)) == 1)

    # Objective
    objective_terms = []
    for i in range(num_workers):
        for j in range(num_tasks):
            objective_terms.append(costs[i][j] * x[i][j])
    model.Minimize(sum(objective_terms))

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Print solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f'Total cost = {solver.ObjectiveValue()}')
        
        for i in range(num_workers):
            for j in range(num_tasks):
                if solver.BooleanValue(x[i][j]):
                    print(
                        f'Worker {i} assigned to task {j} Cost = {costs[i][j]}')
    else:
        print('No solution found.')


if __name__ == '__main__':
    main()