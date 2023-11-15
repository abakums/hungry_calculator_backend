from users.models import Group, Participant, ParticipantGroup


def create_group(data):
    creator_id = data.get("creator", {}).get("id")
    group = Group(
        title=data.get("title"),
        organizer_id=creator_id,
        requisites=data.get("requisites")
    )
    group.save()

    participants = data.get("participants")
    participants_to_create = []
    for participant in participants:
        participants_to_create.append(Participant(name=participant.get("name")))

    created_participants = Participant.objects.bulk_create(participants_to_create)
    participant_groups_to_create = []
    for participant in created_participants:
        participant_groups_to_create.append(ParticipantGroup(group=group, participant=participant))

    participants_to_create.append(ParticipantGroup(group=group, participant_id=creator_id, is_organizer=True))

    ParticipantGroup.objects.bulk_create(participant_groups_to_create)

    return group
