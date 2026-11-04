def group(list1):
    my_dict = {}

    for i in list1:
        key = "".join(sorted(i))

        if key in my_dict:
            my_dict[key].append(i)
        else:
            my_dict[key] = [i]

    return list(my_dict.values())


test_1 = group(["eat", "tea", "tan", "ate", "nat", "bat"])
print(test_1)



test_1 = group(["eat", "tea", "tan", "ate", "nat", "bat"])

word = "eat"
print(sorted(word))

word_2 = "ate"
print(sorted(word))

print(test_1)