from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from rest_framework import generics
from khanto.forms.anuncio_form import AnuncioForm
from khanto.models import Anuncio
from khanto.serializers import AnuncioSerializer
from django.views.generic import View

class AnuncioList(generics.ListAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    
    def get(self, request):
        anuncios = Anuncio.objects.all()
        return render(request, 'anuncios/templates/list.html', {'anuncios': anuncios})

class AnuncioDetail(generics.RetrieveAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

class AnuncioCreateView(generics.CreateAPIView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/templates/anuncio_create.html'
    success_url = 'anuncio-list'
    serializer_class = AnuncioSerializer

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class AnuncioUpdateView(generics.UpdateAPIView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/templates/anuncio_update.html' 
    success_url = reverse_lazy('anuncio-list')
    serializer_class = AnuncioSerializer
    
    def get(self, request, *args, **kwargs):
        anuncio = get_object_or_404(Anuncio, pk=self.kwargs['pk'])
        form = self.form_class(instance=anuncio)
        return render(request, self.template_name, {'form': form, 'anuncio': anuncio})

    
    def post(self, request, *args, **kwargs):
        anuncio = get_object_or_404(Anuncio, pk=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=anuncio)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'anuncio': anuncio})

