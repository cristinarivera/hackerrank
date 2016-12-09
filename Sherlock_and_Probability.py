def calcularmcd(countTot, countYes):
    if countTot == 0:
        return 1
    if countYes > 0:
        resto = countTot % countYes
        if (countYes, resto) in lista:
            return lista.get((countYes, resto))
        else:
            mcd = calcularmcd(countYes, resto)
            lista[(countYes, resto)] = mcd
            return mcd
    else:
        return countTot


def partir(s):
    inic = s.find(' ')
    return int(s[:inic]), int(s[inic + 1:])


archivo = open('Sherlock_and_Probability_input.txt', 'r')

t = int(archivo.readline())  ## número de
lista = dict()

for n in range(t):
    countYes = 0
    countTot = 0
    s = archivo.readline()
    N, K = partir(s)
    cadena = archivo.readline()
    for i in range(N):
        countTot += N
        if cadena[i] is '1':
            for j in range(N):
                if cadena[j] is '1':
                    if i > j:
                        dif = i - j
                    else:
                        dif = j - i
                    if dif <= K:
                        countYes += 1

    if (countTot, countYes) in lista:
        mcd = lista.get((countTot, countYes))
    else:
        mcd = calcularmcd(countTot, countYes)
        lista[(countTot, countYes)] = mcd
    if mcd is 1:
        print(countYes, '/', countTot, sep='')
    else:
        print(countYes // mcd, '/', countTot // mcd, sep='')

archivo.close()