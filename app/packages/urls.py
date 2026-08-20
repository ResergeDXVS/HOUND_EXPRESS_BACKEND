from django.urls import path, include
from .views import CreateGuideView, UpdateGuideView, GetGuideView, DeleteGuideView, ReportGuidesView, HistoricalGuideView


urlpatterns = [
    path('create-guide', CreateGuideView.as_view()),
    path('update-guide/<int:pk>', UpdateGuideView.as_view()),
    path('get-guides', GetGuideView.as_view()),
    path('delete-guide/<int:pk>', DeleteGuideView.as_view()),
    path('report',ReportGuidesView.as_view()),
    path('get-history/<int:pk>',HistoricalGuideView.as_view()),
]