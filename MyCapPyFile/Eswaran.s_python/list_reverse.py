def reverse_list ( Ist ) :
    new_lst = []
    for i in range (len ( Ist ) -1, -1, -1) :
        new_lst . append ( Ist [ i ])
    #new_lst.sort(reverse= True)
    #return Ist[::-1]
    return new_lst
    
print ( reverse_list ([1 , 2 , 3 , 4 , 5]) )