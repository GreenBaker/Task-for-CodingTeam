from django.db.models import Prefetch
from rest_framework import viewsets
from Foods.models import Food, FoodCategory
from Foods.serializers import FoodListSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.filter(food__is_publish=True).distinct().prefetch_related(
        Prefetch("food", queryset=Food.objects.filter(is_publish=True)))
