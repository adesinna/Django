from . import views
from django.urls import path


app_name = 'app1' # name spacing to identify the urls
urlpatterns = [
    path('', views.index, name="index"),
    path('item/', views.item, name="item"),
    path('<int:id>/', views.detail, name="detail"), # the name is used to replace hard coded url in the template
]