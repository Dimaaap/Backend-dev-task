from django.urls import path

from .views import RevenueStatisticsByDayAndName

urlpatterns = [
    path("", RevenueStatisticsByDayAndName.as_view(), name='revenue-statistics')
]