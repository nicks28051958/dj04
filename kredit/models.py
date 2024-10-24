from django.db import models

class Kredit(models.Model):
    bank_name = models.CharField(max_length=100)
    credit_name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    credit_char = models.CharField(max_length=250)

    def __str__(self):
        return self.bank_name
