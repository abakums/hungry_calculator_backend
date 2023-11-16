from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers, status

from bills.utils.bill_positions import create_bill_positions


class BillPositionBulkCreateAPIView(APIView):
    permission_classes = [AllowAny]

    class InputSerializer(serializers.Serializer):
        class PositionsSerializer(serializers.Serializer):
            class PayerSerializer(serializers.Serializer):
                id = serializers.IntegerField(required=True)
                pricePerPart = serializers.IntegerField(required=True)

            title = serializers.CharField(required=True)
            price = serializers.IntegerField(required=True)
            payers = PayerSerializer(many=True)

        groupId = serializers.CharField(required=True)
        positions = PositionsSerializer(many=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = create_bill_positions(serializer.validated_data)

        return Response(data=data, status=status.HTTP_201_CREATED)
