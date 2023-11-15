from users.models import Participant


def create_participant(data):
    participant = Participant(name=data.get("name"))
    participant.save()
    return participant
