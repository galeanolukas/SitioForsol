from django.db import models
from django.utils import timezone

# Create your models here.

def subir_media(instance, filename):
	return "galeria/" + filename
	
def subir_file(instance, filename):
	return "archivos/" + filename

class Post(models.Model):
	opciones = (('Principal', 'Principal'),
                ('Noticias', 'Noticias'), 
				('Tutoriales', 'Tutos'),
				('Eventos', 'Eventos'),
                ('Proyectos', 'Proyectos'))
	#autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=80)
	categoria = models.CharField(max_length=30, choices=opciones)
	texto = models.TextField()
	imagen = models.FileField(upload_to='archivos/', null=True, blank=True)
	fecha_post = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return str([self.titulo, self.fecha_post])
		
class Media(models.Model):
	nombre = models.CharField(max_length=30)
	archivo = models.FileField(upload_to=subir_media, null=True, blank=True)
	
	def __str__(self):
		return self.nombre
		
	

	
	
