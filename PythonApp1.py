ik=''
while len(ik) !=11 or ik.isdigit()!=True:
    try:
        ik=input('Введите свой isikukood: ')
    except ValueError:
        print('Неверно введен isikukood.')
print('Анализ isikukood:'.center(50,'-'))
print('Первый символ:')
ik_list=list(ik)
if int(ik_list[0]) not in [1,2,3,4,5,6]:
    print(ik_list[0],' - неправильно')
else:
    print(ik_list[0],' - правильно')
    kuu=ik_list[3]+ik_list[4]
    kuu=int(kuu)
    if kuu>0 and kuu<13:
        print(ik_list[3],ik_list[4], 'Правильный месяц!')
        paev=int(ik_list[5]+ik_list[6])
        #1,3,5,7,8,10,12 31 päev
        #2,4,6,9,11 28-29,30 päeva
        #1,2 - '18', 3,4 - '19', 5,6 - '20' +ik_list[1]+ik_list[2]
        if int(ik_list[0])==1 or int(ik_list[0])==2:
            aasta=int('18'+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==3 or int(ik_list[0])==4:
            aasta=int('19'+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==5 or int(ik_list[0])==6:
            aasta=int('20'+ik_list[1]+ik_list[2])

        if kuu in [1,3,5,7,8,10,12] and paev>0 and paev<32:
            print(ik_list[5],ik_list[6], 'Правильный день!')
        elif (kuu in [4,6,9,11] and paev>0 and paev<31) or (kuu==2 and paev>0 and paev<29):
            print(ik_list[5],ik_list[6], 'Правильный день!')
        elif aasta % 4==0 and kuu ==2 and paev>0 and paev<30:
            print(ik_list[5],ik_list[6], 'Правильный день! 29 февраля.')
        else:
            print(ik_list[5],ik_list[6], 'Неправильный день!')
    else:
        print(ik_list[3],ik_list[4], 'Неправильный месяц!')
#год ik_list[1],ik_list[2]
#месяц ik_list[3],ik_list[4]
#число ik_list[5],ik_list[6]
Summa=0
for i in range(1,11):
    if i<10:
        Summa+=i*int(ik_list[i-1])
    else:
        Summa+=(i-9)*int(ik_list[i-1])
print('Summa: ',Summa)
jaak=Summa//11
if jaak==10:
    Summa=0
    for i in range(3,13):
        if i<=9:
            Summa+=i*int(ik_list[i-1])
        else:
            Summa+=(i-9)*int(ik_list[i-1])
    jaak=Summa//11
jaak=Summa-jaak*11
print('Kontrollnumber: ',jaak)
if jaak==int(ik_list[10]):
    print('Isikukood правильный!')
else:
    print('Isikukood неправильный!')
