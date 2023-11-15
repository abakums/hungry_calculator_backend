from django.urls import path, include


bill_positions_urlpatterns = [
    # path()
]

urlpatterns = [
    path("bill_positions/", include(bill_positions_urlpatterns))
]
