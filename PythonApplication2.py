from random import *
sınad=["maja", "auto", "p‰ike", "ıhtu", "ıunad", "kala", "kool", "raamat"]
salasına=choice(sınad)
k=len(salasına)
p=6
while p>0:
    print("_ "*k)
    print(f"On j‰‰nud {p} katset")
    p-=1
    sına=input("Sisesta oma variant: ").lower()
    if len(sına)!=k:
        print(f"Sına peab olema {k} t‰hte pikk!")
        continue
    if sına==salasına:
        print("Huraa!")
        break
    else:
        print("Proovi uuesti!")
        tulemus=""
        i=0
        while i<k:
            t‰ht=sına[i]
            if t‰ht==salasına[i]:
                tulemus+=f"[{t‰ht}]"
            elif t‰ht in salasına:
                tulemus+=f"[{t‰ht}]"
            else:
                 tulemus+=f"[{t‰ht}]"
                 i+=1
                 print(tulemus)
                 k-=1
                 if k==0:
                   print(f"Kahjuks kaotasid! ’ige sına oli: {salasına}")

