from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def register_student(request):
  if request.method == 'POST':
    form = StudentRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('success_page')  # Redirect to success page after saving
  else:
    form = StudentRegistrationForm()
  return render(request, 'registration_form.html', {'form': form})
