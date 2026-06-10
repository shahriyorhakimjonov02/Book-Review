from api.serializers.user import UserRegisterSerializer
from django.db.models import Avg
from api.serializers.base import *


class BookSerializer(BaseSerializer):
    class Meta:
        model = models.Book
        fields = ("id", "name", "author", "published_date", "book_images")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        avg = instance.ratings.aggregate(
            avg=Avg("rating")
        )["avg"]

        data["average_rating"] = round(avg, 1) if avg else 0
        data["ratings_count"] = instance.ratings.count()
        return data


class BookDetailSerializer(BaseSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["category"] = CategoryRelationSerializer(
            instance.category
        ).data

        avg = instance.ratings.aggregate(
            avg=Avg("rating")
        )["avg"]

        data["average_rating"] = round(avg, 1) if avg else 0
        data["ratings_count"] = instance.ratings.count()

        return data

class WriteCommentSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(default=0)
    comment = serializers.CharField(max_length=750)

class CommentSerializer(BaseSerializer):
    class Meta:
        model = models.Comment
        fields = ("user", "comment")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = UserRegisterSerializer(instance.user).data
        return data

class AddRatingSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)

# class RatingSerializer(serializers.Serializer):
#     class Meta:
#         model = models.Rating
#         fields = ("user", "rating")
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data["user"] = UserRegisterSerializer(instance.user).data
#         return data