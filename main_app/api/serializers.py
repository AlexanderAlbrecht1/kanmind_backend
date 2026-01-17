from rest_framework import serializers

from main_app import models

class BoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    member_count = serializers.PositiveIntegerField(default=1)
    ticket_count = serializers.PositiveIntegerField(default=0)
    tasks_to_do_count = serializers.PositiveIntegerField(default=0)
    tasks_high_prio_count = serializers.PositiveIntegerField(default=0)
    owner_id = serializers.PositiveIntegerField()
