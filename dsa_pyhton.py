# def print_items(n):
#     for i in range(n):
#         print(i)
#     for j in range (n):
#         print(j)

# print_items(10)

def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

# O(n^2)
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)

# print_items(10)

# O(n^2)+O(n) = O(n^2 + n) == O(n^2)
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
    
#     for k in range(n):
#         print (k)

# print_items(10)

#O(1)

def add_items(n):
    return n+n