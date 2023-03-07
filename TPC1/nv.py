def parsing(ficheiro):
    with open(ficheiro) as my_file:
        listaLinhas = my_file.readlines()
        inicio=0
        infoDict= dict()
        infoDict["idade"]      = []
        infoDict["sexo"]       = []
        infoDict["tensao"]     = []
        infoDict["colesterol"] = []
        infoDict["batimento"]  = []
        infoDict["temDoenca"]  = []
        for linha in listaLinhas:
            linha = linha[:-1]
            if(inicio==0):
                inicio +=1
                continue
            idade,sexo,tensao,colesterol,batimento,temDoenca = linha.split(',')
            infoDict["idade"].append(int(idade))
            infoDict["sexo"].append(sexo)
            infoDict["tensao"].append(int(tensao))
            infoDict["colesterol"].append(int(colesterol))
            infoDict["batimento"].append(int(batimento))
            infoDict["temDoenca"].append(int(temDoenca))
    return infoDict

def doencaSexo(infoDict):
    dictDoencaSexo = {}

    i,f,m,fTotal,mTotal =0,0,0,0,0
    for element in infoDict["sexo"]:
        if(element == "M"):
            if((infoDict["temDoenca"][i])==1):
                m +=1
            mTotal +=1
        else:
            if((infoDict["temDoenca"][i])==1):
                f +=1
            fTotal +=1
        i+=1

    dictDoencaSexo["M"]= m/mTotal *100
    dictDoencaSexo["F"]= f/fTotal *100
    return dictDoencaSexo

def doencaEtario(infoDict):
    dictEtario = {}
    idadeMin = min(infoDict['idade'])
    idadeMax =max(infoDict['idade'])
    limMin = (idadeMin//5) *5
    i=0

    while(limMin <= idadeMax):
        n,nT,i = 0,0,0
        
        limMin4 = limMin +4
        for l in infoDict['idade']:
            if(l>=limMin and l<=limMin4):
                nT +=1
                if((infoDict['temDoenca'][i])==1):
                    n+=1
            i+=1
        dictEtario[f'{limMin}-{limMin4}']= (n/nT) *100
        
        limMin +=5
    return dictEtario

def doencaColesterol(infoDict):
    dictColesterol = {}
    colMin = min([x for x in infoDict['colesterol'] if x != 0])
    colMax = max(infoDict['colesterol'])

    while(colMin <= colMax):
        n,nT,i = 0,0,0
        colMin9 = colMin +9
        for l in infoDict['colesterol']:
            if(l>=colMin and l<=colMin9):
                nT +=1
                if((infoDict['temDoenca'][i])==1):
                    n+=1
            i+=1    
        if(nT !=0):
            dictColesterol[f'{colMin}-{colMin9}'] = (n/nT) *100
        else:
            dictColesterol[f'{colMin}-{colMin9}'] = 0
        colMin +=10
    return dict

def doencaTensao(infoDict):
    dictTensao = {}
    tensaoMin = min(infoDict['tensao'])
    tensaoMax = max(infoDict['tensao'])

    while(tensaoMin <= tensaoMax):
        n,nT,i = 0,0,0
        tensaoMin4 = tensaoMin +4
        for l in infoDict['tensao']:
            if(l>=tensaoMin and l<=tensaoMin4):
                nT +=1
                if((infoDict['temDoenca'][i])==1):
                    n+=1
            i+=1    
        if(nT !=0):
            dictTensao[f'{tensaoMin}-{tensaoMin4}'] = (n/nT) *100
        else:
            dictTensao[f'{tensaoMin}-{tensaoMin4}'] = 0
        tensaoMin +=5
    return dictTensao

def doencaBatimento(infoDict):
    dictBatimento = {}
    batMin = min(infoDict['batimento'])
    batMax = max(infoDict['batimento'])

    while(batMin <= batMax):
        n,nT,i = 0,0,0
        batMin4 = batMin +4
        for l in infoDict['batimento']:
            if(l>=batMin and l<=batMin4):
                nT +=1
                if((infoDict['temDoenca'][i])==1):
                    n+=1
            i+=1    
        if(nT !=0):
            dictBatimento[f'{batMin}-{batMin4}'] = (n/nT) *100
        else:
            dictBatimento[f'{batMin}-{batMin4}'] = 0
        batMin +=5
    return dictBatimento

def print_table(data):
    # Cabeçalho da tabela
    print("--------------------------------------------------------------")
    print("| {:^15} | {:^15} |".format("Age Range", "Percentage"))
    print("--------------------------------------------------------------")
    
    # Imprimir as linhas da tabela com os dados passados
    for key, value in data.items():
        print("| {:^15} | {:^15.2f}% |".format(key, value))
        
    # Rodapé da tabela
    print("--------------------------------------------------------------")

def print_table2(data):
    print("{:<20s}{:<20s}".format("Doença", "Colesterol"))
    print("+--------------------+--------------------+")
    for key, value in data.items():
        print("|{:^20s}|{:^20f}|".format(key, value))
    print("+--------------------+--------------------+")


infoDict = parsing("myheart.csv")

# Imprime a porcentagem de homens e mulheres com doença cardíaca
print("Percentage of men and women with heart disease:")
doenca_sexo = doencaSexo(infoDict)
print_table(doenca_sexo)

# Imprime a porcentagem de pessoas com doença cardíaca por faixa etária
print("Percentage of people with heart disease by age range:")
doenca_etario = doencaEtario(infoDict)
print_table(doenca_etario)

# Imprime a porcentagem de pessoas com doença cardíaca por nível de colesterol
print("Percentage of people with heart disease by cholesterol level:")
doenca_colesterol = doencaColesterol(infoDict)
print_table2(doenca_colesterol)

# Imprime a porcentagem de pessoas com doença cardíaca por nível de pressão arterial
print("Percentage of people with heart disease by blood pressure level:")
doenca_tensao = doencaTensao(infoDict)
print_table(doenca_tensao)

# Imprime a porcentagem de pessoas com doença cardíaca por nível de batimentos cardíacos
print("Percentage of people with heart disease by heart rate level:")
doenca_batimento = doencaBatimento(infoDict)
print_table(doenca_batimento)
