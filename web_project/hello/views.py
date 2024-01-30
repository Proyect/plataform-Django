from django.shortcuts import render, redirect
from hello.models import Person
from hello.forms import PersonEdidForm

def edit_person(request, pk):
    person = Person.objects.get(pk=pk)
    form = PersonEdidForm(request.POST or None, instance=Person)

    if request.request == "POST":
        if form.is_valid():
            form.save()
            return redirect("Person_list")
        
    context = {
        "form": form,
        "person":Person
    }
    return render(request,"person_edit.html")