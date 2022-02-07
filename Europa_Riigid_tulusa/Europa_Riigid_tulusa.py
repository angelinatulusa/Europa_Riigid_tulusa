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
"""
sonastik={}
file=open("riigid_pealinnad.txt",'r')
for line in file:
    k, v=line.strip().split("-")
    sonastik[k.strip()]=v.strip()

print(sonastik)
"""

riik_list=[]
pealinn_list=[]
riik_list=loe_failist("riik.txt",riik_list)
pealinn_list=loe_failist("pealinn.txt",pealinn_list)


while True:
    try:
        a=int(input("Это карта со странами и столицами, хочешь начать?(1-да, 2-нет) "))
        if a==1:
            while True:
                vopros=int(input("Что именно ты хочешь сделать?\n1 - Страна-Столица \n2 - Столица-Страна \n"))
                if vopros==1:
                    s=input("Какая страна? ")
                    s.lower()
                    strana_stolica(riik_list,pealinn_list,s)
                
        elif a==2:
            print("Ну как хочешь")
            break
        else:
            print("Что-то не так, попробуйте еще раз")

    except:
        ValueError