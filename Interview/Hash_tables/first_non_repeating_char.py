def first_non_repeating_char(string):
    my_dict = {}
    sort_1 = []
    sort_2 = []
    for i in string:
       if i in my_dict:
           sort_1.append(i)
       else:
            my_dict[i] = True
    
    for j in my_dict:
        if j not in sort_1:
            sort_2.append(j)

    if not sort_2:
        return None
    
    return sort_2[0]

           





print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""