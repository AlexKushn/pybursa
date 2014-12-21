from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from coaches.models import Coach


class CoachModelForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Coach
        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'teacher',
                  'user', 'dossier']


def coaches_list(request):
    coaches = Coach.objects.all()
    page_title = 'coaches list'
    return render(request, 'coaches/list.html', {'coaches': coaches,
                                                 'title': page_title})


def coaches_item(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    page_title = 'couch item'
    return render(request, 'coaches/item.html', {'coach': coach,
                                                 'title': page_title})


def coach_edit(request, coach_id):
    title = "Coach edit item"
    coach = get_object_or_404(Coach, id=coach_id)
    if request.method == 'POST':
        form = CoachModelForm(request.POST, instance=coach)
        if form.is_valid():
            coach = form.save()
            return redirect('coach-edit', coach.id)
    else:
        form = CoachModelForm(instance=coach)
    return render(request, 'coaches/edit.html',
                  {'form': form, 'title': title})


def coach_add(request):
    title = "Coach add item"
    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
            coach = form.save()
            return redirect('coach-edit', coach.id)
    else:
        form = CoachModelForm()
    return render(request, 'coaches/edit.html',
                  {'form': form, 'title': title})


def coach_delete(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    coach.delete()
    return redirect('coaches-list')