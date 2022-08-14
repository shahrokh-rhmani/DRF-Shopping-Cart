from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CardProduct
from .serializers import CartProductSerializer
from django.shortcuts import get_object_or_404


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
    def get(self, request, id=None):
        # get id
        if id:
            item = get_object_or_404(CardProduct, pk=id)
            serializer = CartProductSerializer(item)
            return Response({"status":"success", "data": serializer.data},
                status=status.HTTP_200_OK)

        # get all
        items = CardProduct.objects.all()
        serializer = CartProductSerializer(items, many=True)
        return Response({"status":"success", "data": serializer.data},
                status=status.HTTP_200_OK)
    # patch
    def patch(self, request, id=None):
        item = CardProduct.objects.get(id=id)
        serializer = CartProductSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    # delete
    def delete(self, request, id=None):
        item = get_object_or_404(CardProduct, pk=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
