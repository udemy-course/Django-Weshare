from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ImageForm
from .models import Image


@login_required
def image_upload(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            return render(request, 'image/image_upload_done.html')
    else:
        form = ImageForm()
    return render(request, 'image/image_upload.html', {
        'form': form
    })


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 12)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    return render(
        request,
        'image/image_list.html',
        {'images': images}
    )


@login_required
def image_detail(request, id, slug):
    image = Image.objects.filter(id=id, slug=slug).first()
    return render(
        request,
        'image/image_detail.html',
        {'image': image}
    )


@login_required
def image_like(request, id):
    image = Image.objects.get(id=id)
    image.user_like.add(request.user)
    return redirect('images:image_detail', id=id, slug=image.slug)


@login_required
def image_unlike(request, id):
    image = Image.objects.get(id=id)
    image.user_like.remove(request.user)
    return redirect('images:image_detail', id=id, slug=image.slug) 
