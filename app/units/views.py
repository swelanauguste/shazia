from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import UnitForm
from .models import Unit


class UnitListView(ListView):
    model = Unit

    def get_queryset(self):
        queryset = Unit.objects.all()
        query = self.request.GET.get("q")

        if query:
            return Unit.objects.filter(
                Q(description__icontains=query)
                | Q(location__name__icontains=query)
                | Q(condition__name__icontains=query)
                | Q(condition1__name__icontains=query)
                | Q(remarks__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UnitForm()
        return context


class UnitCreateView(CreateView):
    model = Unit
    form_class = UnitForm

    def get_success_url(self):
        return reverse_lazy("list")


class UnitUpdateView(UpdateView):
    model = Unit
    form_class = UnitForm


class UnitDetailView(DetailView):
    model = Unit
