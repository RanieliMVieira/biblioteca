from django import template
from datetime import datetime

register = template.Library()

@register.filter
def mostra_duracao(data1, data2):
    if isinstance(data1, datetime) and isinstance(data2, datetime):
        dias = (data1 - data2).days
        texto = 'Dias'
        if dias == 1:
            texto = 'Dia'
        return f"{dias} {texto}"

    return "Ainda não foi devolvido"