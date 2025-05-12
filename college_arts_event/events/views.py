from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Event, Participant, Result
from .forms import EventForm, RegistrationForm, ResultForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def home(request):
    events = Event.objects.all()
    return render(request, 'main/home.html', {'events': events})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'main/create_event.html', {'form': form})


@login_required
def participate(request, event_id):
    event = Event.objects.get(id=event_id)
    Participant.objects.create(user=request.user, event=event)
    return redirect('home')


@login_required
def submit_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ResultForm()
    return render(request, 'main/submit_result.html', {'form': form})
