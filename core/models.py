from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField("Título", max_length=100)
    text = models.TextField("Texto", null=True, blank=True)
    image = models.ImageField("Imagem", upload_to='institute/', null=True, blank=True)
    created_date = models.DateTimeField("Data de criação", auto_now_add=True)
    updated_date = models.DateTimeField("Data de edição", auto_now=True)

    class Meta:
        ordering = ['-updated_date']
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.title
