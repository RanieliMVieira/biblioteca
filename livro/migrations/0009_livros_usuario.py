# Generated by Django 4.1.3 on 2022-11-29 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0008_livros_categoria_livros_editora'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
