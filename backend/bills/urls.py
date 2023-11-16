from django.urls import path, include

from bills.views.bill_positions.bulk_create import BillPositionBulkCreateAPIView


bill_positions_urlpatterns = [
    path("create/", BillPositionBulkCreateAPIView.as_view(), name="bill-positions-bulk-create")
]


urlpatterns = [
    path("bill_positions/", include(bill_positions_urlpatterns))
]
