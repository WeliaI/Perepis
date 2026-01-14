with open('Perepis.txt') as file:
    L = file.read().split('\n')

col = 0
for i in L:
    people = i.split()
    if int(people[-1].split('.')[-1]) < 1978:
        col += 1
        print(people[0])
    
diap1 = int(input('\nВведите первое число диапозона: '))
diap2 = int(input('Введите второе число диапозона: '))
print()
for i in L:
    people = i.split()
    if diap1 < int(people[-1].split('.')[-1]) < diap2:
        print(i)