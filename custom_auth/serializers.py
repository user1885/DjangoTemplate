from rest_framework.serializers import Serializer
from custom_auth.models import CustomUser


class CustomUserSerializer(Serializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_staff']
        