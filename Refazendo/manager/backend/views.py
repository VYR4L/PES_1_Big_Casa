from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from manager.annual_leave.models import AnnualLeave
from rest_framework.permissions import IsAuthenticated

from rest_framework import status


class LoginUser(APIView):
    def post(self, request):
        username = self.request.data.get("username")
        password = self.request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Incorrect username or password"}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        logout(self.request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


class UserAnnualLeave(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        annual_leave = AnnualLeave.objects.filter(user=user).first()
        if not annual_leave:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {
                "user": user.username,
                "annual_leave": annual_leave.annual_leave,
            },
            status=status.HTTP_200_OK,
        )
    

class UserExtraHours(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        annual_leave = AnnualLeave.objects.filter(user=user).first()
        if not annual_leave:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {
                "user": user.username,
                "extra_hours": annual_leave.extra_hours,
            },
            status=status.HTTP_200_OK,
        )
    

class UserDayOff(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        annual_leave = AnnualLeave.objects.filter(user=user).first()
        if not annual_leave:
            return Response(
                {"message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            {
                "user": user.username,
                "day_off": annual_leave.day_off,
            },
            status=status.HTTP_200_OK,
        )