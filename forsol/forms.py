from django.forms import ModelForm,  Form, EmailField, CharField, Textarea
from .models import Post, Media

class FormPost(ModelForm):
	
	class Meta:
		model = 	Post
		fields = ('titulo', 'categoria', 'texto', 'imagen')	
		
class FormSubirMedia(ModelForm):
	class Meta:
		model  = Media
		fields = ('nombre', 'archivo')

class ContactoForm(Form):
    Correo = EmailField(required=True)
    Nombre = CharField(required=True)
    Mensaje = CharField(widget=Textarea, required=True)
