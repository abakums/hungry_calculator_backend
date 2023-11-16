from rest_framework.generics import get_object_or_404

from users.models import Group
from bills.models import BillPosition, ParticipantBillPosition


def create_bill_positions(data):
    response = {"positions": []}
    group = get_object_or_404(Group.objects.all(), group_uuid=data.get("groupId"))
    positions = data.get("positions")

    for position in positions:
        bill_position = BillPosition(
            title=position.get("title"),
            price=position.get("price"),
            group_id=group.id,
            parts=position.get("parts")
        )
        bill_position.save()
        payers = position.get("payers")
        for payer in payers:
            participant_bill_position = ParticipantBillPosition(
                bill_position_id=bill_position.id,
                participant_id=payer.get("id"),
                participant_price=payer.get("personalPrice"),
                personal_parts=payer.get("personalParts")
            )
            participant_bill_position.save()

        response["positions"].append({"id": bill_position.id, "title": bill_position.title})
        return response
