from django.shortcuts import render

# Create your views here.
def all_nirmal(request):
    return render(request,'nirmal/all_nirmal.html')

def order(request):
    return render(request, 'order.html')