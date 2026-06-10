from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

import src.core.models as models
import api.serializers as serializers

class BookListAPIView(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    search_fields = ['name', "id"]
    filterset_fields = ['category']
    filter_backends = [SearchFilter, DjangoFilterBackend]

class BookDetailAPIView(RetrieveAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookDetailSerializer

class WriteCommentAPIView(APIView):
    @extend_schema(request=serializers.WriteCommentSerializer,
                   responses={"status": bool})
    def post(self, request):
        try:
            user = request.user
            data = request.data
            book = get_object_or_404(models.Book, pk=data.get('book_id'))
            comment = data.get('comment')
            models.Comment.objects.create(user=user, book=book, comment=comment)
            return Response({"status": True})
        except Exception as e:
            return Response({"status": False, "error": str(e)})


class CommentListAPIView(ListAPIView):
    queryset = models.Comment.objects.all()
    filterset_fields = ['book']
    filter_backends = [DjangoFilterBackend]
    serializer_class = serializers.CommentSerializer


class AddRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(request=serializers.AddRatingSerializer,
                   responses={"status": bool})
    def post(self, request):
        try:
            serializer = serializers.AddRatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            book = get_object_or_404(
                models.Book,
                pk=serializer.validated_data["book_id"]
            )

            rating_obj, created = models.Rating.objects.update_or_create(
                user=request.user,
                book=book,
                defaults={
                    "rating": serializer.validated_data["rating"]
                }
            )

            return Response({
                "status": True,
                "rating": rating_obj.rating
            })
        except Exception as e:
            return Response({"status": False, "error": str(e)})

# class RatingListAPIView(ListAPIView):
#     queryset = models.Rating.objects.all()
#     filterset_fields = ['book']
#     filter_backends = [DjangoFilterBackend]
#     serializer_class = serializers.RatingSerializer