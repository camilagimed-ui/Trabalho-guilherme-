
alunos = ['ana','joao','gabriel','kauan','julia']
medias = [8,      9,       10,      9.8,      10]
#o (len(alunos) acessa os nomes só que como se fosse numeros ou seja ana = 0 joao = 1 e as medias ja se encontra
#  com numero ent n precisa

for indice in range(len(alunos)):
    print(f'nome do aluno: {alunos[indice]} | media do aluno: {medias[indice]}')