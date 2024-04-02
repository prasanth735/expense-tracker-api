from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Expense(models.Model):

    tilte=models.CharField(max_length=200)

    amount=models.PositiveIntegerField()

    expense_categories = (
        ("Housing", "Housing"),
        ("Transportation", "Transportation"),
        ("Food", "Food"),
        ("Health", "Health"),
        ("Entertainment", "Entertainment"),
        ("DebtPayments", "Debt Payments"),
        ("PersonalCare", "Personal Care"),
        ("Education", "Education"),
        ("Savings", "Savings"),
        ("Miscellaneous", "Miscellaneous")
    )
    
    category=models.CharField(max_length=200,choices=expense_categories,default="Miscellaneous")

    created_date=models.DateField(auto_now_add=True)

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    priority_categories=(

        ("need","need"),

        ("want","want")
    )

    priority=models.CharField(max_length=200,choices=priority_categories,default="need")

    def __str__(self):

        return self.tilte
    





