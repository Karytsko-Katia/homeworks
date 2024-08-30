from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

# Create your models here.

User = get_user_model()

class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile", 
        on_delete=models.CASCADE
        )
    delivery_address = models.CharField(
        max_length=500, 
        verbose_name="Адрес доставки",
        blank=True,
        null=True
        )
    phone_number = models.CharField(
        max_length=15, 
        default="+375",
        verbose_name="Номер телефона"
        )
    add_inform = models.CharField(
        max_length=300, 
        verbose_name="Дополнительная информация",
        blank=True,
        null=True
        )
    
    def __str__(self):
        return f"{self.user.username} {self.phone_number} profile" 
