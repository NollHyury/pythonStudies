entrada = open("dataScience/geneticComparison/forComparison/Escherichia.fasta").read()
saida = open("dataScience/geneticComparison/resultsHtml/escherichia.html", "w")

cont = {}

colection = ['A','T','C','G']
for i in colection:
    for j in colection:
        cont[i+j] = 0



entrada = entrada.replace("\n","")


for k in range(len(entrada)-1):
    cont[entrada[k] + entrada[k+1]] += 1


i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; height:100px; color:#fff; border:1px solid#111; float:left;"+
        "background-color:rgba(0,0,0,"+str(transparencia)+");'>"+k+"</div>")

    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
    
    i+=1

saida.close()