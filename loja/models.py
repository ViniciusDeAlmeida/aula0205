from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    descricao = models.TextField(blank=True, null=True)
    e_estoque = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    pagamento_a_vista = 'av'
    pagamento_2x = 'p2'
    pagamento_3x = 'p3'
    pagamento_4x = 'p4'
    pagamento_5x = 'p5'

    pagamento_opcoes = [
        (pagamento_a_vista, 'Pagamento à vista'),
        (pagamento_2x, 'Parcelado em 2x'),
        (pagamento_3x, 'Parcelado em 3x'),
        (pagamento_4x, 'Parcelado em 4x'),
        (pagamento_5x, 'Parcelado em 5x')
    ]

    nome = models.CharField(max_length=120)
    email =models.EmailField()
    endereco = models.CharField(max_length=150)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2, choices=pagamento_opcoes, default=pagamento_a_vista)

    def __str__(self):
        return self.nome

