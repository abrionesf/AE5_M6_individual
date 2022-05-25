# Generated by Django 4.0.4 on 2022-05-24 07:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_capitulo', models.IntegerField(blank=True, null=True)),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='capitulos')),
                ('video', models.FileField(upload_to='capitulos')),
                ('contenido', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='cursos')),
                ('video', models.FileField(upload_to='cursos')),
                ('slug', models.SlugField(max_length=250, unique=True, unique_for_date='publicado')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_leccion', models.IntegerField(blank=True, null=True)),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='lecciones')),
                ('video', models.FileField(upload_to='lecciones')),
                ('contenido', models.TextField(blank=True, null=True)),
                ('capitulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avirtual.capitulo')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avirtual.curso')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='autores',
            field=models.ManyToManyField(to='avirtual.tutor'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avirtual.curso'),
        ),
    ]