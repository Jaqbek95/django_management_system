from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from .models import Project, Customer


class ProjectSerializer(ModelSerializer):

    customer = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    project_manager = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nick'
     )

    class Meta:
        model = Project
        fields = ('id', 'customer', 'description', 'project_manager', 'status')

class CustomerSerializer(ModelSerializer):

    project_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Customer
        fields = ('name', 'project_count')

    def get_project_count(self, obj):
        count = obj.project_set.count()
        return count