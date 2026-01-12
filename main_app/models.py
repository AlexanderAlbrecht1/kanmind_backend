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