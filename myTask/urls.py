from django.urls import include, path
from Foods.urls import router1

urlpatterns = [
    path('api/v1/', include(router1.urls)),
]