from django.db.models import Sum
from rest_framework import generics

from .serializers import SpendStatisticSerializer
from .models import SpendStatistic
from revenue.models import RevenueStatistic


class SpendStatisticsByDayAndName(generics.ListAPIView):
    serializer_class = SpendStatisticSerializer

    def get_queryset(self):
        queryset = SpendStatistic.objects.values("date", "name").annotate(
            total_spend=Sum("spend"),
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversion=Sum("conversion"),
            revenue=Sum("revenuestatistic__revenue")
        )
        return queryset
