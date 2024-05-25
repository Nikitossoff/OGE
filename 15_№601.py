list = []
for i in range(0,999):
    i = int(input())
    if i != 0:
        if i % 7 == 0:
            r = i - 2 
            if r % 10 == 0:
                list.append(i)
    else:
        break
print(sum(list))