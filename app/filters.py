import django_filters
from app.models import Car

import logging

logger = logging.getLogger(__name__)


def get_fields(model):
    result = {}
    field_list = model._meta.get_fields()
    fields = []
    for field_name in field_list:
        fields.append(str(field_name).split('.')[-1])
    for field in fields:

        result[field] = [(v, v) for v in model.objects.all().order_by(
        ).values_list(field, flat=True).distinct()]
    logger.info(f'app - filters - get_fields result {result}')
    return result


class CarFilter(django_filters.FilterSet):

    brand = django_filters.ChoiceFilter(
        choices=get_fields(Car)['brand'], lookup_expr='iexact')
    model = django_filters.ChoiceFilter(
        choices=get_fields(Car)['model'], lookup_expr='iexact')

    release_year = django_filters.ChoiceFilter(
        choices=get_fields(Car)['release_year'], lookup_expr='iexact')

    class Meta:

        model = Car
        fields = ['model', 'brand', 'transmission', 'release_year']
