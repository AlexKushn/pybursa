from django.shortcuts import render
from coaches.models import Coach


def coaches_list(request):
    coaches = Coach.objects.all()
    page_title = 'coaches list'
    return render(request, 'coaches/list.html', {'coaches': coaches,
                                                 'title': page_title})


def coaches_item(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    page_title = 'couch item'
    return render(request, 'coaches/item.html', {'coach': coach,
                                                 'title': page_title})