from django.shortcuts import render
from searchapp import func


def index(request):
    is_request = False
    if 'q' in request.GET and request.GET['q'] != '':
        is_request = True
        result = func.search_sentence(request.GET["q"])
        return render(request, 'index.html', context={"sentences": result, "check": is_request})
    else:
        return render(request, 'index.html')
