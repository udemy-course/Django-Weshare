from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ImageForm


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
    return render(
        request,
        'image/image_list.html'
    )
