from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Bill, House


class BillsListView(generic.ListView):
    model = Bill
    template_name = 'bills/list.html'


class BillDetailView(generic.DetailView):
    model = Bill
    template_name = 'bills/detail.html'


def index(request):
    return HttpResponse(render(request, 'bills/index.html'))


class HouseListView(generic.ListView):
    model = House
    template_name = 'bills/houselist.html'


def housedetail(request, pk):
    house = get_object_or_404(House.objects.filter(pk=pk))
    bill_list = Bill.objects.filter(bill_house=house)
    bill_count = bill_list.count()
    context = {
        'house': house,
        'bill_list': bill_list,
        'bill_count': bill_count,
    }
    return render(request, 'bills/housedetail.html', context)


class BillUpdateView(generic.UpdateView):
    model = Bill
    template_name = 'bills/update.html'
    fields = [
        'bill_number',
        'bill_name',
        'bill_house',
        'bill_content',
        'date_first_posted',
    ]

    def form_valid(self, form):
        bill = form.save()
        return redirect('bills:detail', pk=bill.pk)


class BillCreateView(generic.CreateView):
    model = Bill
    template_name = 'bills/create.html'
    fields = [
        'bill_number',
        'bill_name',
        'bill_house',
        'bill_content',
        'date_first_posted',
    ]

    def form_valid(self, form):
        bill = form.save()
        return redirect('bills:detail', pk=bill.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'bill'
        return context


class HouseCreateView(generic.CreateView):
    model = House
    template_name = 'bills/create.html'
    fields = [
        'house_name',
        'house_code',
        'logo_url',
    ]

    def form_valid(self, form):
        bill = form.save()
        return redirect('bills:housedetail', pk=bill.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'house'
        return context


class HouseUpdateView(generic.UpdateView):
    model = House
    template_name = 'bills/update.html'
    fields = [
        'house_name',
        'house_code',
        'logo_url',
    ]

    def form_valid(self, form):
        bill = form.save()
        return redirect('bills:housedetail', pk=bill.pk)


class BillDeleteView(generic.DeleteView):
    model = Bill
    success_url = reverse_lazy('bills:list')


class HouseDeleteView(generic.DeleteView):
    model = House
    success_url = reverse_lazy('bills:houselist')


class BillSearchListView(generic.ListView):
    model = Bill
    template_name = 'bills/billsearch.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        result = Bill.objects.filter(Q(bill_name__contains=query) | Q(bill_content__contains=query)
                                     | Q(bill_number__contains=query))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


def guide(request):
    return render(request, 'bills/guide.html')
