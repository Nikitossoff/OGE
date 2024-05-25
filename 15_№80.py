kolvo = int(input())
list = []
for i in range(kolvo):
    i = int(input())
    if i % 3 == 0:
        list.append(i)
print(min(list))