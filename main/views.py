from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def show_page(request):
    return render(request, 'main/show.html')