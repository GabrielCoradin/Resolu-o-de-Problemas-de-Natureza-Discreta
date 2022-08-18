#ler arquivo
arquivo = open("tarefa-1_1.txt", "r")
#manipulacoes para colocar em matriz
vet1 = []
matriz1 = []
vet1 = arquivo.readlines()
#identificacao de simbolos
simb = ['U','I','D','C']

#for para preencher a matriz
for i in range(len(vet1)):     
    matriz1.append(vet1[i].split())

#for para caminhar na matriz e fazer a identificacao dos simbolos
for l in range(len(matriz1)):
        if matriz1[l][0] in simb:
            calculo = matriz1[l][0]

            #identificar uniao
            if calculo == 'U':
                conjU1 = matriz1[l+1]
                conjU1_1 = [] #vetor para formatacao
                conjU2 = matriz1[l+2]
                conjU2_1 = [] #vetor para formatacao
                uniao = conjU1 #variavel para guardar o primeiro conjunto e posteriormente realizar a uniao do segundo conjunto, antes da formatacao final
                uniaofinal = [] #resultado final com formatacao pedida

                #for para realizar a operacao de uniao
                for conj in conjU2:
                    if conj not in conjU1:
                        uniao.append(conj)

                #loop para realizar a formatacao necessaria   
                for i in range(len(conjU2)):
                    lista = conjU2[i]
                    retirar_virgula = lista.replace(",","")
                    conjU2_1.append(retirar_virgula)

                #loop para realizar a formatacao necessaria   
                for i in range(len(conjU1)):
                    lista = conjU1[i]
                    retirar_virgula = lista.replace(",","")
                    conjU1_1.append(retirar_virgula)        

                #loop para retirar virgulas do resultado
                for i in range(len(uniao)):
                    lista = uniao[i]
                    retirar_virgula = lista.replace(",","")
                    uniaofinal.append(retirar_virgula)

                print("Uniao: "
                "Conjunto 1: {", ','.join(conjU1_1), "}",
                "Conjunto 2: {", ','.join(conjU2_1), "}", 
                "Resultado: {", ','.join(uniaofinal), "}") #comando .join para retira "[]" e adicionar ","

            #identificar intersecao
            elif calculo == 'I':
                conjI1 = matriz1[l+1]
                conjI1_1 = [] #vetor para formatacao
                conjI2 = matriz1[l+2]
                conjI2_1 = [] #vetor para formatacao
                intersecao = [] #vetor para guardar o resultado antes da formatacao final
                intersfinal = [] #resutado final com formatacao pedida

                #for para realizar a operacaode intersecao
                for inters in conjI1:
                    if inters in conjI2:
                        intersecao.append(inters)

                #loop para realizar a formatacao necessaria   
                for i in range(len(conjI1)):
                    lista = conjI1[i]
                    retirar_virgula = lista.replace(",","")
                    conjI1_1.append(retirar_virgula)

                #loop para realizar a formatacao necessaria   
                for i in range(len(conjI2)):
                    lista = conjI2[i]
                    retirar_virgula = lista.replace(",","")
                    conjI2_1.append(retirar_virgula)
                
                #loop para retirar virgulas do resultado
                for i in range(len(intersecao)):
                    lista = intersecao[i]
                    retirar_virgula = lista.replace(",","")
                    intersfinal.append(retirar_virgula)

                print("Interseção: "
                "Conjunto 1: {", ','.join(conjI1_1), "}",
                "Conjunto 2: {", ','.join(conjI2_1), "}",
                "Resultado: {", ','.join(intersfinal), "}")   #comando .join para retira "[]" e adicionar ","

            #identificar diferenca
            elif calculo == 'D':
                conjD1 = matriz1[l+1]
                conjD1_1 = [] #vetor para formatacao
                conjD2 = matriz1[l+2]
                conjD2_1 = [] #vetor para formatacao
                diferenca = []#vetor para guardar o resultado antes da formatacao final
                diferencafinal = [] #resultado final com formatacao pedida
                
                #for para realizar a operacao de diferenca
                for difer in conjD1:
                    if difer not in conjD2:
                        diferenca.append(difer)

                #loop para realizar a formatacao necessaria   
                for i in range(len(conjD1)):
                    lista = conjD1[i]
                    retirar_virgula = lista.replace(",","")
                    conjD1_1.append(retirar_virgula)

                #loop para realizar a formatacao necessaria   
                for i in range(len(conjD2)):
                    lista = conjD2[i]
                    retirar_virgula = lista.replace(",","")
                    conjD2_1.append(retirar_virgula)           
                
                #loop para retirar virgulas do resultado
                for i in range(len(diferenca)):
                    lista = diferenca[i]
                    retirar_virgula = lista.replace(",","")
                    diferencafinal.append(retirar_virgula)        

                print("Diferença: "
                "Conjunto 1: {", ','.join(conjD1_1), "}", 
                "Conjunto 2: {", ','.join(conjD2_1), "}", 
                "Resultado: {", ','.join(diferencafinal), "}")   #comando .join para retira "[]" e adicionar ","

            #identificar cartesiano
            elif calculo == 'C':
                conjC1 = matriz1[l+1]
                conjC1_1=[] #vetor para formatacao
                conjC2 = matriz1[l+2]
                conjC2_1=[] #vetor para formatacao
                cartesiano = [] #vetor para guardar o resultado antes da formatacao final
                cartesianofinal = []  #resultado final com formatacao pedida

                #loop para realizar a formatacao necessaria                
                for i in range(len(conjC2)):
                    lista = conjC2[i]
                    retirar_virgula = lista.replace(",","")
                    conjC2_1.append(retirar_virgula)

                #loop para realizar a formatacao necessaria                 
                for i in range(len(conjC1)):
                    lista = conjC1[i]
                    retirar_virgula = lista.replace(",","")
                    conjC1_1.append(retirar_virgula)    
                
                #for para realizar a operacao de cartesiano
                for x in conjC1:
                    for y in conjC2_1:
                        if (x+y) not in cartesiano:
                            cartesiano.append(x+y)          
                
                print("Cartesiano: "
                "Conjunto 1: {", ','.join(conjC1_1), "}", 
                "Conjunto 2: {", ','.join(conjC2_1), "}", 
                "Resultado: {", "("+ ');('.join(cartesiano)+ ")", "}")  #comando .join para retira "[]" e adicionar ");("