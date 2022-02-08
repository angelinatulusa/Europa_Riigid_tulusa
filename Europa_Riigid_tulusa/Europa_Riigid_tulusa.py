from random import shuffle
import random
def loe_failist(f:str,s:list):
    fail=open(f,'r')
    for rida in fail:
        s.append(rida.strip())
    fail.close()
    return s

def strana_stolica(riik:list,pealinn:list,strana):
    if strana in riik:
        stolica=pealinn[riik.index(strana)]
        print(strana+"-"+stolica)
    else:
        print("Такого слова в словаре нету")

def ispravlenie(l1:list,l_1:str,l2:list,l_2:str,slovo):
    if slovo in l1:
            pravilno=l2[l1.index(slovo)]
            l1.remove(slovo)
            l2.remove(pravilno)
            print(l2, l1)
    elif slovo in l2:
            pravilno=l1[l2.index(slovo)]
            l2.remove(slovo)
            l1.remove(pravilno)
            print(l2, l1)
    l1.append(input("Введи новую страну "))
    l2.append(input("Введи новую столицу: "))
    loe_failist(l_1,l1)
    loe_failist(l_2,l2)

def kontrol(l1:list,l2:list):
    vsego_ballov=0
    lists=[]
    lists.extend(l1)
    lists.extend(l2)
    random.shuffle(lists)
    print('random list ',lists)
    for i in range(len(l2)):
        otvet=input(f"Какая страна/столица тут должна быть? '{lists[i]}': ")
        if otvet in l1 or otvet in l2:
            if lists[i] in l1:
               if l1.index(lists[i])==l2.index(otvet):
                    vsego_ballov+=1
                    print("Правильно!")
                    print()
            elif lists[i] in l2:
                if l2.index(lists[i])==l1.index(otvet):
                    vsego_ballov+=1
                    print("Правильно!")
                    print()
        else:
            print("Неправильно!")
            print()
    resultat=(vsego_ballov/len(l1))*100
    print(f"Ваш результат: {resultat}%")

riik_list=[]
pealinn_list=[]
riik_list=loe_failist("riik.txt",riik_list)
pealinn_list=loe_failist("pealinn.txt",pealinn_list)


while True:
    try:
        a=int(input("Это карта со странами и столицами, хочешь начать?(1-да, 2-нет) "))
        if a==1:
            while True:
                vopros=int(input("Что именно ты хочешь сделать?\n1 - Страна-Столица \n2 - Столица-Страна \n3 - Исправить ошибку \n4 - Контроль знаний \n"))
                if vopros==1:
                    s=[]
                    s=input("Какая страна? ")
                    strana_stolica(riik_list,pealinn_list,s)
                elif vopros==2:
                    s=[]
                    s=input("Какая столица? ")
                    strana_stolica(pealinn_list,riik_list,s)
                elif vopros==3:
                    osibka=input("Страна/столица с ошибкой:  ")
                    if osibka not in riik_list and osibka not in pealinn_list:
                        print("Такого варианта нет ")
                    else:
                        ispravlenie(riik_list,"riik.txt",pealinn_list,"pealinn.txt")
                elif vopros==4:
                    kontrol(riik_list,pealinn_list)

        elif a==2:
            print("Ну как хочешь")
            break
        else:
            print("Что-то не так, попробуйте еще раз")

    except:
        ValueError