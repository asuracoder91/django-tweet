from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from tweets.models import Tweet
from .serializers import UserSerializer
from tweets.serializers import TweetSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserTweetsAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        password = request.data.get("password")
        if not password:
            return Response(
                {"error": "비밀번호를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST
            )
        user.set_password(password)
        user.save()
        return Response(
            {"status": "비밀번호가 변경되었습니다."}, status=status.HTTP_200_OK
        )
