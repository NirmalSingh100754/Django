from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import ChaiVarity

# Create your views here.
def all_nirmal(request):
    chais=ChaiVarity.objects.all()
    return render(request,'nirmal/all_nirmal.html',{'chais':chais})

def order(request):
    return render(request, 'order.html')
def chai_desc(requset, chai_id):
    chai=get_object_or_404(ChaiVarity, pk=chai_id)
    return render(requset, 'nirmal/chai_details.html', {'chai': chai})