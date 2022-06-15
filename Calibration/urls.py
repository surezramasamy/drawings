
from django.urls import path
from .import views
from .views import Instruments_Listview,Fixtures_Listview,Fixtures_Listview2

urlpatterns = [
    path('',views.Basic.as_view(), name='home'),
    path('Fixtures',views.Fixtures_Listview.as_view(), name='Fixtures'),
    path('Fixtures2',views.Fixtures_Listview2.as_view(), name='Fixtures2'),
    path('Instruments',views.Instruments_Listview.as_view() , name='Instruments'),
    path('Cal',views.cal, name='Cal'),
    path('Cal2',views.cal2, name='Cal2'),

]
