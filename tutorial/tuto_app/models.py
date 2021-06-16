from django.db import models
# Create your models here.
COLORES = (
    ('0', 'Rojo'),
    ('1', 'Amarillo'),
    ('2', 'Verde'),
    ('3', 'Azul'),
    ('4', 'Negro'),
)
class Deposito(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30)

class Articulo(models.Model):
    codigo =models.IntegerField()
    descripcion = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=1, choices=COLORES)
    deposito = models.ForeignKey(Deposito, null=True, on_delete=models.SET_NULL)