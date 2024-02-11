from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class BaseModel(models.Model):
    """Base Model"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
