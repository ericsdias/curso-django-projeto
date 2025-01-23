from django.urls import path

<<<<<<< HEAD
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>', views.recipe),
=======
from recipes.views import home
urlpatterns = [
    path('', home),
>>>>>>> 38d6e5a86f3185056e66767df0eaa44322017b6a
]