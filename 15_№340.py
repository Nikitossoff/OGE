list = []
for i in range(0,999):
    i = int(input())
    if i != 0:
        if i % 6 == 0:
            r = i - 4 
            if r % 5 == 0:
                list.append(i)
    else:
        break
print(sum(list))