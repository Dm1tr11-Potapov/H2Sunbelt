from django.db import models

class Guestbook(models.Model):
    user_first_name = models.CharField(max_length=30, blank=False)
    user_last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    feedback_frame = models.CharField(max_length=1000, blank=False)
    checkbox = models.BooleanField(default=False) # if false, then in draft mode

    def __str__(self):
        return f'Отзыв от {self.user_first_name} {self.user_last_name}'