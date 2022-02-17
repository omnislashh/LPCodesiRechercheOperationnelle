U = set([1,2,3,4])
R = U
S = [set([1,2]), 
     set([1]), 
     set([1,2,3]), 
     set([1]), 
     set([3,4]), 
     set([4]), 
     set([1,2]), 
     set([3,4]), 
     set([1,2,3,4])]
w = [1, 1, 2, 2, 2, 3, 3, 4, 4]

C = []
costs = []

def findMin(S, R):
    minCost = 99999.0
    minElement = -1
    for i, s in enumerate(S):
        try:
            cost = w[i]/(len(s.intersection(R)))
            if cost < minCost:
                minCost = cost
                minElement = i
        except:
            # Division by zero, ignore
            pass
    return S[minElement], w[minElement]

while len(R) != 0:
    S_i, cost = findMin(S, R)
    C.append(S_i)
    R = R.difference(S_i)
    costs.append(cost)

print ("Cover: ", C)
print ("Total Cost: ", sum(costs), costs)

# https://stackoverflow.com/questions/7942312/how-do-i-make-my-implementation-of-greedy-set-cover-faster