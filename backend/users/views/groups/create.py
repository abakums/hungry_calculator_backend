from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers, status

from users.utils.groups import create_group


class GroupCreateAPIView(APIView):
    permission_classes = [AllowAny]

    class InputSerializer(serializers.Serializer):
        class CreatorSerializer(serializers.Serializer):
            id = serializers.IntegerField(required=True)

        class ParticipantSerializer(serializers.Serializer):
            name = serializers.CharField(required=True)

        title = serializers.CharField(required=True)
        requisites = serializers.CharField(required=True)
        creator = CreatorSerializer(required=True)
        participants = ParticipantSerializer(many=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group, participants = create_group(serializer.validated_data)

        data = {
            "groupId": group.group_uuid,
            "participants": [
                {
                    "id": participant.id,
                    "name": participant.name
                } for participant in participants
            ]
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
