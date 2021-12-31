from django.urls import path
from .views import PizzaView, IngredienteView, Ingredientes_x_pizzaView, PizzaDetalleView

urlpatterns = [
    # Listar pizzas (GET); Agregar pizza (POST)
    path('pizza/', PizzaView.as_view()),
    # Modificar pizza por su id
    path('pizza/<str:id>', PizzaView.as_view()),
    # Listar ingredientes (GET); Agregar ingrediente (POST)
    path('ingrediente/', IngredienteView.as_view()),
    # Eliminar un ingrediente por id (DEL); Modificar un ingrediente por su id (PATCH)
    path('ingrediente/<str:id>', IngredienteView.as_view()),
    # Agregar un ingrediente (por su id) a una pizza (por su id) (POST)
    path('ingrediente-x-pizza/', Ingredientes_x_pizzaView.as_view()),
    # Eliminar un ingrediente (por su id) de una pizza (por su id) (DEL); 
    path('ingrediente-x-pizza/<str:pizza>/<str:ingrediente>', Ingredientes_x_pizzaView.as_view()),
    # Ver detalle de una pizza (por su id) (GET)
    path('pizza-detalle/<str:id>',PizzaDetalleView.as_view()),
]