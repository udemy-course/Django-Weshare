from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import MyUserCreationForm


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')


def register(request):
    if request.method == 'POST':
        user_form = MyUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1']
            )
            new_user.save()
            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user}
            )
    else:
        user_form = MyUserCreationForm()
    return render(
        request,
        'account/register.html',
        {'user_form': user_form}
    )


@login_required
def profile(request, username):
    user = User.objects.filter(username=username).first()
    return render(
        request, 'account/profile.html',
        {'user': user}
    )
