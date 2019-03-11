from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from fossee4.forms import inputImages
from fossee4.models import Images

# Create your views here.
def index(request):
    return render(request,"fossee4/index.html")

def uploadImage(request):
    form = inputImages()
    if request.method=="POST":
        form = inputImages(request.POST,request.FILES)
        form.save()

    return render(request,"fossee4/uploadImage.html",{"form":form})

def getallImages(request):
    images = Images.objects.all()
    return render(request,"fossee4/getallImages.html",{"images":images})


def ImagebyId(request):
    if request.method == 'POST':
        ide = request.POST.get('id')
        images = Images.objects.filter(ide = ide)
        return render(request,"fossee4/getallImages.html",{"images":images})

    return render(request,"fossee4/ImagebyId.html")

def ImagebyUser(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        print(user)
        images = Images.objects.filter(createdby = user)
        return render(request,"fossee4/getallImages.html",{"images":images})
    return render(request,"fossee4/ImagebyUser.html")

def doImageUpdate(request):
    if request.method == 'POST':
        ide = request.POST.get('id')
        if request.POST.get('update')=='update':
            return HttpResponseRedirect(reverse('fossee4:ImageUpdate', kwargs={'ide':ide}))
        elif request.POST.get('delete')=='delete':
            return HttpResponseRedirect(reverse('fossee4:ImageDelete', kwargs={'ide':ide}))


    return render(request,"fossee4/doImageUpdate.html")

def ImageUpdate(request,ide):
    image = Images.objects.get(ide=ide)
    print("is it calling")
    form = inputImages(instance=image)

    if request.method=="POST":
        form = inputImages(request.POST,request.FILES, instance=image)
        form.save()
        return render(request,"fossee4/updatedImage.html")
    return render(request,"fossee4/ImageUpdate.html",{"form":form,"ide":ide})


def ImageDelete(request,ide):
    image = Images.objects.get(ide=ide).delete()
    return render(request,"fossee4/deletedImage.html")