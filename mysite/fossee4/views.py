from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.shortcuts import render
from fossee4.forms import inputImages
from fossee4.models import Images

# front page
def index(request):
    return render(request,"fossee4/index.html")


def uploadImage(request):
    form = inputImages()
    if request.method=="POST":
        form = inputImages(request.POST,request.FILES)
        message=''
        if form.is_valid():
            form.save()
            message='successfully uploaded, please go back to the main page to use other functionalities of api'
        else :
            return render(request,"fossee4/uploadImage.html",{"form":form})
        return render(request,"fossee4/successful.html",{"message":message})
    return render(request,"fossee4/uploadImage.html",{"form":form})

def getallImages(request):
    images = Images.objects.all()
    return render(request,"fossee4/getallImages.html",{"images":images})


def ImagebyId(request):
    if request.method == 'POST':
        uniqueId = request.POST.get('id')
        images = Images.objects.filter(uniqueId = uniqueId)
        message=''
        if not images:
            message="No Image exists for the given id,please try with a different id:)"
            return render(request,"fossee4/successful.html",{"message":message})
        return render(request,"fossee4/getallImages.html",{"images":images,"message":message})

    return render(request,"fossee4/ImagebyId.html")

def ImagebyUser(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        print(user)
        images = Images.objects.filter(createdby = user)
        if not images:
            message="No Image is created by the this user,please try with a different name:)"
            return render(request,"fossee4/successful.html",{"message":message})
        return render(request,"fossee4/getallImages.html",{"images":images})
    return render(request,"fossee4/ImagebyUser.html")

def doImageUpdate(request):
    if request.method == 'POST':
        uniqueId = request.POST.get('id')
        if request.POST.get('update')=='update':
            return HttpResponseRedirect(reverse('fossee4:ImageUpdate', kwargs={'uniqueId':uniqueId}))
        elif request.POST.get('delete')=='delete':
            return HttpResponseRedirect(reverse('fossee4:ImageDelete', kwargs={'uniqueId':uniqueId}))


    return render(request,"fossee4/doImageUpdate.html")

def ImageUpdate(request,uniqueId):
    image = Images.objects.filter(uniqueId=uniqueId)
    if not image:
            message="No Image exists for the given id,please try with a different id:)"
            return render(request,"fossee4/successful.html",{"message":message})
    form = inputImages(instance=image[0])

    if request.method=="POST":
        form = inputImages(request.POST,request.FILES, instance=image[0])
        form.save()
        return render(request,"fossee4/updatedImage.html")
    return render(request,"fossee4/ImageUpdate.html",{"form":form,"uniqueId":uniqueId})


def ImageDelete(request,uniqueId):
    image = Images.objects.filter(uniqueId=uniqueId)
    if not image:
            message="No Image exists for the given id,please try with a different id:)"
            return render(request,"fossee4/successful.html",{"message":message})
    image.delete()
    return render(request,"fossee4/deletedImage.html")