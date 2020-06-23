from django.contrib import admin

from .models import *

admin.site.register(Pessoa)
admin.site.register(Usuario)
admin.site.register(Endereco)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Telefone)
admin.site.register(Funcionario)
admin.site.register(Fornecedor)
admin.site.register(Endereco_fornecedor)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Oferta)
admin.site.register(Fornecedor_categoria)
admin.site.register(Fornecedor_produto)
admin.site.register(Cesta)
admin.site.register(Cesta_produtos)

fields = ('image_tag',)
readonly_fields = ('image_tag')



# Register your models here.
