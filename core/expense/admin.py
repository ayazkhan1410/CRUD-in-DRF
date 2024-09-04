from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Transactions)
class AdminTransactions(admin.ModelAdmin):
    list_display = ('title', 'amount', 'trans_type')
    list_per_page = 10
    