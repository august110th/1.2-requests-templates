from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(u'Название', max_length=64)
    price = models.IntegerField(u'Цена')
    image = models.ImageField(u'Изображение')
    release_date = models.DateField(u'Дата выпуска')
    lte_exist = models.CharField(u'Наличие LTE', max_length=3)
    slug = models.SlugField(u'Slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name