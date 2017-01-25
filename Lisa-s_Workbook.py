
archivo = open('Lisa-s_Workbook_input.txt', 'r')

# n, k = input().split(' ')
n, k = archivo.readline().strip().split(' ') # n and k — the number of chapters and the maximum number of problems per page respectively.
n, k = [int(n),int(k)]

chapters = archivo.readline().strip().split(' ')
pages = 1
contador = 0
for x in range(n):
    max_docs = 0
    print('\n***************** chapter ', x+1, chapters[x])
    num_docs = int(chapters[x])
    for y in range(num_docs):
        if y + 1 == pages:
            print('Special doc in chapter ', x+1, 'doc: ', y + 1, 'page: ', pages)
            contador += 1
        else:
            print('Not special doc in chapter ', x+1, 'doc: ', y + 1, 'page: ', pages)

        max_docs += 1
        if max_docs == k and y < num_docs - 1:
            pages += 1
            max_docs = 0
    pages += 1
print(contador)