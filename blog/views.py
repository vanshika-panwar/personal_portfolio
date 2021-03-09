from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Blogs
# Create your views here.
def all_blogs(request):
    #blog_count = Blogs.objects.count
    blogs = Blogs.objects.order_by('-date')#[:5]#puts limit
    return render(request,'all_blogs.html',{'bb':blogs} )

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog})

# def temp(request):
#     return render(request,'temp.html')