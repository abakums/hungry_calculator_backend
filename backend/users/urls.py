from django.urls import path, include

from users.views.groups.get import GroupGetAPIView
from users.views.groups.create import GroupCreateAPIView
from users.views.participants.create import ParticipantCreateAPIView


participants_urlpatterns = [
    path("create/", ParticipantCreateAPIView.as_view(), name="participant-create")
]


groups_url_patterns = [
    path("create/", GroupCreateAPIView.as_view(), name="group-create"),
    path("get/<str:group_uuid>/", GroupGetAPIView.as_view(), name="groups-get"),
]


urlpatterns = [
    path("participants/", include(participants_urlpatterns)),
    path("groups/", include(groups_url_patterns))
]
