# Generated by Django 3.2.9 on 2021-12-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=10)),
                ('MGMT_type', models.IntegerField()),
                ('FLAIR_imgc', models.IntegerField()),
                ('T1w_imgc', models.IntegerField()),
                ('T2w_imgc', models.IntegerField()),
                ('T1wCE_imgc', models.IntegerField()),
            ],
        ),
    ]
