from django import template

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css_addition):
    css_classes = field.field.widget.attrs.get('class', '')
    return field.as_widget(attrs={"class": "%s %s" % (css_classes, css_addition)})



