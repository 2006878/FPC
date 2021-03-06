import pandas as pd

print("Lista de notas: ")

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/ratings.csv"
notas = pd.read_csv(uri)
notas.columns = ["Usuário" , "Filme" , "Nota", "Momento"]
resultado = notas.head()
print(resultado)

print("Listas de filmes:")

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
filmes = pd.read_csv(uri)
filmes.columns = ["ID Usuário", "Título", "Gênero"]
resultado = filmes.head()
print(resultado)

