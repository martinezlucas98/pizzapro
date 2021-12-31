from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import Ingredientes_x_pizzaSerializer, PizzaSerializer, IngredienteSerializer
from .models import Ingredientes_x_pizza, Pizza, Ingrediente
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication


class PizzaView(APIView):
    def post(self, request):
        if (self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)):
            serializer = PizzaSerializer(data=request.data, context= {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'ok', 'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "error", "detail": "Se necesita autorización."})

    def patch(self, request, id):
        if (self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)):
            item = Pizza.objects.get(id=id)
            serializer = PizzaSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "ok", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})
        else:
            return Response({"status": "error", "detail": "Se necesita autorización."})

    def get(self,request):
        if (self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)):
            items = Pizza.objects.all()
        else:
            items = Pizza.objects.filter(activo=True)
        serializer = PizzaSerializer(items, many=True)
        return Response({"status": "ok", "data": serializer.data}, status=status.HTTP_200_OK)


class IngredienteView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        if (self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)):
            request.data._mutable = True
            # Ponemos en mayuscula la categoria (ya que así está en el diccionario en ./models.py)
            request.data['categoria'] = request.data['categoria'].upper()
            request.data._mutable = False
            serializer = IngredienteSerializer(data=request.data, context= {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'ok', 'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "error", "detail": "Se necesita autorización."})

    def get(self, request):
        items = Ingrediente.objects.all()
        serializer = IngredienteSerializer(items, many=True)
        return Response({"status": "ok", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        if (self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)):
            try:
                Ingredientes_x_pizza.objects.filter(ingrediente=id)[0]
                return Response({"detail": "Hay al menos una pizza que contiene este ingrediente. No se puede eliminar."})
            except:
                item = get_object_or_404(Ingrediente, id=id)
                item.delete()
                return Response({"status": "ok", "data": "Item Eliminado"})
        else:
            return Response({"status": "error", "detail": "Se necesita autorización."})

        
    def patch(self, request, id):
        if (self.request.user.is_staff):
            request.data._mutable = True
            # Ponemos en mayuscula la categoria (ya que así está en el diccionario en ./models.py)
            request.data['categoria'] = request.data['categoria'].upper()
            request.data._mutable = False

            item = Ingrediente.objects.get(id=id)
            serializer = IngredienteSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "ok", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})
        else:
            return Response({"status": "error", "detail": "Se necesita autorización."})



class Ingredientes_x_pizzaView(APIView):
    def post(self, request):
        request.data._mutable = True
        # Ponemos en mayuscula los campos de caracteres
        request.data['pizza'] = request.data['pizza'].upper()
        request.data['ingrediente'] = request.data['ingrediente'].upper()
        request.data._mutable = False
        serializer = Ingredientes_x_pizzaSerializer(data=request.data, context= {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pizza,ingrediente):
        try:
            item = Ingredientes_x_pizza.objects.filter(pizza=pizza, ingrediente=ingrediente)[0],
            item[0].delete()
            return Response({"status": "ok", "data": "Item Eliminado"})
        except:
            return Response({"detail": "No se encontraron coincidencias."})


class PizzaDetalleView(APIView):
    def get(self, request, id):
        ingredientes= Ingredientes_x_pizza.objects.filter(pizza=id).values('ingrediente')
        item = get_object_or_404(Pizza, id=id)
        serializer = PizzaSerializer(item)
        data = {}
        data.update(serializer.data)
        data['ingredientes']=[]

        for ingrediente in ingredientes:
            ingredienteSerializer = IngredienteSerializer(get_object_or_404(Ingrediente,id=ingrediente['ingrediente']))
            data['ingredientes'].append(ingredienteSerializer.data['nombre'])

        data['ingredientes'].sort()
        return Response({"status": "ok", "data": data}, status=status.HTTP_200_OK)
    