from Trialapp.forms import ReviewForm
from django.views.generic.edit import FormView
from django.shortcuts import render,redirect


# Create your views here.
class ReviewEmailView(FormView):
    template_name = 'Trialapp/message.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        return redirect('alert')
    
def alertView(request):
    msg = "Thanks For Your Review"
    return render(request,'Trialapp/alerts.html',{'msg':msg})