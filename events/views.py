from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from authentication.forms import organizerForm
from functools import wraps
from django.contrib import messages
from authentication.models import User, Organizer
from .forms import *
from .models import *
import os 
from django.shortcuts import (
    HttpResponseRedirect,
    get_object_or_404,
    get_list_or_404,
    redirect,
    render,
)
from django.conf import settings

@login_required
def createEventView(request):
    categories = Categories.objects.all()

    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            event = form.save(commit=False)
            event.organizer = user
            event.save()
            # event = Events.objects.create(
            #     organizer = user,
            #     eventName = request.POST["eventName"],
            #     eventDescription = request.POST["eventDescription"],
            #     payment = request.POST["payment"],
            #     eventCategories = request.POST["eventCategories"],
            #     eventStartDate = request.POST["eventStartDate"],
            #     eventEndDate = request.POST["eventEndDate"],
            #     eventStartTime = request.POST["eventStartTime"],
            #     eventEndTime = request.POST["eventEndTime"],
            #     eventType = request.POST["eventType"],
            #     venue = request.POST["venue"],
            #     eventCity = request.POST["eventCity"],

            # )
            if event:
                messages.success(request, f"Event created successfully.",extra_tags="success")
                return redirect('events-list')
            else:
                messages.error(request, f"Internal error occured! Tru again in a few.",extra_tags="danger")

        else:
            context={
                "form":form,
                "categories": categories,
            }
            return render(request, 'events/create_event.html',context)

    form = createEventForm()
    context = {
        "categories": categories,
        "form":form,
    }
    return render(request, 'events/create_event.html',context)



@login_required
def eventsListView(request):

    try:
        events = Events.objects.filter(organizer=request.user.id)
        context ={
            'events':events,
        }

    except Exception as e:
        messages.error(request, f"Error occured while fetching data from database", extra_tags='danger')
        return redirect('organizer-home')

    return render(request, 'events/events_list.html',context)










@login_required
# @organizerIsSetup
def eventsDetailView(request, id):
    obj = get_object_or_404(Events, id=id)
    dire = Events.objects.filter(organizer=request.user.id)
    org = get_object_or_404(Organizer, organizer=request.user.id)
    img = Images.objects.filter(event=obj.id)
    if request.POST and request.POST.get("add-image", None):
        url = request.get_full_path()
        newUrl = url.split('/')
        urlID = int(newUrl[len(newUrl)-1])
        addEventImages(request,urlID)
        return redirect('event-details', id)
    if request.POST and request.POST.get("updateImage", None):
        url = request.get_full_path()
        newUrl = url.split('/')
        urlID = int(newUrl[len(newUrl)-1])
        updateEventImage(request,urlID)
        return redirect('event-details', id)
    if img:
        first = img[0].image
    else:
        first =None
    if obj in dire:
        form = createEventForm(request.POST or None,request.FILES or None, instance=obj)
        # form2 = ImagesForm(request.POST or None, instance=img)
        if request.method=="POST":


            if form.is_valid():
                event = form.save(commit=False)
                user = User.objects.get(username=request.user.username)
                event.organizer=user
                event.save()
                messages.success(request, f'The Event has been updated!',extra_tags="success")
                url = request.get_full_path()
                # this = url.replace('update', '')
                return redirect('event-details',obj.id)
        context = {
            'form': form,
            'img':img,
            'first':first
        }
        return render(request, "events/events_detail.html", context)
    else:
        messages.warning(
            request, f'You have no authorization to access or edit other events!',extra_tags="warning")
        return redirect ('events-list')




def addEventImages(request,newUrl):
    try: 
        images = request.FILES.getlist('eventImages')
        event = Events.objects.get(id=newUrl)
        for image in images:
            if image.size > 15728640 :
                messages.error(request,"Maximum allowed size for image is 15MB.",extra_tags="danger")
                return redirect('event-details' ,newUrl)

            
            reversedName = image.name [::-1]
            extension = reversedName.split('.')[0]
            ext = extension[::-1]

            if not ext in settings.IMAGE_EXT:
                messages.error(request,"File type not supported! Please upload only:  .jpg, .jpeg, .png format files.",extra_tags="danger")
                return redirect('event-details' ,newUrl)  
            Images.objects.create(
                event = event,
                image = image
            )
        messages.success(request, "Images added successfully!", extra_tags="success")
    except Exception as e:
        messages.error(request, "Error occured during your upload. Make sure file format is of PNG, JPEG, or JPG",extra_tags="danger")
        return redirect('event-details' ,newUrl)







def updateEventImage(request,newUrl):
    try: 
        image = request.FILES['updatedEventImage']
        id = request.POST['id']
        before = Images.objects.get(id=id)


        if image.size > 15728640 :
            messages.error(request,"Maximum allowed size for image is 15MB.",extra_tags="danger")
            return redirect('event-details' ,newUrl)

        reversedName = image.name [::-1]
        extension = reversedName.split('.')[0]
        ext = extension[::-1]

        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq", image.size)

        if not ext in settings.IMAGE_EXT:
            messages.error(request,"File type not supported! Please upload only:  .jpg, .jpeg, .png format files.",extra_tags="danger")
            return redirect('event-details' ,newUrl)

        os.remove(before.image.path)
        before.image = request.FILES['updatedEventImage']
        before.save()
        messages.success(request, "Images updated successfully!", extra_tags="success")
    except Exception as e:
        messages.error(request, "Error occured during your upload. Make sure file format is of PNG, JPEG, or JPG",extra_tags="danger")
        return redirect('event-details' ,newUrl)