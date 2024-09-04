from typing import Iterable
from django.db import models

# Create your models here.
class Transactions(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    amount = models.FloatField()
    trans_type  = models.CharField(max_length=100,choices=(("DEBIT","DEBIT"), ("CREDIT","CREDIT")), null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.trans_type == "DEBIT":
            self.amount = self.amount * -1
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.title} - {self.trans_type}"