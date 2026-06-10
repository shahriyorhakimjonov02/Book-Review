# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
#
# import api.serializers as serializers
# import src.core.models as models
#
# @api_view(['GET'])
# def category_api(request):
#     object_list = models.Category.objects.all()
#     serializer = serializers.CategorySerializer(object_list, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK )
#
# @api_view(['POST'])
# def category_create(request):
#     serializer = serializers.CategorySerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET'])
# def category_detail(request, pk):
#     try:
#         instance = models.Category.objects.get(id=pk)
#         serializer = serializers.CategorySerializer(instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except models.Category.DoesNotExist as e:
#         return Response(e.message, status=status.HTTP_404_NOT_FOUND)
#
# @api_view(['PUT'])
# def category_update(request, pk):
#     try:
#         instance = models.Category.objects.get(id=pk)
#         serializer = serializers.CategorySerializer(instance=instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except models.Category.DoesNotExist as e:
#         return Response({"Error": str(e)}, status=status.HTTP_404_NOT_FOUND)
#
# @api_view(['DELETE'])
# def category_delete(request, pk):
#     try:
#         instance = models.Category.objects.get(id=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except models.Category.DoesNotExist as e:
#         return Response({"Error": str(e)}, status=status.HTTP_404_NOT_FOUND

from rest_framework.generics import ListAPIView

import src.core.models as models
import api.serializers as serializers

class CategoryListApi(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
