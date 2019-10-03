from django import template
from django.utils.safestring import mark_safe
register = template.Library() 

@register.simple_tag
def youtube_tag(link):
    return mark_safe('<div class="video-box"><iframe src="%s"></iframe></div>' % link)

@register.simple_tag
def imagen_tag(img):
    return mark_safe('<div class="imagen"><img src="/media/%s"></div>' % img)

@register.simple_tag
def galeria_tag(fotos):
    for img in fotos:
        grupo = '<div><div id="titulo">%s</div><table>' % img.nombre
        screen = '''<a href="{% url '%s' %}"><img src="{% url '%s' %}"/></a>''' % (img.archivo.url, img.archivo.url)
        grupo + '</tr><tr><td>%s</td></tr>' % screen
    grupo + "</table></div>"
    return mark_safe(grupo)

@register.simple_tag
def codigo_tag(*args):
    return mark_safe('<code style="{font-family: monospace; background-color:gray;}">%s</code>')

@register.simple_tag
def render_posttag(var):
    result = '''{% autoescape off %}<div id="titulo">{{ %s.titulo }}</div></div><BR>
{{ %s.texto }}
{% if post.imagen %}<img src="{{ %s.imagen.url }}">{% endif %}{% endautoescape %}''' % (var, var, var)
    return mark_safe(result)