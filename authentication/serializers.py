from rest_framework.serializers import ModelSerializer

from .models import User

class RegistrationSeralizer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']