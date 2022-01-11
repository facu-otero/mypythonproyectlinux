from django import template
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def saluda(req):
    
    return HttpResponse("Hi! World")

def despedirse(req):
    
    return HttpResponse("""
                        
    <h3>Chau, Gracias por visitarnos!</h3>                 
                        
                        """
    )
    
def saluda_con_nombre(req, nombre):
    texto = f'Hola {nombre}, como estas?'
    return HttpResponse (texto)

def saluda_con_template(req):
    mi_dic = {
        "nombre": "Facundo",
        "apellido": "Otero",
        "ahora": datetime.now()
        
    }
    mi_html = open("/home/facundo/django/proyecto1/proyecto1/plantillas/template1.htm")
    mi_plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(mi_dic)
    documento = mi_plantilla.render(mi_contexto)
    return HttpResponse(documento)
    