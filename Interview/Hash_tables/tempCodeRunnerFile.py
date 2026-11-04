def subarray_sum(list_1,target):
    prefix_sum = {0:-1}
    running_sum = 0

    for index, num in enumerate(list_1):
        running_sum = num + running_sum
        req_sum = running_sum - target
        if req_sum in prefix_sum:
            return [prefix_sum[req_sum]+1,index]
        else:
            prefix_sum[running_sum] = index




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
