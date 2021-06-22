from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django_prices_openexchangerates.currencies import CURRENCIES


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    avatar = models.ImageField(upload_to='images', default="images/default.png")
    currency = models.CharField(_('Currency'), default="USD",
                                max_length=5, choices=CURRENCIES)
    wallet_amount = models.FloatField(_('Wallet Amount'), default=0)


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


class Transaction(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                related_name="transaction_to_user")
    to_amount = models.FloatField(_('To Amount'), default=0)
    to_currency = models.CharField(_('To Currency'), default="USD",
                                   max_length=5, choices=CURRENCIES,)
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                  related_name="transaction_from_user")
    from_amount = models.FloatField(_('From Amount'), default=0)
    from_currency = models.CharField(_('From Currency'), default="USD",
                                     max_length=5, choices=CURRENCIES,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
