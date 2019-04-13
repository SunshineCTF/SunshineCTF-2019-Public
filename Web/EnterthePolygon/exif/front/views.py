from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import exifread
import uuid
from .models import images
from exif.settings import MEDIA_ROOT, APPROVED_SIGNER

import jwt
import json
from requests import get as req_get
from base64 import b64encode, b64decode

from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

# checks to see if it is the bot - returns false if bot
def is_victim(user):
    if user.id == 1:
        return True
    return False

def notvictim(user):
    return not(is_victim(user))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # need to get this to auth and redirect
            #user = authenticate(username=username, password=raw_password)
            #login(user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    return redirect("/")

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.filename = request.FILES.get("ifile")._get_name()
            upload.save()
            return redirect('/exif/{0}'.format(upload.get_upldName()))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def imageView(request, **kwargs):
    form = None
    tags = "Looks like you made a mistake"
    filename = ""
    filename = kwargs.get('filename')
    try:
    # if user_id was not provided get logged in user
        user = request.user.id
        obj = images.objects.get(user=user, ifile__endswith=filename)
        with open(obj.ifile.path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        if not tags:
            tags = {"":"There is no exif data"}
    except Exception as e:
        print(e)
    # send url to document_view function with filename
    filepath = 'media/'+filename
    return render(request, 'image.html', {'tags' : tags, 'filepath':filepath, 'filenm':obj.filename})

# media/filename endpoint. Redirects to nginx served files.
@login_required
def document_view(request, filename):
    user = request.user
    document = images.objects.get(user=user, ifile__endswith=filename)
    response = HttpResponse()
    response["Content-Disposition"] = "inline"
    response["Content-Type"] = "image/jpeg"
    response['X-Accel-Redirect'] = "/protected/user-{0}/{1}".format(str(user.id),document.get_upldName())
    return response


@user_passes_test(is_victim)
def vic_imageView(request, **kwargs):
    form = None
    userid= kwargs.get('userid')
    filename = kwargs.get('filename')
    try:
    # if user_id was not provided get logged in user
        obj = images.objects.get(user=userid, ifile__endswith=filename)
        with open(obj.ifile.path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        if not tags:
            tags = {"":"There is no exif data"}
    except Exception as e:
        print(e)
    # send url to document_view function with filename
    filepath = 'bot/media/{0}/{1}'.format(userid, filename)
    return render(request, 'image.html', {'tags' : tags, 'filepath':filepath, 'filenm':obj.filename})

@user_passes_test(is_victim)
def vic_document_view(request, **kwargs):
    userid = kwargs.get('userid')
    filename = kwargs.get('filename')
    document = images.objects.get(user=userid, ifile__endswith=filename)
    response = HttpResponse()
    response["Content-Disposition"] = "inline"
    response["Content-Type"] = "image/jpeg"
    response['X-Accel-Redirect'] = "/protected/user-{0}/{1}".format(str(userid),document.get_upldName())
    return response



def validateToken(request, template, flag):
    token = request.COOKIES.get('jwtsess')

    if token:
        # check if token is valid (if not state invalid token)
        try:
            split = token.split('.')[1]
            split = b64decode(split + '=' * (4 - len(split) % 4))
            unverfied_values = json.loads(split) # jwt is headers.keys.signature - have to fix padding
            sign_host = unverfied_values.get('sig')
            decoded = {}
            if any(approved_host in sign_host for approved_host in APPROVED_SIGNER): # this is easily bypassed to a remote host by including the string anywhere in the url.
                secret = b64encode(req_get(sign_host, timeout=1).content)
                decoded = jwt.decode(token, secret)
        except Exception as e:
            print(e)
            return render(request, template, {'output': e})

        # cant be bothered to implement this legit so hardcoded cases
        try:
            if decoded.get('user') == 'therock':
                if decoded.get('role') == 'admin':
                    return render(request, template, {'output': flag})
        except:
            return render(request, template, {'output': "Not valid user/role"})

    return render(request, template, {'output': "Not Logged In"})


def admin(request, **kwargs):
    # check if token could exist (if not say not authed)
    return validateToken(request, 'adminFlag.html', 'SUN{Can_Y0U_smell_JWT?}')

@login_required
def profile(request, **kwargs):
    uploads = images.objects.filter(user=request.user)

    return render(request, 'profile.html', {'uploads': uploads})
