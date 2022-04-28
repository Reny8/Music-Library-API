# Generated by Django 4.0.4 on 2022-04-28 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_remove_song_album_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album_image',
            field=models.CharField(default='https://icon-library.com/images/no-image-available-icon/no-image-available-icon-26.jpg', max_length=300),
            preserve_default=False,
        ),
    ]