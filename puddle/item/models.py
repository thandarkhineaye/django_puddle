from django.db import models
from django.contrib.auth.models import User
# Category
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# Item
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, default=False)
    name = models.CharField(max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name