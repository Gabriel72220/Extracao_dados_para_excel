import pdfplumber as pdf
import os
j=0
#22 salgados
#26 refri
#18
tam_salgados=21
tam_refri=47
array=["Croassaint misto","coxinha","empada","pastel forno","pao batata frango","pao de batata misto","esfiha mista","esfiha carne","esfiha mistao","esfiha queijo","croassaint queijo","croassaint frango","quiche","enroladinho","doguinho","hamburgue","kibe","coracao","beirute","esfiha frango","almofada","esfiha calabresa","coca lata","coca 250ml","coca 1L","coca 600ml","refri laranja","refri cola","pepsi 1l","pepsi 2l","pepsi lata","pepsi twist","pepsi black","cajuina 250ml","cajuina 1l","cajuina 2l","guarana lata","guarana 1l","fanta 250","fanta 2l","agua","agua com gas","citrus","pepsi 250ml","suco","fanta lata maracuja","fanta lata laranja","guarana kuat 1l","refri guarana"]

i=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
arquivo = open('C:/Users/Usuario/Documents/Extracao_dados_para_excel-main/novo-arquivo.txt', 'r')
lista = arquivo.read()
chars = "[],'"
lista = str(lista).translate(str.maketrans('', '', chars))
arquivo.close()
print(len(lista.split()))
run=True
while run:
    if j<=46:
        i[j]=int(lista.split()[j])
        j+=1
    else:
        run=False
run=True
resultado=0
while run:
    x=input(" 1- Ver Quantidade Total de salgados vendidos\n 2- ver quantidade vendida de cada salgado\n 3- ver total de bebidas vendidas\n 4- ver lista de bebidas vendidas \n 5- Zerar Tabela\n 6- Beirute \n 0- fechar ")
    if int(x)==0:
       run=False
    if int(x)==1:
       j=0
       resultado=0
       while j<=tam_salgados:
           resultado+=int(i[j]) 
           j+=1
           if j==18:
              j+=1
       print("Foram Vendidos:",int(resultado) ,"Salgados")
    if int(x)==2:
       j=0
       while j<=tam_salgados:
        print(array[j],":",i[j])
        j+=1
        if j==18:
          j+=1

    if int(x)==3:
       j=22
       resultado=0
       while j<=tam_refri:
           resultado+=int(i[j]) 
           j+=1
       print("Foram Vendidos:",int(resultado) ,"Bebidas")
    
    if int(x)==4:
       j=22

       while j<=tam_refri:
        print(array[j],":",i[j])
        j+=1
    if int(x)==5:
       j=0
       while j<=47:
         i[j]=0 
         j+=1
       arquivo = open('C:/Users/Usuario/Documents/Extracao_dados_para_excel-main/novo-arquivo.txt', 'w')
       arquivo.write(str(i))
       arquivo.close()
    
    if int(x)==6:
        print(array[18],":",i[18])