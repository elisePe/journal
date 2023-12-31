# ~/projects/django-web-app/merchex/listings/views.py
from entree.models import entrees,users
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from entree.forms import writeForm,signForm,logForm


def home(request):

    return render(request, 'entree/home.html')

def read(request, idu,nbr):
    en = entrees.objects.get(Q(nbr=nbr) & Q(us_id=idu))
    av = entrees.objects.filter(Q(nbr=nbr-1) & Q(us_id=idu)).exists()
    ap = entrees.objects.filter(Q(nbr=nbr+1) & Q(us_id=idu)).exists()
    idp=int(nbr+1)
    idm=int(nbr-1)

    return render(request, 'entree/read.html',{'en':en,'av':av,'ap':ap,'idp':idp,'idm':idm,'idu':idu,'nbr':int(nbr)})







def write(request,idu):
    if request.method == 'POST':
        form = writeForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            deja=entrees.objects.filter(us_id=idu).count()+1
            write = entrees.objects.create(texte=form.cleaned_data['texte'],date=form.cleaned_data['date'],us_id=idu,nbr=deja)
            write.save()

            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('read',idu,deja)

    else:
        form = writeForm()

    return render(request,
            'entree/write.html',
            {'form': form, 'idu':idu})






def sign(request):
    if request.method == 'POST':
        form = signForm(request.POST)
        deja = users.objects.count() + 1
        test=0
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            sign = users.objects.create(name=form.cleaned_data['name'], passw=form.cleaned_data['passw'], us_id=deja)
            sign.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('write', idu=deja)

    else:
        form = signForm()

    return render(request,
            'entree/sign.html',
            {'form': form})



def log(request):
    if request.method == 'POST':
        form = logForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            all=users.objects.all()
            name = form.cleaned_data['name']
            iddd=1
            users_name = users.objects.filter(name=name)
            if users_name.exists() :
                userobj = users.objects.get(name=name)
                if userobj.passw == form.cleaned_data['passw']:
                    return redirect('read', userobj.us_id, entrees.objects.filter(us_id=userobj.us_id).count())


    else:
        form = logForm()

    return render(request,
            'entree/log.html',
            {'form': form})