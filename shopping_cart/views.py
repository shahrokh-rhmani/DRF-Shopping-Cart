from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CardProduct
from .serializers import CartProductSerializer


class CartProductView(APIView):
    # POST
    def post(self, request):
        serializer = CartProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST)

    # GET
    def get(self, request):
        items = CardProduct.objects.all()
        serializer = CartProductSerializer(items, many=True)
        return Response({"status":"success", "data": serializer.data},
                status=status.HTTP_200_OK)
