#Utilizando o Colaboratory

#features (1 sim, 0 não)
#pelo longo?
#perna curta?
#faz auau?


#var
porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1 , 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# 1 => porco, 0 => cachorro

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classe = [1,1,1,0,0,0]

from sklearn.svm import LinearSVC 

model = LinearSVC()
model.fit (dados, classe)

animal_misterioso =[1,1,1]
model.predict ([animal_misterioso])


misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

teste = [misterio1, misterio2, misterio3]
previsoes = model.predict (teste)

teste_classe = [0,1,1]


corretos = (previsoes == teste_classe).sum()
total = len(teste)
taxa_de_acerto = corretos/total
print ("Taxa de acerto: ", taxa_de_acerto *100)
