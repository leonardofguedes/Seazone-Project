from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from rest_framework import generics
from khanto.models import Reserva
from khanto.serializers import ReservaSerializer
from khanto.forms.reserva_form import ReservaForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import DeleteView


class ReservaList(generics.ListAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    
    def get(self, request):
        reservas = Reserva.objects.all()
        return render(request, 'reservas/templates/list.html', {'reservas': reservas})


class ReservaCreateView(generics.CreateAPIView):
    form_class = ReservaForm
    template_name = 'reservas/templates/create.html'
    success_url = 'reserva-list'
    serializer_class = ReservaSerializer
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            checkin = form.cleaned_data.get('checkin')
            checkout = form.cleaned_data.get('checkout')
            if checkin >= checkout:
                return render(request, self.template_name, {'form': form, 'error': 'Data de check-in deve ser anterior à data de check-out'})
            form.save()
            return redirect(reverse('reserva-list'))
        return render(request, self.template_name, {'form': form})


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reservas/templates/delete.html'
    success_url = reverse_lazy('reserva-list')
    
    def get(self, request, *args, **kwargs):
        reserva = get_object_or_404(Reserva, pk=self.kwargs['codigoReserva'])
        return render(request, self.template_name, {'reserva': reserva})
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)
