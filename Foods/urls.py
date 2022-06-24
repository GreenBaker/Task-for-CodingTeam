from rest_framework import routers
from Foods import views

router1 = routers.DefaultRouter()
router1.register('foods', views.FoodCategoryViewSet)
