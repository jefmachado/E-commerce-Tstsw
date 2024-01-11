from django.db import models

class BaseModels(models.Model):

    class Meta:
        abstract = True
        app_label = 'app_ecommerce'
