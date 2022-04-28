from crudbuilder.abstract import BaseCrudBuilder
from app.models import Drink

class DrinkCrud(BaseCrudBuilder):
    model = Drink
    search_fields = ['size']
    tables2_fields = ('size', 'price', 'order_date', 'quantity', 'category')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    login_required=False
    permission_required=False

