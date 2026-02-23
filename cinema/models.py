from django.db import models

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    # Описываем поле, ссылающееся на модель OriginalTitle:
    original_title = models.OneToOneField(
        OriginalTitle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Связь с оригинальным названием; допускается пустое значение"
    )
    
class OriginalTitle(models.Model):
    title = models.CharField(max_length=128)