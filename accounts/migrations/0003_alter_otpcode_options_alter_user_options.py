# Generated by Django 5.0 on 2023-12-25 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_otpcode_alter_user_email_alter_user_full_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otpcode',
            options={'verbose_name': 'کد احراز هویت', 'verbose_name_plural': 'کدهای احراز هویت'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
    ]
