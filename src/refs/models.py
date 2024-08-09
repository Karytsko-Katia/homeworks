from django.db import models

# Create your models here.

# class Region(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(
#         blank=True,
#         null=True
#     )
#     def __str__(self):
#         return f"{self.pk} {self.name}"
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.name} #{self.pk}"
    
class Publishing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.name} #{self.pk}"  

class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.name} #{self.pk}"  

class Serie(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        default=1,
        related_name='series'
    )
    name = models.CharField(max_length=100)
    total_number = models.PositiveIntegerField()
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.name} #{self.pk}"  

class SeriesPrivately(models.Model):
    book_number = models.PositiveIntegerField()
    book_name = models.TextField()
    series_name = models.ForeignKey(
        Serie,
        on_delete=models.PROTECT,
        default=1,
        related_name='privately'
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    def __str__(self):
        return f"{self.book_number} {self.book_name} #{self.pk}"  


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

