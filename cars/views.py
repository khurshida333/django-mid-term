from django.shortcuts import render,redirect
from . import forms
from.import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views import View


from django.views.generic import CreateView
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class AddCarCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_cars.html' #render
    success_url = reverse_lazy('Profile') #redirect

    def form_valid(self, form):
        form.instance.author = self.request.user
        print("Form is valid. File: ", self.request.FILES)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid. Errors: ", form.errors)
        return self.render_to_response(self.get_context_data(form=form))

from django.views.generic import UpdateView
@method_decorator(login_required, name='dispatch')
class EditCarUpdateView(UpdateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_cars.html' #render
    success_url = reverse_lazy('Profile') #redirect
    pk_url_kwarg = 'id'
    

from django.views.generic import DeleteView
@method_decorator(login_required, name='dispatch')
class CarDeleteView(DeleteView):
    model = models.Car
    template_name = 'delete_cars.html' #render
    success_url = reverse_lazy('Profile') #redirect
    pk_url_kwarg = 'id'

from django.views.generic import DetailView

class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        car = self.object #post model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

@login_required
def buy_car(request, car_id):
    car = models.Car.objects.get(id=car_id)
    
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        car.buyers.add(request.user)  # Add the user to the buyers
        messages.success(request, "Car purchased successfully!")
    else:
        messages.error(request, "Sorry, this car is out of stock.")
    
    return redirect('details_cars',id=car.id) 