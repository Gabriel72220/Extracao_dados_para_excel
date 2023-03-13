import pdfplumber as pdf
import os
import time
j=0
i=[0,0]
array=["Mestrado","Doutorado"]
def buscarpdf(file):
    with pdf.open(file) as tool:
        for p_no,page in enumerate(tool.pages, 1):
           
            data= page.extract_text()
            
            return data

def cacarinformacao(text,array,qtd):
    j=0
    run=True
    b=0
    tamanho= int (len(text.split()))
    quantidade=0
    while run:
        if array[j] in text.split()[b]:
            quantidade=int(text.split()[b+1])
            i[j]=i[j]+quantidade
            
        if b<tamanho-1:
            b+=1
        else:
            b=0
            j+=1
        if(j==2):
            run=False
def exclui():
    os.remove("B:/Documentos/PDF/2.pdf")
TRUE = True

arquivo = open('B:/Documentos/Programacao/Trabalho/novo-arquivo.txt', 'r')
lista = arquivo.read()
chars = "[],'"
lista = str(lista).translate(str.maketrans('', '', chars))
arquivo.close()
run1=True
while run1:
    if j<=1:
        i[j]=int(lista.split()[j])
        j+=1
    else:
        run1=False

while TRUE:
    diretorio = 'B:/Documentos/PDF/2.pdf'
    existe = os.path.exists(diretorio)
    if existe == True:
       time.sleep(2)
       text=buscarpdf("B:/Documentos/PDF/2.pdf")
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
       print(lista)
       