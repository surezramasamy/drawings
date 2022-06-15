from django.urls import path
from .views import HomePageView,drgupload
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('drg', views.drg, name='drg'),
    path('drgupload/',views.drgupload, name='drgupload'),


]
