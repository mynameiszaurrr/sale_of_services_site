# Generated by Django 3.2.15 on 2022-09-14 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paypage', '0004_alter_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAPI',
            fields=[
                ('api_id', models.CharField(help_text='API ID продукта', max_length=100, verbose_name='API ID')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='paypage.item')),
            ],
        ),
    ]
