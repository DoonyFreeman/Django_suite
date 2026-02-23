from django.db import models

class ProductType(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class OriginalTitle(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class VideoProduct(models.Model):
    title = models.CharField(max_length=128)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE
    )
    original_title = models.OneToOneField(
        OriginalTitle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Связь с оригинальным названием; допускается пустое значение"
    )

    # удобный доступ к режиссёрам через промежуточную таблицу
    directors = models.ManyToManyField(
        'Director',
        through='DirectorVideoProduct',
        related_name='video_products',
    )

    def __str__(self):
        return self.title


class Director(models.Model):
    full_name = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name


class DirectorVideoProduct(models.Model):
    video_product = models.ForeignKey(VideoProduct, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "director–video product relation"
        verbose_name_plural = "director–video product relations"
