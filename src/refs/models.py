from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.pk} {self.name}"
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.pk} {self.name}"
    
class Publishing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.pk} {self.name}"  

# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     author = models.ForeignKey(
#         Author,
#         on_delete=models.PROTECT,
#         related_name='books'
#         )
#     publishing = models.ForeignKey(
#         Publishing,
#         on_delete=models.PROTECT,
#         related_name='books'
#         )
#     genre = models.ForeignKey(
#         Genre,
#         on_delete=models.PROTECT,
#         related_name='books'
#         )
#     series = models.TextField(
#         blank=True,
#         null=True
#         )
#     description = models.TextField(
#         blank=True,
#         null=True
#     )
#     price = models.DecimalField()
#     number = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.pk} {self.name}" 

