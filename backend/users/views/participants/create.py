from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers, status

from users.utils.participants import create_participant


class ParticipantCreateAPIView(APIView):
    permission_classes = [AllowAny]

    class InputSerializer(serializers.Serializer):
        title = serializers.CharField(required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        participant = create_participant(serializer.validated_data)

        data = {"id": participant.id}
        return Response(data=data, status=status.HTTP_201_CREATED)
