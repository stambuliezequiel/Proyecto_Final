from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True,upload_to='usuario', default='usuario/user-default.png')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_name='usuario_set', 
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='usuario_permissions_set',
        related_query_name='usuario',
    )
    

    def get_absolute_url(self):
        return reverse('index')

   
