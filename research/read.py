import numpy as np
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
        linetabExtract = []
        linetabExtract = ar        
        # linetabExtract.pop(0)  # eject item0
        testsite_array.append(ar)
        
print(testsite_array)