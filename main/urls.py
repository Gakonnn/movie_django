from django.urls import path ,include
from . import views




urlpatterns = [
    path('',views.index,name='glavni'),
    path('<slug:genr>/',views.index,name='movie_genr'),
    path('<slug:genr>/<int:page_nm>/', views.index, name='movie_genr'),
    path('<slug:genr>/<slug:moox>/',views.movie_page,name='movie_detail'),
]