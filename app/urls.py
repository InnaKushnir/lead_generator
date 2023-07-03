from django.urls import path
from app.views import UserCreateView, home, ObjectListView, ObjectCreateView

urlpatterns = [
    path("", home, name="home"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("object/", ObjectListView.as_view(), name="object-list"),
    path("object/create/", ObjectCreateView.as_view(), name="object-create"),
]

app_name = "app"
