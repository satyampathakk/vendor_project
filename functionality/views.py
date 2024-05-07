# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer,PurchaseOrderSerializer,VendorPerformanceSerializer
from django.http import Http404
from django.utils import timezone
from django.http import HttpResponse
from .utils import calculate_vendor_performance_metrics
from rest_framework_simplejwt.tokens import RefreshToken

class CustomAuthTokenView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request,vendor_code, *args, **kwargs):
        
        if not vendor_code:
            return Response({'error': 'Vendor code is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            vendor = Vendor.objects.get(vendor_code=vendor_code)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor with provided vendor code does not exist'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(vendor)
        access = refresh.access_token

        return Response({
            'access': str(access),
            'refresh': str(refresh),
            'vendor_id': vendor.id
        })
    
class VendorList(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetail(APIView):
    def get_object(self, pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, pk):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vendor = self.get_object(pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PurchaseOrderList(APIView):
    def get(self, request):
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderDetail(APIView):
    def get_object(self, pk):
        try:
            return PurchaseOrder.objects.get(pk=pk)
        except PurchaseOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        purchase_order = self.get_object(pk)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def put(self, request, pk):
        purchase_order = self.get_object(pk)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        purchase_order = self.get_object(pk)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VendorPerformance(APIView):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(pk=vendor_id)
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)

class AcknowledgePurchaseOrder(APIView):
    def post(self, request, po_id):
        try:
            po = PurchaseOrder.objects.get(pk=po_id)
            po.acknowledgment_date = timezone.now()
            po.save()
            vendor=calculate_vendor_performance_metrics(po.vendor)
            HistoricalPerformance.objects.create(
                vendor_code=po.vendor_code,
                date=timezone.now(),
                on_time_delivery_rate=vendor.on_time_delivery_rate,
                quality_rating_avg=vendor.quality_rating_avg,
                average_response_time=vendor.average_response_time,
                fulfilment_rate=vendor.fulfillment_rate
            )
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)
        



def hello(request):
    return HttpResponse("urlpatterns = ['api/vendors/', 'api/vendors/<int:pk>/', 'api/purchase_orders/', 'api/purchase_orders/<int:pk>/', 'api/vendors/<int:vendor_id>/performance/', 'api/purchase_orders/<int:po_id>/acknowledge/']")