U = set([1,2,3,4,5,6,7,8])
R = U
S = [set([5,3,4,7,10,10,5,3]), 
     set([2,0,1,4,7,13,8,6]), 
     set([10,8,10,13,10,5,0,2]), 
     set([11,9,7,4,2,3,8,11])]
w = [8, 15, 7, 6]

C = []
costs = []

def findMin(S, R):
    minCost = 50
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