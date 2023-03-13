import pdfplumber as pdf
import os
j=0
tam=1
array=["Mestrado","Doutorado"]
i=[0,0]
arquivo = open('B:/Documentos/Programacao/Trabalho/novo-arquivo.txt', 'r')
lista = arquivo.read()
chars = "[],'"
lista = str(lista).translate(str.maketrans('', '', chars))
arquivo.close()
print(len(lista.split()))
run=True
while run:
    if j<=1:
        i[j]=int(lista.split()[j])
        j+=1
    else:
        run=False
run=True
resultado=0
while run:
    x=input(" 1- Ver Quantidade Total de salgados vendidos\n 2- ver quantidade vendida de cada salgado\n 3- ver salgados vendidos no atacado\n 4- Zerar Tabela\n 0- fechar ")
    if int(x)==0:
       run=False
    if int(x)==1:
       j=0
       while j<=tam:
           resultado+=int(i[j]) 
           j+=1
       print("Foram Vendidos:",int(resultado) ,"Salgados")
    if int(x)==2:
       j=0
       while j<=tam:
        print(array[j],":",i[j])
        j+=1
    if int(x)==3:
       print("EM desenvolvimento")
    if int(x)==4:
       j=0
       while j<=tam:
         i[j]=0 
         j+=1
       arquivo = open('B:/Documentos/Programacao/Trabalho/novo-arquivo.txt', 'w')
       arquivo.write(str(i))
       arquivo.close()
       