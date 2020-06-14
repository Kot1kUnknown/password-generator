# -*- coding:utf -8 -*-
#!/usr/bin/python3
import random as r

simvoli = '=+#@*&^%~qwertyuiopasdfghjklzxcvbnm,.1234567890QWERTYUIOPASDFGHJKLZXCVBNM<>:;"!?/{}[]`'


#Сам генир, изи просто))
skolko = int(input('Введите колличество паролей: '))
dlina = int(input('Введите длину паролей(я): '))
for n in range(skolko):
    passw =''
    for i in range(dlina):
        passw += r.choice(simvoli)
    print(passw)
