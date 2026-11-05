def longest_consecutive_sequence(list1):
    my_set = set(list1)
    longest = 0

    for num in my_set:
        if (num - 1) not in my_set:
            i = num
            count = 1

            while (i + 1) in my_set:
                i = i + 1
                count += 1

            if count > longest:
                longest = count

    return longest


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""