from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FachschaftUserForm


def index(request):
    messages.info(request, 'Info: Diese Seite befindet sich noch im Aufbau...')
    return render(request, 'fsmedhro_core/index.html')


@login_required
def user_profile(request, username):
    p_user = get_object_or_404(User, username=username)

    try:
        f_user = p_user.fachschaftuser
    except ObjectDoesNotExist:
        f_user = None
        if request.user == p_user:
            # wenn eigenes profil, aber noch kein Fachschaft-Profil, dann
            # bearbeiten/hinzufügen
            return redirect('fachschaft:fsmedhro_user_edit')

    context = {'p_user': p_user, 'f_user': f_user}

    return render(request, 'fsmedhro_core/user_profile.html', context)


@login_required
def user_self(request):
    return redirect('user_profile', username=request.user.username)


@login_required
def user_edit(request):
    if request.method == 'POST':
        try:
            # FachschaftUser bereits vorhanden?
            fuform = FachschaftUserForm(
                data=request.POST,
                instance=request.user.fachschaftuser
            )
        except ObjectDoesNotExist:
            fuform = FachschaftUserForm(data=request.POST)

        if fuform.is_valid():
            fuser = fuform.save(commit=False)
            fuser.user = request.user
            fuser.save()
            return redirect('user_profile', username=request.user.username)
    else:
        try:
            # FachschaftUser bereits vorhanden?
            fuform = FachschaftUserForm(instance=request.user.fachschaftuser)
        except ObjectDoesNotExist:
            fuform = FachschaftUserForm()

    return render(request, 'fsmedhro_core/user_edit.html', {'fuform': fuform})
