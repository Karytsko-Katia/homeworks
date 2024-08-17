from django.db import models
from django.urls import reverse, reverse_lazy

from refs.models import Author, Genre, Publishing, Serie

class Item(models.Model):
    title = models.CharField(
        verbose_name='Название книги',
        max_length=200
        )
    cover = models.ImageField(
        verbose_name='Фото обложки',
        upload_to='item_covers/%Y/%m/%d/'
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена, BYN',
        )
    author = models.ManyToManyField(
        Author,
        verbose_name='Автор',
        related_name='books',
        )
    series = models.ForeignKey(
        Serie,
        on_delete=models.SET_NULL,
        verbose_name='Название серии',
        related_name='books_in_seria',
        blank=True,
        null=True
        )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='books_in_genre',
        )
    publishing_year = models.PositiveSmallIntegerField(
        verbose_name='Год издания',
        blank=True,
        null=True
    )
    pages = models.PositiveIntegerField(
        verbose_name='Количество страниц',
        blank=True,
        null=True
    )
    binding = models.CharField(
        verbose_name="",
        default='Твердый',
        max_length=200,
        blank=True,
        null=True
        )
    format = models.CharField(
        max_length=100,
        default='70x90/16',
        verbose_name="Формат",
        blank=True,
        null=True
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=13,
        blank=True,
        null=True
        )
    weight = models.PositiveSmallIntegerField(
        default=15,
        verbose_name='Вес, гр'
    )
    age_restrictions = models.CharField(
        max_length=5,
        verbose_name='Возрастные ограничения',
        blank=True,
        null=True
    )
    publishing = models.ForeignKey(
        Publishing,
        on_delete=models.SET_NULL,
        verbose_name='Издательство',
        related_name='books_published',
        blank=True,
        null=True
        )
    item_in_stock = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Количество книг в наличии'
    )
    active = models.BooleanField(
        default=True,
        verbose_name='Достуно для заказа'
    )
    rating = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Рейтинг'
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата внесения в каталог'
        )
    date_last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения карточки'
        )

    def __str__(self):
        return f"#{self.pk} {self.title}" 
    
    def get_absolute_url (self):
        return reverse_lazy("goods:item-detail", kwargs={"pk":self.pk})

