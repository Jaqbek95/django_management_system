from django.http import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Project, Customer
from authentication.models import User
from .serializers import ProjectSerializer, CustomerSerializer


class ProjectsListView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        customer_name = request.data.get('customer')
        project_manager_name = request.data.get('project_manager')

        customer, created = Customer.objects.get_or_create(name=customer_name)
        project_manager = User.objects.get(nick=project_manager_name)

        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=customer, project_manager=project_manager)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailsView(APIView):
    permission_classes = [IsAuthenticated,]

    def get_object(self, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, id):
        project = self.get_object(id)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        project = self.get_object(id)

        customer_name = request.data.get('customer')
        project_manager_name = request.data.get('project_manager')

        customer, created = Customer.objects.get_or_create(name=customer_name)
        project_manager = User.objects.get(nick=project_manager_name)

        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save(customer=customer, project_manager=project_manager)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        project = self.get_object(id)
        project.delete()
        return Response('User was deleted')
        
class CustomersListView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)