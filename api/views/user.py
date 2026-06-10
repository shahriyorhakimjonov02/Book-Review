from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


import src.core.models as models
import api.serializers as serializers

class UserCreateAPIView(CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        password = serializer.validated_data["password"]
        user = serializer.save()
        user.set_password(password)
        user.save()

class GetMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.UserRegisterSerializer(user)
        return Response(serializer.data)

