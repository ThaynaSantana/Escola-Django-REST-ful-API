from django.db import models


class Estudante(models.Model):
    objects = None
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    objects = None
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avançado'),
    )

    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=255, blank=False)
    nivel = models.CharField(choices=NIVEL, default='B', blank=False, null=False, max_length=1)

    def __str__(self):
        return self.codigo

class Matricula(models.Model):
    objects = None
    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno')
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(choices=PERIODO, default='M', blank=False, null=False, max_length=1)
