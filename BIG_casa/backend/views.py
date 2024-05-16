from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Usuario, Gerente

class CriarGerente(APIView):
    def post(self, request, *args, **kwargs):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        phone = request.data.get("phone")
        cpf = request.data.get("cpf")
        password = request.data.get("password")
        adress = request.data.get("adress")

        if (
            not first_name
            or not last_name
            or not phone
            or not cpf
            or not password
            or not adress
        ):
            return Response(
                {"message": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Gerente.objects.filter(cpf=cpf).exists():
            return Response(
                {"message": "CPF already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        manager = Gerente.objects.create(
            first_name=first_name, last_name=last_name, phone=phone, cpf=cpf, adress=adress, password=password
        )

        if manager:
            manager.save()
            return Response({"message": "Manager created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "Failed to create manager"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("cpf")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = Usuario.objects.get(username=username)
        except:
            user = None

        if user and user.check_password(password):
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class Tela_gerente(APIView):
    permission_classes = [IsAuthenticated]

    # Blocking users who are not from 'Gerente' class
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.groups.filter(name='Gerente').exists():
            return Response(
                {"message": "You do not have permission to acces this page"},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().dispatch(request, *args, **kwargs)

    # Create Users
    def post(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        cpf = request.data.get("cpf")
        adress = request.data.get("adress")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")

        if (
            not first_name
            or not last_name
            or not phone
            or not cpf
            or not adress
            or not password
        ):
            return Response(
                {"message": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Usuario.objects.filter(cpf=cpf).exists():
            return Response(
                {"message": "CPF already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = Usuario.objects.create_user(
            first_name=first_name, last_name=last_name, phone=phone, cpf=cpf, adress=adress, password=password
        )

        if user:
            return Response({"message": "User created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "Failed to create user"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        
    # annual leave's methods:
    def get_annual_leave(self, request, *args, **kwargs):
        users = Usuario.objects.all()
        annual_leave_list = [user.annual_leave for user in users]
        return Response({"annual_leave_list": annual_leave_list}, status=status.HTTP_200_OK)
    
    # day off's methods:
    def get_day_off(self, request, *args, **kwargs):
        users = Usuario.objects.all()
        day_off_list = [user.day_off for user in users]
        return Response({"annual_leave_list": day_off_list}, status=status.HTTP_200_OK)
    
    def put_day_off(self, request, user_id, *args, **kwargs):
        try:
            user_instance = Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return Response(
                {"message": "User doesn't exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if 'day_off' not in request.data:
            return Response(
                {"message":"Missing 'day_off' field in request data"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user_instance.day_off= request.data['day_off']
        user_instance.save()

        return Response(
            {"message": "Day off uptated successfully"},
            status=status.HTTP_200_OK
        )
    
    # extra time's methods:
    def get_extra_time(self, reques, *args, **kwargs):
        users = Usuario.objects.all()
        extra_time_list = [user.extra_time for user in users]
        return Response({"annual_leave_list": extra_time_list}, status=status.HTTP_200_OK)
    
    def put_extra_time(self, request, user_id, *args, **kwargs):
        try:
            user_instance = Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return Response(
                {"message": "User doesn't exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if 'extra_time' not in request.data:
            return Response(
                {"message":"Missing 'extra_time' field in request data"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user_instance.extra_time= request.data['extra_time']
        user_instance.save()

        return Response(
            {"message": "Extra time uptated successfully"},
            status=status.HTTP_200_OK
        )
    
    # Delete Users:
    def delete(self, request, user_id, *args, **kwargs):
        try:
            user_instance = Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return Response(
                {"message": "User doesn't exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        user_instance.delete()

        return Response(
            {"message": "User deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
    
