count = 0
for i in range(0,999):
    i = int(input())
    if i != 0:
        if i % 2 == 0:
            if i % 9 == 0:
                count +=1          
    else:
        break
print(count)