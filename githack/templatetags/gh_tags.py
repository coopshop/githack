from django import template
from githack.models import Badges
from githack.tools.toolbox import experience_required

register = template.Library()

@register.assignment_tag(takes_context=True)
def is_obtained(context, user, badge):

    obtained = False

    try:
        obtained = user.gitscore.badges.filter(id=badge.id).exists()

    except Exception:
        pass

    return 1 if obtained else 0

@register.assignment_tag(takes_context=False)
def experience_points(level):
    return experience_required(level)

@register.assignment_tag(takes_context=False)
def divide(value, arg, scale=1):
    return float(scale) * int(value) / int(arg)