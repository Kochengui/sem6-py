a1=int(input('введите 1 элемент: '))
d=int(input('введите разность : '))
n=int(input('введите количество элементов'))
for i in range(n):
    an = a1 + i * d
    print(an,end=' ')
    
list=[int(i) for i in input('введите числа : ').split()]
max_index=int(input('введите макчимальное значение: '))
min_index=int(input('введите минимальное значение: '))
for i in range(len(list)):
    if list[i]<max_index and list[i]>min_index:
        print(i)