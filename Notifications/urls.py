from django.urls import path
from .import views
from .views import NotificationListView,NoteCreateView
urlpatterns = [
    path('index',views.NotificationListView.as_view(), name='index'),
    path('create',views.NoteCreateView.as_view(),name='create'),

]
