from .models import Pizza,Ingrediente,Ingredientes_x_pizza
from rest_framework import serializers


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id','nombre','precio','activo']

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id','nombre','categoria']

class Ingredientes_x_pizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes_x_pizza
        fields = ['id','pizza','ingrediente']