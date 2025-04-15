from django.http import JsonResponse
from api.serializers import ProductSerializer
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET']) #### Pra que usar um decorador aqui, qual finalidade e o que ele faz especificamente aqui
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
