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
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.member_count = validated_data.get('member_count', instance.member_count)
        instance.ticket_count = validated_data.get('ticket_count', instance.ticket_count)
        instance.tasks_to_do_count = validated_data.get('tasks_to_do_count', instance.tasks_to_do_count)
        instance.tasks_high_prio_count = validated_data.get('tasks_high_prio_count', instance.tasks_high_prio_count)
        instance.owner_id = validated_data.get('owner_id', instance.owner_id)
        instance.save()
        return instance