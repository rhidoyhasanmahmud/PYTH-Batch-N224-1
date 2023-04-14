from django.shortcuts import render, redirect
from Book.forms import kitabform
from Book.models import kitab

def allbook(request):
    Books = kitab.objects.all()
    return render(request, "first.html",{
        'Books': Books
    })

def newbook(request):
    if request.method != "POST":
        form = kitabform()
    else:
        form = kitabform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            try:
                form.save()
                return redirect('/books')
            except:
                pass
    return render(request, "second.html", {"form":form})

def edit(request, id):
    Book = kitab.objects.get(id=id)
    return render(request, "edit.html", {"Book": Book})

def delete(request, id):
    pass

def update(request, id):
    Book = kitab.objects.get(id=id)
    form = kitabform(request.POST, instance = Book)
    print(form.is_valid())
    if form.is_valid():
        try:
            form.save()
            return redirect('/books')
        except:
            pass


    return render(request, "edit.html", {"form": form})


