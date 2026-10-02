from aluno import Aluno
from disciplina import Disciplina
#criar\ instanciar um objeto
aluno1 = Aluno("Joao", "123455", "Ciencia da computaçao")
# criar segunda disciplina

sers = Disciplina ("Solucoes Renovaveis", "Tritiack")
cs = Disciplina( "Computer science",  "Lucas")

# MATRICULAR ALUNOS NA DISCIPLINA disciplinas
aluno1.matricular(sers)
aluno1.matricular(cs)
#print(aluno1.disciplinas[1].professor)

#adicionar notas do aluno refernte as disciplinas
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 8)
aluno1.adicionar_nota(cs, 5)
aluno1.adicionar_nota(cs, 3)
#print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(cs))
print(aluno1.calcular_media_g())