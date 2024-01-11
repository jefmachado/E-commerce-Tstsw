from .base import *

class Produtos(BaseModels):
    nome = models.CharField(max_length=25, verbose_name="Nome", help_text="Nome do Produto")
    tipo = models.CharField(max_length=25, verbose_name="Nome", help_text="Nome do Produto")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor", help_text="Valor do Produto")
    stq = models.IntegerField(verbose_name="estoque", help_text="Estoque do Produto")

    class Meta:
        pass


