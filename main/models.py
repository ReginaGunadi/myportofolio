import uuid
from django.db import models
from django.urls import reverse

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField(blank=True, null=True)
    ended_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

    @property
    def item_type(self):
        return "experience"

    @property
    def get_create_new_url(self): 
        return "main:create_experience"

    @property
    def get_show_all_url(self): 
        return "main:show_experience"
    
    @property
    def get_delete_url(self): 
        return reverse('main:delete_experience', kwargs={'experience_id': self.id})

    @property
    def ambil_isi_list(self):
        return self.description.split("\n")


class Award(models.Model):
    AWARD_CHOICES = [
        ('math', 'Math'),
        ('tech', 'Tech'),
        ('music', 'Music'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=AWARD_CHOICES, default='tech')
    image = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    @property
    def item_type(self):
        return "award"

    @property
    def get_create_new_item_url(self): 
        return "main:create_award"

    @property
    def get_show_all_item_url(self): 
        return "main:show_award"

    @property
    def get_delete_url(self): 
        return reverse('main:delete_award', kwargs={'award_id': self.id})