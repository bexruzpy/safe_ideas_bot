from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Project Title')
    user = models.ForeignKey('users.User', related_name='projects', on_delete=models.CASCADE, verbose_name='User')
    description = models.TextField(verbose_name='Project Description', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    def __str__(self):
        return self.title

# Choose class
class FunctionType(models.TextChoices):
    TEXT = 'text', 'Text'
    IMAGE = 'image', 'Image'
    VOICE = 'voice', 'Voice'
    VIDEO = 'video', 'Video'
    AUDIO = 'audio', 'Audio'
    DOCUMENT = 'document', 'Document'

class Function(models.Model):
    project = models.ForeignKey(Project, related_name='functions', on_delete=models.CASCADE, verbose_name='Project')
    text = models.CharField(max_length=255, verbose_name='Function Text', blank=True, null=True)
    type = models.CharField(max_length=10, choices=FunctionType.choices, verbose_name='Function Type', default=FunctionType.TEXT)
    file_id = models.CharField(max_length=255, verbose_name='File ID', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')


class ComfortTime(models.Model):
    user = models.ForeignKey('users.User', related_name='comfort_times', on_delete=models.CASCADE, verbose_name='User')
    time = models.TimeField(verbose_name='Qulay Vaqt')


class Plan(models.Model):
    project = models.ForeignKey(Project, related_name='plans', on_delete=models.CASCADE, verbose_name='Project')
    text = models.CharField(max_length=255, verbose_name='Plan Text')
    start_date = models.DateTimeField(verbose_name='Start Date', blank=True, null=True)
    end_date = models.DateTimeField(verbose_name='End Date', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    is_done = models.BooleanField(default=False, verbose_name='Is Done')
    def __str__(self):
        return self.text

