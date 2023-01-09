from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import generics
from .forms import ImovelForm
from .models import Imovel
from .serializers import ImovelSerializer
from django.views.generic import DeleteView, View


class ImovelList(generics.ListAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    
    def get(self, request):
        imoveis = Imovel.objects.all()
        return render(request, 'imovel_list.html', {'imoveis': imoveis})

class ImovelDetail(generics.RetrieveAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ImovelCreateView(generics.CreateAPIView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_create.html'
    success_url = 'imovel-list'
    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class ImovelUpdateView(generics.UpdateAPIView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel_update.html' 
    success_url = 'imovel-list'
    serializer_class = ImovelSerializer
    
    def get(self, request, *args, **kwargs):
        imovel = get_object_or_404(Imovel, pk=self.kwargs['pk'])
        form = self.form_class(instance=imovel)
        return render(request, self.template_name, {'form': form, 'imovel': imovel})

    
    def post(self, request, *args, **kwargs):
        imovel = get_object_or_404(Imovel, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'imovel': imovel})


class ImovelDeleteView(DeleteView):
    model = Imovel
    template_name = 'imovel_update.html'
    success_url = 'imovel-list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imovel'] = self.get_object()
        return context

    def get(self, request, *args, **kwargs):
        imovel = get_object_or_404(Imovel, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'imovel': imovel})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)

class ImovelSearchView(View):
    def get(self, request):
        codigo_imovel = request.GET.get('codigo_imovel')
        imoveis = Imovel.objects.filter(codigo_imovel=codigo_imovel)
        return render(request, 'imovel_search_results.html', {'imoveis': imoveis})


