# Generated by Django 4.1.5 on 2023-01-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='gene_id',
            field=models.CharField(db_index=True, max_length=256),
        ),
    ]