from django.utils import timezone
from django.db    import models

class Post(models.Model):
    writer       = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title        = models.CharField(max_length=200)
    desc         = models.TextField()
    write_dt     = models.DateField(default=timezone.now)

    def publish(self):
        self.published_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title