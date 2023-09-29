from django.urls import path

from .views import SpendStatisticsByDayAndName

urlpatterns = [
    path('', SpendStatisticsByDayAndName.as_view(), name="spend")
]
