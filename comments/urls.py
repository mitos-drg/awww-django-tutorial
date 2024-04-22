from django.urls import path

from . import views

app_name = "comments"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:comment_id>/", views.edit, name="edit")
]