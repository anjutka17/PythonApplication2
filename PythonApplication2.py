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
      