from django.shortcuts import render

# Create your views here.
from taskapp.forms import ReviewForm
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render


class ReviewEmailView(FormView):
    template_name = 'taskapp/message.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        return redirect('alert')


def alertView(request):
    msg = "Thanks for the review!"
    return render(request, 'taskapp/alerts.html', {'msg': msg})