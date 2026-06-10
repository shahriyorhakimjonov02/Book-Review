from rest_framework import serializers

import src.core.models as models

class CategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "name")

class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created_at'] = instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
        data['updated_at'] = instance.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        return data