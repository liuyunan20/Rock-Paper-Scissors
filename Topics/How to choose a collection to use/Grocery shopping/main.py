shopping_list = input().split()
shopping_dict = {}
for item in shopping_list:
    shopping_dict.setdefault(item, 0)
    shopping_dict[item] += 1
for key in shopping_dict:
    print(shopping_dict[key], key)
