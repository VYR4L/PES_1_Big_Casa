from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Gerente
from manager.backend.models import Usuario
from .permissions import IsGerente
from manager.backend.serializers import UsuarioSerializer


class LoginManager(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)
        if user is not None:
            if hasattr(user, 'gerente'):
                login(request, user)
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "User is not a manager"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"message": "Incorrect username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    def delete(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
    

class ManageUsers(APIView):
    permission_classes = [IsGerente]

    def post(self, request):
        cpf = request.data.get("cpf")
        username = cpf
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        phone = request.data.get("phone")
        address = request.data.get("address")

        if not all([username, password, first_name, last_name, cpf, phone, address]):
            return Response(
                {"message": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        if Usuario.objects.filter(user__profile__cpf=cpf).exists():
            return Response(
                {"message": "CPF already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username, password=password,
            first_name=first_name, last_name=last_name
        )
        user.profile.cpf = cpf
        user.profile.phone = phone
        user.profile.address = address
        user.profile.save()
        user.save()

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer = UsuarioSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        username = request.data.get("username")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        cpf = request.data.get("cpf")
        phone = request.data.get("phone")
        address = request.data.get("address")

        if not all([username, password, first_name, last_name, cpf, phone, address]):
            return Response(
                {"message": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.username = username
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.profile.cpf = cpf
        user.profile.phone = phone
        user.profile.address = address
        user.profile.save()
        user.save()

        return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)


class ManagerAnnualLeave(APIView):
    permission_classes = [IsGerente]

    def get(self, request):
        users = User.objects.all()
        annual_leave = []
        for user in users:
            annual_leave.append(
                {
                    "user": user.username,
                    "annual_leave": user.annual_leave.annual_leave,
                }
            )
        return Response(annual_leave, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        annual_leave = request.data.get("annual_leave")
        if not annual_leave:
            return Response(
                {"message": "Annual leave is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user.annual_leave.annual_leave = annual_leave
        user.annual_leave.save()

        return Response(
            {"message": "Annual leave updated successfully"}, status=status.HTTP_200_OK)
    

class ManagerExtraHours(APIView):
    permission_classes = [IsGerente]

    def get(self, request):
        users = User.objects.all()
        extra_hours = []
        for user in users:
            extra_hours.append(
                {
                    "user": user.username,
                    "extra_hours": user.annual_leave.extra_hours,
                }
            )
        return Response(extra_hours, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        extra_hours = request.data.get("extra_hours")
        if not extra_hours:
            return Response(
                {"message": "Extra hours are required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user.annual_leave.extra_hours = extra_hours
        user.annual_leave.save()

        return Response(
            {"message": "Extra hours updated successfully"}, status=status.HTTP_200_OK)
    

class ManagerDayOff(APIView):
    permission_classes = [IsGerente]

    def get(self, request):
        users = User.objects.all()
        day_off = []
        for user in users:
            day_off.append(
                {
                    "user": user.username,
                    "day_off": user.annual_leave.day_off,
                }
            )
        return Response(day_off, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        day_off = request.data.get("day_off")
        if not day_off:
            return Response(
                {"message": "Day off is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        user.annual_leave.day_off = day_off
        user.annual_leave.save()

        return Response(
            {"message": "Day off updated successfully"}, status=status.HTTP_200_OK)
    

class ControlManager(APIView):
    permission_classes = [IsGerente]

    def post(self, request):
        cpf = request.data.get("cpf")
        username = cpf
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        phone = request.data.get("phone")
        address = request.data.get("address")

        if not all([username, password, first_name, last_name, cpf, phone, address]):
            return Response(
                {"message": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        if Gerente.objects.filter(user__profile__cpf=cpf).exists():
            return Response(
                {"message": "CPF already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username, password=password,
            first_name=first_name, last_name=last_name
        )
        user.profile.cpf = cpf
        user.profile.phone = phone
        user.profile.address = address
        user.profile.save()
        user.save()

        gerente = Gerente.objects.create(user=user)
        gerente.save()

        return Response({"message": "Manager created successfully"}, status=status.HTTP_201_CREATED)
