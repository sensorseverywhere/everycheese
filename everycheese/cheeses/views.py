from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese


class CheeseDetailView(DetailView):
    model = Cheese


#LoginRequired on left for reasons of 'method resolution order'
class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = [
        "name",
        "description",
        "firmness",
        "country_of_origin",
    ]