from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.shortcuts import render
from fossee4.forms import inputImages
from fossee4.models import Images


# argument: request 
# what it does:renders the front page 
# returns: returns the front page
def index(request):
    return render(request,"fossee4/index.html")

# argument:request
# what it does:take file as input from user , validate the requirements and save it in database
# returns:  unique id of the image
def uploadImage(request):
    form = inputImages()
    if request.method=="POST":
        form = inputImages(request.POST,request.FILES)
        message=''
        if form.is_valid():
            curr = form.save()
            unique_id=curr.pk
            message="successfully uploaded the image, above is your unique id returned by the api. please keep it for future reference"
        else :
            return render(request,"fossee4/uploadImage.html",{"form":form})
        return render(request,"fossee4/successful.html",{"message":message,"unique_id":unique_id})
    return render(request,"fossee4/uploadImage.html",{"form":form})

# argument:request
# what it does:get all the images from the database without any filters
# returns:a page with all those images
def getallImages(request):
    images = Images.objects.all()
    return render(request,"fossee4/getallImages.html",{"images":images})


# argument:request
# what it does:take the unique id from the user and filter the image from the database of that particular id
# returns:page displaying that image
def ImagebyId(request):
    if request.method == 'POST':
        uniqueId = request.POST.get('id')
        images = Images.objects.filter(pk = uniqueId)
        message=''
        if not images:
            message="No Image exists for the given id,please try with a different id:)"
            return render(request,"fossee4/successful.html",{"message":message})
        return render(request,"fossee4/getallImages.html",{"images":images,"message":message})

    return render(request,"fossee4/ImagebyId.html")

# argument:request
# what it does:take the name of the user who created the image  and filter the image from the database
# returns:page rendering those images
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


# argument:request
# what it does:take the id of the image from the user 
# returns:if user press update, it calls ImageUpdate function else it calls ImageDelete function
def doImageUpdate(request):
    if request.method == 'POST':
        uniqueId = request.POST.get('id')
        if request.POST.get('update')=='update':
            return HttpResponseRedirect(reverse('fossee4:ImageUpdate', kwargs={'uniqueId':uniqueId}))
        elif request.POST.get('delete')=='delete':
            return HttpResponseRedirect(reverse('fossee4:ImageDelete', kwargs={'uniqueId':uniqueId}))


    return render(request,"fossee4/doImageUpdate.html")

# argument:request
# what it does:since it is called by doImageUpdate function, it gets the unique id of the image 
#              from that function, it fetches the image from the database and saves the changes
#              as specified by the user.
# returns:page rendering current and saved changes
def ImageUpdate(request,uniqueId):
    image = Images.objects.filter(pk=uniqueId)
    if not image:
            message="No Image exists for the given id,please try with a different id:)"
            return render(request,"fossee4/successful.html",{"message":message})
    form = inputImages(instance=image[0])

    if request.method=="POST":
        form = inputImages(request.POST,request.FILES, instance=image[0])
        form.save()
        return render(request,"fossee4/updatedImage.html")
    return render(request,"fossee4/ImageUpdate.html",{"form":form,"uniqueId":uniqueId})


# argument:request
# what it does:since it is called by doImageUpdate function, it gets the unique id of the image 
#              from that function, it fetches the image from the database and deletes that particular
#              Image from the database
# returns:page rendering successfull deleted message or the error message in case image doesn't exist
def ImageDelete(request,uniqueId):
    image = Images.objects.filter(pk=uniqueId)
    if not image:
            message="No Image exists for the given id,please try with a different id:)"
            return render(request,"fossee4/successful.html",{"message":message})
    image.delete()
    return render(request,"fossee4/deletedImage.html")