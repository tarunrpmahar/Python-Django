# Generated by Django 3.1.3 on 2020-11-14 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://lh3.googleusercontent.com/proxy/i6MxMUVrUmfPztimRyLkJe8Vf3_-oJdxnivTDGwJaG-k7rqV4xP6T00e6e_uvhBcHafpQKBiP7XhhE6BOICZXPVZdftMEcijVOKVGO7PljydnzuoaRyWIYFV5Ncb', max_length=500),
        ),
    ]
