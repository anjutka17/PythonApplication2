from random import *
s�nad=["maja", "auto", "p�ike", "�htu", "�unad", "kala", "kool", "raamat"]
salas�na=choice(s�nad)
k=len(salas�na)
p=6
while p>0:
    print("_ "*k)
    print(f"On j��nud {p} katset")
    p-=1
    s�na=input("Sisesta oma variant: ").lower()
    if len(s�na)!=k:
        print(f"S�na peab olema {k} t�hte pikk!")
        continue
    if s�na==salas�na:
        print("Huraa!")
        break
    else:
        print("Proovi uuesti!")
        tulemus=""
        i=0
        while i<k:
            t�ht=s�na[i]
            if t�ht==salas�na[i]:
                tulemus+=f"[{t�ht}]"
            elif t�ht in salas�na:
                tulemus+=f"[{t�ht}]"
            else:
                 tulemus+=f"[{t�ht}]"
                 i+=1
                 print(tulemus)
                 k-=1
                 if k==0:
                   print(f"Kahjuks kaotasid! �ige s�na oli: {salas�na}")

