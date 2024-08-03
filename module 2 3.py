my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for num in my_list:
    if num > 0:
        print(num)
    elif num == 0:
        continue
    else:
        var = num < 0
        break
