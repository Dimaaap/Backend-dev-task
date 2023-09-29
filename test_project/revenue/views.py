from django.shortcuts import render
from django.db.models import Sum
from rest_framework import generics

from .serializers import RevenueStatisticSerializer
from .models import RevenueStatistic


class RevenueStatisticsByDayAndName(generics.ListAPIView):
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        queryset = RevenueStatistic.objects.values("date", "name").annotate(
            total_revenue=Sum("revenue"),
            total_spend=Sum("spend__spend"),
            total_impressions=Sum("spend__impressions"),
            total_clicks=Sum("spend__clicks"),
            total_conversion=Sum("spend__conversion"),

        )
        return queryset

