from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404

from users.models import Group, Participant
from bills.models import BillPosition, ParticipantBillPosition


class GroupGetAPIView(APIView):
    permission_classes = [AllowAny]

    class OutputSerializer(serializers.ModelSerializer):
        class CreatorSerializer(serializers.ModelSerializer):
            id = serializers.IntegerField(required=True)

            class Meta:
                model = Participant
                fields = ("id",)

        class ParticipantSerializer(serializers.Serializer):
            id = serializers.IntegerField(required=True)
            name = serializers.CharField(required=True)

            class Meta:
                model = Participant
                fields = ("id", "name")

        class BillSerializer(serializers.ModelSerializer):
            class PositionSerializer(serializers.Serializer):
                id = serializers.IntegerField(required=True)
                title = serializers.CharField(required=True)
                price = serializers.IntegerField(required=True)
                parts = serializers.IntegerField(required=True)
                personalParts = serializers.IntegerField(required=True)
                personalPrice = serializers.IntegerField(required=True)

            payerId = serializers.IntegerField(required=True)
            totalPrice = serializers.IntegerField(required=True)
            positions = PositionSerializer(many=True, required=True)

        title = serializers.CharField(required=True)
        requisites = serializers.CharField(required=True)
        creator = CreatorSerializer(required=True, source="organizer")
        participants = ParticipantSerializer(many=True)
        bill = BillSerializer(many=True, source="get_bill")

        class Meta:
            model = Group
            fields = ("title", "requisites", "creator", "participants", "bill")

    def get_queryset(self, group_uuid):
        group = get_object_or_404(Group.objects.all(), group_uuid=group_uuid)
        return group

    def get(self, request, group_uuid):
        group = self.get_queryset(group_uuid)

        data = self.OutputSerializer(group).data

        return Response(data=data, status=status.HTTP_200_OK)
