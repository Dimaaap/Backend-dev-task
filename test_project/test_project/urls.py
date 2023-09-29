from django.urls import path, include

urlpatterns = [
    path("spend/", include("spend.urls")),
    path("revenue/", include("revenue.urls"))
]
