# utils.py
from django.db.models import Avg, Count, F
from .models import PurchaseOrder

def calculate_vendor_performance_metrics(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

    # On-Time Delivery Rate
    on_time_delivery_count = completed_pos.filter(delivery_date__lte=F('acknowledgment_date')).count()
    total_completed_pos = completed_pos.count()
    vendor.on_time_delivery_rate = (on_time_delivery_count / total_completed_pos) * 100 if total_completed_pos else 0

    # Quality Rating Average
    vendor.quality_rating_avg = completed_pos.exclude(quality_rating__isnull=True).aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating'] or 0.0

    # Average Response Time
    vendor.average_response_time = completed_pos.exclude(acknowledgment_date__isnull=True).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time'] or 0.0

    # Fulfilment Rate
    fulfilled_pos = completed_pos.exclude(status='completed_with_issues')
    vendor.fulfillment_rate = (fulfilled_pos.count() / total_completed_pos) * 100 if total_completed_pos else 0

    vendor.save()
    return vendor
