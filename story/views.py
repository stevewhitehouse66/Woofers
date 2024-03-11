from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def test_view(request):
    context = {
        'message': 'Hello, Django!'
    }
    return render(request, 'index.html', context)