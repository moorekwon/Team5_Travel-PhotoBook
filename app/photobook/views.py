from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from members.models import User
from photobook.forms import PhotoForm
from photobook.models import PhotoBook, Page


def page_create(request, photobook_pk):
    photobook = PhotoBook.objects.get(pk=photobook_pk)
    Page.objects.create(
        book=photobook
    )
    return render(request, 'page_1.html')


# def add_photo(request, page_pk, photo_num):
#     page = Page.objects.get(pk=page_pk)
#     pass
#     # if request.method =='POST':
#     # for i in photo_num:
#     #     Photo.objects.create(
#     #         photo_page=page,
#     #     )


def index(request):
    return render(request, 'index.html')


def album_create(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.user

        PhotoBook.objects.create(book_name=book_name, author=author)
        return redirect('page_1')

    return render(request, 'create_photobook.html')


def upload_image(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/photobook/create/')
    else:
        form = PhotoForm()
    return render(request, 'create_photobook.html', {'form': form})
