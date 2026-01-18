from rest_framework import serializers

from tasks_app.models import Task
   
class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    board = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    status = serializers.CharField(max_length=50)
    priority = serializers.CharField(max_length=50)
    assignee_id = serializers.IntegerField(allow_null=True, required=False) # id wird außer der user liste genommen und die details in der respond angezeigt
    reviewer_id = serializers.IntegerField(allow_null=True, required=False) # id wird außer der user liste genommen und die details in der respond angezeigt
    due_date = serializers.DateField(allow_null=True, required=False)   
    comments_count = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.board = validated_data.get('board', instance.board)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.assignee_id = validated_data.get('assignee_id', instance.assignee_id)
        instance.reviewer_id = validated_data.get('reviewer_id', instance.reviewer_id)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.comments_count = validated_data.get('comments_count', instance.comments_count)
        instance.save()
        return instance 