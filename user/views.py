from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from account.models import account
from account.models import account_image
from user.forms.create_user import ProfileCreateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm(),

    })

def get_user_by_id(request,id):
    return render(request, 'user/my_account.html', {
        'user': get_object_or_404(User, pk=id)
    })

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        user = [{
            'id': x.id,
            'name': x.name,
        } for x in User.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': user})
    context = {'computers': User.objects.all().order_by('name')}
    return render(request, "user/my_account.html", context)

#@login_required
def create_user(request):
    profile = account.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileCreateForm(data=request.POST, instance = profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            created = form.save()
            acc_img = account_image(image=request.POST['image'], user = created)
            acc_img.save()
            #return redirect('user/my_account')
    else:
        form = ProfileCreateForm()
    return render(request, 'user/create_user.html', {
        'form': form,
    })


@login_required
def show_user(request):
    account_info = account.objects.filter(user=request.user).first()
    account_photo = account_image.objects.filter(user=account_info).first()

    return render(request,'user/my_account.html',{
        'account_info':account_info,
        'account_photo': account_photo.image
    })

#def review_info(request, id):
 #   if request.method == 'GET':
  #      if request.user.is_authenticated:
   #         person_info = account.objects.filter(user=request.user, pk =id).first()
    #        image = account_image.product_image_set.first().image

   # return render(request, 'user/my_account.html', {
    #    'person_info': person_info,
     #   'image': image
   # })



