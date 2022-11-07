from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "workpage.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog_index_page.html")

def contact(request):
    return render(request, "contact.html")

def work(request):
    return render(request, "work_page.html")