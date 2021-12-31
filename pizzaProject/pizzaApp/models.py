from django.db import models

# El modelo Pizza
class Pizza (models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    nombre = models.CharField(max_length=32)
    precio = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.id = (self.id).upper()
        return super(Pizza, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre



CAT_BASICO = 'BASICO'
CAT_PREMIUM = 'PREMIUM'
CATEGORIAS_CHOICES = [
    (CAT_BASICO, 'Basico'),
    (CAT_PREMIUM, 'Premium')
]
# El modelo para cada ingrediente
class Ingrediente (models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    nombre = models.CharField(max_length=32)
    # Solo hay dos categorias por lo que usamos choices
    categoria = models.CharField(max_length=32, choices=CATEGORIAS_CHOICES, default=CAT_BASICO)

    def save(self, *args, **kwargs):
        self.id = (self.id).upper()
        self.categoria = (self.categoria).upper()
        return super(Ingrediente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


# Modelo para relacionar cada pizza con sus ingredientes
class Ingredientes_x_pizza (models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)