n_tiket=abs(int(input('Введите количество посетителей = ')))

List_age = list(map(int, input(f'введите возраст посетителей через запятую, всего {n_tiket} билетов = ').split(',')))
print(List_age)

summ = 0
for i in List_age :

 if i < 18:
    summ += 0

 elif 18<=i<=25:
     summ += 990

 elif 25<i :
     summ += 1390

 if n_tiket > 3 :
     summ *= 0.9

print(summ)