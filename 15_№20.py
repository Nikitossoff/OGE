kolvo = int(input())
list = []
for i in range(kolvo):
    i = int(input())
    if i % 5 == 0:
        list.append(i)
print(max(list))