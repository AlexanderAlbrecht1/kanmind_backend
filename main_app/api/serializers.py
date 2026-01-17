from rest_framework import serializers

from main_app.models import Board

class BoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    member_count = serializers.IntegerField(default=1)
    ticket_count = serializers.IntegerField(default=0)
    tasks_to_do_count = serializers.IntegerField(default=0)
    tasks_high_prio_count = serializers.IntegerField(default=0)
    owner_id = serializers.IntegerField()

    def create(self, validated_data):
        return Board.objects.create(**validated_data)