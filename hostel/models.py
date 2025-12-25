from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single Sharing'),
        ('double', 'Double Sharing'),
        ('triple', 'Triple Sharing'),
    ]

    BLOCK_CHOICES = [
        ('A', 'Block A'),
        ('B', 'Block B'),
        ('C', 'Block C'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    year = models.IntegerField()

    preferred_block = models.CharField(
        max_length=1, choices=BLOCK_CHOICES, blank=True, null=True
    )
    preferred_room_type = models.CharField(
        max_length=10, choices=ROOM_TYPE_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.user.username


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single Sharing'),
        ('double', 'Double Sharing'),
        ('triple', 'Triple Sharing'),
    ]

    BLOCK_CHOICES = [
        ('A', 'Block A'),
        ('B', 'Block B'),
        ('C', 'Block C'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    block = models.CharField(max_length=1, choices=BLOCK_CHOICES)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    capacity = models.IntegerField()
    occupied = models.IntegerField(default=0)

    def is_available(self):
        return self.occupied < self.capacity

    def __str__(self):
        return f"{self.room_number} - Block {self.block} ({self.room_type})"



class Allocation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    allocated_on = models.DateTimeField(auto_now_add=True)
