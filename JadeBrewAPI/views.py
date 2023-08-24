from django.shortcuts import render
from .forms import MenuForm
from .models import Menu
from django.http import JsonResponse

# Create the views.py

def form_view(request):

    form = MenuForm()
    
    if request.method == 'POST':
        form = MenuForm(request.POST)
        print(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            mf = Menu(
                item_name = cd['item_name'],
                category = cd['category'],
                description = cd['description']
            ).save()

            # mf.save()

            return JsonResponse({'message': 'success'})
        
    return render(request, 'menu_items.html', {'form': form})
