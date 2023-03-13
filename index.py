import pdfplumber as pdf
import os
import time
j=0
i=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
array=["000001","000002","000003","000004","000005","000008","000009","000010","000011","000012","000013","000014","000016","000018","000019","000020","000021","000022","000023","000025","000098","000099","000052","000053","000054","000055","000056","000057","000058","000059","000060","000061","000062","000063","000064","000065","000066","000067","000068","000069","000070","000071","000072","000073","000149","000150","000151","000152","000103"]
def buscarpdf(file):
    with pdf.open(file) as tool:
        for p_no,page in enumerate(tool.pages, 1):
           
            data= page.extract_text()
            
            return data

def cacarinformacao(text,array,qtd):
    j=0
    run=True
    b=0
    aux=0
    tamanho= int (len(text.split()))
    quantidade=0
    while run:
        if array[j] in text.split()[b]:
          if len(array[j]) == len(text.split()[b]): 
           run2=True
           aux=b
           while run2: 
            if("UNI" in text.split()[aux]):
                quantidade=int(text.split()[aux-1])
                i[j]=i[j]+quantidade
                run2=False
            else:
                aux+=1
            
        if b<tamanho-1:
            b+=1
        else:
            b=0
            j+=1
        if(j==48):
            run=False
def exclui():
    os.remove("C:/Users/Usuario/Documents/Extracao_dados_para_excel-main/2.pdf")
TRUE = True
j=0
arquivo = open('novo-arquivo.txt', 'r')
lista = arquivo.read()
chars = "[],'"
lista = str(lista).translate(str.maketrans('', '', chars))
arquivo.close()
run1=True
while run1:
    if j<=46:
        i[j]=int(lista.split()[j])
        j+=1
    else:
        run1=False

while TRUE:
    diretorio = 'C:/Users/Usuario/Documents/Extracao_dados_para_excel-main/2.pdf'
    existe = os.path.exists(diretorio)
    if existe == True:
       time.sleep(2)
       text=buscarpdf("C:/Users/Usuario/Documents/Extracao_dados_para_excel-main/2.pdf")
       cacarinformacao(text,array,i)
       exclui()
       
       arquivo = open('novo-arquivo.txt', 'w')
       arquivo.write(str(i))
       arquivo.close()
       arquivo = open('novo-arquivo.txt', 'r')
       lista = arquivo.read()
       chars = "[],'"
       lista = str(lista).translate(str.maketrans('', '', chars))
       arquivo.close()
       
       