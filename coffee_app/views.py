#COFFEE APP VIEWS
#COFFEE APP
#COFFEE APP
#COFFEE APP

from django.shortcuts import render, get_object_or_404, redirect
from .models import Roast, BrewEntry
from django.contrib.auth.decorators import login_required
from .forms import BrewEntryForm
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import RoastForm
from django.core.exceptions import PermissionDenied
from django.http import Http404


#render list of roasts for user, including filter options 

def roast_list(request):
    roasts = Roast.objects.select_related("coffee_shop").all()
    # featured_roasts = Roast.objects.order_by('-id')[:5] #last five added- maybe use later
    latest_entries = BrewEntry.objects.select_related('user','roast').order_by("-date_created")[:12]
    gifting_roasts = Roast.objects.filter(is_good_to_gift=True)
    profile = request.GET.get("profile",'')
    crowd = request.GET.get("crowd", '')
    sort = request.GET.get("sort", '')

    if profile:
        roasts = roasts.filter(profile=profile)

    if crowd:
        roasts = roasts.filter(crowd=crowd)

    if sort == "popular":
        roasts = roasts.annotate(
            brew_count=Count("brew_entries")
        ).order_by("-brew_count")



    return render(
        request, 
        "roasts/roast_list.html", 
        {"roasts": roasts,
        #  "featured_roasts": featured_roasts,
        "gifting_roasts": gifting_roasts,
          "profile": profile,
          "crowd": crowd,
          "sort": sort,
          "latest_entries": latest_entries})


#should a user click on one roast, render its details 

def roast_details(request, pk):
    roast = get_object_or_404(Roast, pk=pk) #primary key. get_object handles the 'doesn't exist' error gracefully. 
    entries = roast.brew_entries.all().order_by("-date_created") 
    return render(
        request, 
        "roasts/roast_details.html", 
        {"roast": roast, "most_common_brew_method": roast.most_common_brew_method(), "entries": entries})

######## BREW ENTRY CRUD BELOW #######

@login_required
def brewentry_create(request):
    if request.method == "POST":
        form = BrewEntryForm(request.POST)
        if form.is_valid():
            brew_entry = form.save(commit=False) #do not save yet
            brew_entry.user = request.user 
            brew_entry.save() 
            return redirect("brewentry_detail", pk=brew_entry.pk) #redirects to see the full details of the post #DOUBLECHECK brew_entry_detail
    else:
        form = BrewEntryForm()

    return render(
        request,
        "coffee_app/brewentry_form.html",
        {"form": form}
    )

@login_required 
def brewentry_list(request): 
    entries = BrewEntry.objects.filter(user=request.user)
    return render(
        request,
        "coffee_app/brewentry_list.html",
        {"entries": entries}
    )

@login_required
def brewentry_detail(request, pk): 
    entry = get_object_or_404(BrewEntry,  pk=pk) 
    # user=request.user was removed for community feed testing
    return render(
        request, 
        "coffee_app/brewentry_detail.html",
        {"entry": entry}
    )

@login_required
def brewentry_update(request, pk): 
    instance = get_object_or_404(BrewEntry, pk=pk, user=request.user)
    if request.method == "POST":
        form = BrewEntryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect("brewentry_list") #URL name not function
    else:
        form = BrewEntryForm(instance = instance) 

    return render(
        request,
        "coffee_app/brewentry_update.html",
        {"form": form}

    )
    
@login_required 
def brewentry_delete(request, pk): 
    entry = get_object_or_404(BrewEntry, pk=pk, user=request.user)
    if request.method == "POST":
        entry.delete()
        return redirect("brewentry_list")
    return render(
        request,
        "coffee_app/brewentry_delete.html",
        {"entry": entry}
    )
     

######## BREW ENTRY CRUD ABOVE ###### COMMUNITY FEED BELOW 


def community(request): # should return all community journal entries
    entries = BrewEntry.objects.all().order_by("-date_created")

    paginator = Paginator(entries, 10) 
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)


    return render(
        request, 
        "coffee_app/community.html", 
        {"page_object": page_object, 
         "show_empty_message": False, })


def is_staff_user(user):
    return user.is_staff


#staff create, update, delete roast:

@login_required
def roast_create(request):
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == "POST":
        form = RoastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("roast_list")
    else:
        form = RoastForm()

    return render(request, "roasts/roast_create.html", {"form": form})



@login_required
def roast_update(request, pk):
    if not request.user.is_staff:
        raise Http404

    roast = get_object_or_404(Roast, pk=pk)

    if request.method == "POST":
        form = RoastForm(request.POST, instance=roast)
        if form.is_valid():
            form.save()
            return redirect("roast_list")  # or wherever you want
    else:
        form = RoastForm(instance=roast)

    return render(request, "roasts/roast_form.html", {"form": form, "roast": roast})



@login_required
def roast_delete(request, pk):
    if not request.user.is_staff:
        raise Http404

    roast = get_object_or_404(Roast, pk=pk)

    if request.method == "POST":
        roast.delete()
        return redirect("roast_list")

    return render(request, "roasts/roast_confirm_delete.html", {"roast": roast})
