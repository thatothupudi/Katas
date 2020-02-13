def Combination(sequence1=[], sequence2=[]):
    num = len(sequence1)
    store_list = []
    for row in range(num):
        store_list.append(sequence1[row])
        store_list.append(sequence2[row])
    
    return store_list

combined_list = Combination([11,22,33],  [1,2,3])
print(combined_list)
    
