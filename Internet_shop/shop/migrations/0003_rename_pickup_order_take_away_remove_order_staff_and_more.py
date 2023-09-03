# Generated by Django 4.2.3 on 2023-09-03 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_productorder_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pickup',
            new_name='take_away',
        ),
        migrations.RemoveField(
            model_name='order',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='product',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='_amount',
        ),
        migrations.AddField(
            model_name='productorder',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_in', to='shop.product'),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
