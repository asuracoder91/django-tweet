from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view(), name="users"),
    path("<int:pk>/", views.UserDetailAPIView.as_view(), name="user_detail"),
    path("<int:pk>/tweets/", views.UserTweetsAPIView.as_view(), name="user_tweets"),
    path("password/", views.ChangePasswordAPIView.as_view(), name="change_password"),
]
