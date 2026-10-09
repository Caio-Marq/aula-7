produto = "Mouse Gamer Wifi"
Valores = [20, 71, 100, 30]

if "mouse".lower() in produto.lower():
    print ("produto encontrado")
else:
    print ("produto n encontrado")

def dobrar(valor):
    resultado = valor * 2
    return resultado
print(dobrar(4))

valores_novos = []
for item in Valores:
    valores_novos.append(dobrar(item))
print(valores_novos)
print(Valores)

alunos = ["Ana","Hugo","Mariana","Pedro","Ana Paula"]
aluno_procurado = input("digite um nome ...  ")
for item in alunos:
    if aluno_procurado.lower() in item.lower():
        print(item)







