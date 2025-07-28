from django.db import models
from django.utils import timezone

class User(models.Model):
    tg_id = models.BigIntegerField(unique=True, verbose_name='Telegram ID')
    first_name = models.CharField(max_length=255, verbose_name='First Name', blank=False, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last Name')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    end_use_date = models.DateTimeField(default=timezone.now, verbose_name='End Use Date')
    def full_name(self):
        return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name
    def __str__(self):
        return self.full_name()+f" ({self.id})"
    def __int__(self):
        return int(self.tg_id)
    

