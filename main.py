import time
import os

def encryption():#зашифровывает текст находящийся в папке
    sings = ['!', ',', '.', '\"', '\'', ';', ':', '?', '\n', ' ', '(', ')', '[', ']', '{', '}']
    print("Текст лежащий в папке 'encryption.txt' будет зашифрован.")
    indent = int(input("Введите отступ, с которым будет проводиться шифрование >>> "))
    f = open('encryption.txt', 'r', encoding = 'utf8')
    name = input("Введите имя файла куда будет сохранён зашифрованный тескт (exemole.txt)>>> ")
    if name[-4:-1] != '.txt':
        name += '.txt'
    w = open(name, 'w', encoding = 'utf8')
    for line in f:
        for i in line:
            if i in sings:
                w.write(i)
            else:
                w.write(chr(ord(i.lower()) + indent))



def decryption():
    sings = ['!', ',', '.', '\"', '\'', ';', ':', '?', '\n', ' ', '(', ')', '[', ']', '{', '}']
    print("Текст лежащий в папке 'decryption.txt' будет рашифрован.")
    sing = {}
    f = open('decryption.txt', 'r', encoding = 'utf8')
    name = input("Введите имя файла куда будет сохранён расшифрованный тескт (example)>>> ")


    for line in f:
        for i in line:
            if i not in sings:
                sing[i.lower()] = sing.get(i.lower(), 0) + 1
    key_max = list()
    key_max.append('a')
    sing['a'] = sing.get('a', 0) + 0
    f.close()

    for key in sing:
        if sing[key] > sing[key_max[0]]:
            key_max.clear()
            key_max.append(key)
        elif sing[key] == sing[key_max[0]]:
            key_max.append(key)
    indent = list()
    for i in key_max:
        indent.append(ord('e') - ord(i))

    for i in indent:
        f = open('decryption.txt', 'r', encoding='utf8')
        k = 1
        w = open(name + str(k) + '.txt', 'w', encoding='utf8')
        for line in f:
            for j in line:
                if j in sings:
                    w.write(j)
                else:
                    w.write(chr(ord(j.lower()) + i))
        k += 1
        f.close()










print("Привет, это программа по шифрованию и дешифрованию текстов с помощью шифра цезаря!")
while True:
    answer = int(input("Введите что вы хотите сделать (1 - зашифровать; 2 - дешифровать) >>> "))
    if answer == 1:
        encryption()
        break
    elif answer == 2:
        decryption()
        break
    else:
        print("Такого варианта работы программы нет!\nПопробуй ещё раз!")
        time.sleep(1)
        os.system('cls||clear')
