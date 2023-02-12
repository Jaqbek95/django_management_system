from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# from rest_framework import request
# from rest_framework.response import Response

# from .serializers import UserSeralizer


# class RegisterView(APIView):
#     def post (self, request):
#         serializer = UserSeralizer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)