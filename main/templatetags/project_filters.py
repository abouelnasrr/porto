from django import template

register = template.Library()

@register.filter
def dictify(value):
    """Convert a Project object to a dictionary."""
    if hasattr(value, 'id'):
        return {
            'id': value.id,
            'name': value.name,
            'description': value.description,
            'duration': value.duration,
        }
    return {}
