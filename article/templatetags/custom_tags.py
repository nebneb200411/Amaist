from django import template
register = template.Library()


@register.filter
def sort_by(queryset, order):
    return queryset.order_by('-created_at')

@register.simple_tag
def count_good(article):
    evaluators = article.good_from.all()
    good_num = evaluators.count()
    return good_num
