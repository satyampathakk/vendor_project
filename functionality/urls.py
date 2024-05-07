# urls.py
from django.urls import path
from .views import VendorList,CustomAuthTokenView, VendorDetail, PurchaseOrderList, PurchaseOrderDetail,VendorPerformance, AcknowledgePurchaseOrder,hello

urlpatterns = [
    path('',hello),
     path('api/token/<str:vendor_code>/', CustomAuthTokenView.as_view(), name='token_obtain'),
    path('api/vendors/', VendorList.as_view(), name='vendor-list'),
    path('api/vendors/<int:pk>/', VendorDetail.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', PurchaseOrderList.as_view(), name='purchase-order-list'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderDetail.as_view(), name='purchase-order-detail'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformance.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge-purchase-order'),
]
