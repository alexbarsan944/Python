# 1. Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.
def Fibo(n):
    fibArray = [0, 1]
    for i in range(2, n):
        fibArray.append(fibArray[i - 1] + fibArray[i - 2])
    return fibArray


arr = Fibo(12)


# print(arr)

# 2. Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def prime(lis=list(), retList=list()):
    for item in lis:
        if isPrime(item):
            retList.append(item)
    return retList


# print(prime(range(100)))

# TODO
# 3. Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.
# Sa se scrie o functie care primeste ca parametru o lista de puncte
# si returneaza o lista de tuple (a,b,c) unice care reprezinta dreptele unice determinate de acele puncte
# ( (a,b,c) corespunde dreptei ax + by + c = 0).
def three(*tup: tuple()):
    def getLine(tup1: tuple(), tup2: tuple()):
        a = tup2[1] - tup1[1]
        b = tup1[0] - tup2[0]
        c = a * (tup1[0]) + b * (tup1[1])
        return a, b, c

    lst = list()
    for i in range(0, len(tup) - 1):
        for j in range(i + 1, len(tup)):
            lst.append(getLine(tup[i], tup[j]))

    return lst


# print(three((1, 2), (1, 5), (1,6), (2,9)))


# 4. Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza:
# (a intersectat cu b, a reunit cu b, a - b, b - a)

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def reunion(lst1, lst2):
    return list(set(lst1) | set(lst2))


def aMinusB(lst1, lst2, lst3=list()):
    for i in range(0, len(lst1)):
        if lst1[i] not in lst2:
            lst3.append(lst1[i])
    return lst3


def bMinusA(lst2, lst1, lst3=list()):
    for i in range(0, len(lst1)):
        if lst1[i] not in lst2:
            lst3.append(lst1[i])
    return lst3


# print(bMinusA(range(1, 10), range(5, 12)))

# 5. Sa se scrie o functie care primeste ca parametru o lista x, si un numar k.
# Sa se returneze o lista cu tuple care sa reprezinte combinari de len(x) luate cate k din lista x.
# Exemplu: pentru lista x = [1,2,3,4] si k = 3 se va returna [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)].

from itertools import combinations


def five(x: list(), k, lstRet=list()):
    comb = combinations(x, k)
    for i in (comb):
        lstRet.append(i)
    return lstRet


# print(five([1, 2, 3, 4], 3))


# 6. Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x.
# Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
# Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 se va returna [1, 2, 3]
# 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla in listele 1 si 2.
def six(k, *lst):
    elemList = []
    finalList = []
    for lists in lst:
        for elem in lists:
            elemList.append(elem)
    for i in elemList:
        if elemList.count(i) == k and i not in finalList:
            finalList.append(i)
    return finalList


# print(six(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))

# 7. Sa se scrie o functie care primeste ca parametri un numar x default egal cu 1,
# un numar variabil de siruri de caractere si un flag boolean setat default pe True.
# Pentru fiecare sir de caractere, sa se genereze o lista care sa contina caracterele care au codul ASCII divizibil cu x
# in caz ca flag-ul este setat pe True, in caz contrar sa contina caracterele care au codul ASCII nedivizibil cu x.
# Exemplu: x=2, "test", "hello", "lab002", flag=False va returna (["e", "s"], ["e", "o"], ["a"]).
# Atentie: functia trebuie sa returneze un numar variabil de liste care sa corespunda cu numarul de siruri de caractere primite ca input.
def seven(x=1, flag=True, *strings):
    finalList = []
    for word in strings:
        lst = []
        for char in word:
            if flag == True and ord(char) % x == 0:
                lst.append(char)
            elif flag == False and ord(char) % x != 0:
                lst.append(char)
        finalList.append(lst)
    return tuple(finalList)


# print(seven(2, False, "test", "hello", "lab002"))

# 8. Sa se scrie o functie care primeste un numar variabil de liste si returneaza o lista de tuple astfel:
# primul tuplu sa contina primele elemente din liste, al doilea element sa contina elementele de pe pozitia 2 din liste, etc.
# Ex: pentru listele [1,2,3], [5,6,7], ["a", "b", "c"] se va returna: [(1,5,"a"), (2,6,"b"), (3,7,"c")].
# Observatie: In cazul in care listele primite ca input nu au acelasi numar de elemente, elementele lipsa vor fi inlocuite
# cu None pentru a putea fi generate max([len(x) for x in input_lists]) tuple.

def eight(*input_lists):
    maxi = max([len(x) for x in input_lists])
    retList = []
    tups = ()

    for i in range(0, maxi):
        for tuple in input_lists:
            if i < maxi - 1:
                tups += (tuple[i],)
            else:
                tups += None,
        retList.append(tups)
        tups = ()
    print(retList)


# eight([1, 2, 3], [5, 6, 7], ["a", "b", "c", "d"])


# 9. Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter al celui de-al 2-lea element
# din tuplă. Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def nine(lst: list()):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][1][2] > lst[j][1][2]:
                aux = lst[i]
                lst[i] = lst[j]
                lst[j] = aux
    print(lst)

def nineV2(lst: list()):
    lstRet = []
    for i in sorted(lst, key=lambda x: x[1][2]):
        lstRet.append(i)
    print(lstRet)


nineV2([('abc', 'bcd'), ('abc', 'zza')])
# nine([('abc', 'bcd'), ('abc', 'zza')])
