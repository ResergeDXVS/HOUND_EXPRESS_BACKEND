from django.urls import path, include
from .views import CreateGuideView, UpdateGuideView, GetGuideView, DeleteGuideView


urlpatterns = [
    path('create-guide', CreateGuideView.as_view()),
    path('update-guide/<int:pk>', UpdateGuideView.as_view()),
    path('get-guide/<int:pk>', GetGuideView.as_view()),
    path('delete-guide/<int:pk>', DeleteGuideView.as_view()),
]