
from django.shortcuts import render, get_object_or_404, redirect
from .models import Roast, BrewEntry
from django.contrib.auth.decorators import login_required
from .forms import BrewEntryForm
from django.core.paginator import Paginator
from django.db.models import Count
from .forms import RoastForm
from django.core.exceptions import PermissionDenied
from django.http import Http404

def roast_list(request):
    roasts = Roast.objects.select_related("coffee_shop").all()
    latest_entries = BrewEntry.objects.select_related('user','roast').order_by("-date_created")[:12]
    gifting_roasts = Roast.objects.filter(is_good_to_gift=True)
    availability = request.GET.get("availability", "")
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

    if availability == "available":
        roasts = roasts.filter(is_available=True)
    


    return render(
        request, 
        "roasts/roast_list.html", 
        {"roasts": roasts,
        "gifting_roasts": gifting_roasts,
          "profile": profile,
          "crowd": crowd,
          "sort": sort,
          "latest_entries": latest_entries,
          "availability": availability})



def roast_details(request, pk):
    roast = get_object_or_404(Roast, pk=pk) 
    entries = roast.brew_entries.all().order_by("-date_created") 
    return render(
        request, 
        "roasts/roast_details.html", 
        {"roast": roast, "most_common_brew_method": roast.most_common_brew_method(), "entries": entries})


@login_required
def brewentry_create(request):
    if request.method == "POST":
        form = BrewEntryForm(request.POST)
        if form.is_valid():
            brew_entry = form.save(commit=False) 
            brew_entry.user = request.user 
            brew_entry.save() 
            return redirect("brewentry_detail", pk=brew_entry.pk) 
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
    return render(
        request, 
        "coffee_app/brewentry_detail.html",
        {"entry": entry}
    )

@login_required
def brewentry_update(request, pk): 
    instance = ""
    # if request.user.is_staff or request.user.is_superuser:
    # print(request.user)
    # print(f"PK: {pk}")
    instance = get_object_or_404(BrewEntry, pk=pk)
    # else:
    # instance = get_object_or_404(BrewEntry, pk=pk, user=request.user)
    # print(instance)
    if request.method == "POST":
        form = BrewEntryForm(request.POST, instance=instance)
        print("did you get here")
        print(form.is_valid())
        if form.is_valid():
            print("how about here?")
            form.save()

            if request.user.is_staff:
                return redirect("community")
            else:
                return redirect("brewentry_list")
    else:
        form = BrewEntryForm(instance = instance) 

    return render(
        request,
        "coffee_app/brewentry_update.html",
        {"form": form}

    )
    
@login_required 
def brewentry_delete(request, pk):
    if request.user.is_staff or request.user.is_superuser: 
        entry = get_object_or_404(BrewEntry, pk=pk)
    else:
        entry = get_object_or_404(BrewEntry, pk=pk, user=request.user)
     

    if request.method == "POST":
        entry.delete()
        if request.user.is_staff:
            return redirect("community")
        else:
            return redirect("brewentry_list")
    return render(
        request,
        "coffee_app/brewentry_delete.html",
        {"entry": entry}
    )


def community(request): 
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
            return redirect("roast_list")  
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
