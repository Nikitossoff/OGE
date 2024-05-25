kolvo = int(input())
list = []
for i in range(kolvo):
    i = int(input())
    if i % 6 == 0:
        list.append(i)
print(sum(list))