import datetime
from dataclasses import dataclass


@dataclass
class SpendItem:
    name: str
    date: datetime.date
    spend: float
    impressions: int
    clicks: int
    conversion: int


@dataclass
class RevenueItem:
    name: str
    date: datetime.date
    revenue: float
    spend: SpendItem
