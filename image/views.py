from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    image_list = Image.objects.filter(user=request.user)
    return render(
        request,
        'image/image_list.html',
        {'images': image_list}
    )


@login_required
def image_detail(request, id, slug):
    image = Image.objects.filter(id=id, slug=slug).first()
    return render(
        request,
        'image/image_detail.html',
        {'image': image}
    )
