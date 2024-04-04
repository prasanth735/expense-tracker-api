# Generated by Django 5.0.1 on 2024-04-03 03:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_rename_tilte_expense_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Salary', 'Salary'), ('Business', 'Business'), ('Investment', 'Investment'), ('Rental', 'Rental'), ('Interest', 'Interest'), ('Dividend', 'Dividend'), ('Royalty', 'Royalty'), ('Capital', 'Capitat'), ('Pension', 'Pension'), ('SocialSecurity', 'SocialSecurity')], default='Salary', max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]