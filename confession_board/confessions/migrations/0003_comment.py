# Generated by Django 4.2.6 on 2023-10-15 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confessions', '0002_rename_content_confession_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('confession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confessions.confession')),
            ],
        ),
    ]
