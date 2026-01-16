from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=100)
    member_count = models.PositiveIntegerField(default=1)
    ticket_count = models.PositiveIntegerField(default=0)
    tasks_to_do_count = models.PositiveIntegerField(default=0)
    tasks_high_prio_count = models.PositiveIntegerField(default=0)
    owner_id = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    board = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    assignee_id = models.PositiveIntegerField(null=True, blank=True) # id wird außer der user liste genommen und die details in der respond angezeigt
    reviewer_id = models.PositiveIntegerField(null=True, blank=True) # id wird außer der user liste genommen und die details in der respond angezeigt
    due_date = models.DateField(null=True, blank=True)
    comments_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name