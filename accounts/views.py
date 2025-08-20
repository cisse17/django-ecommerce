from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()

# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():     
            user = User.objects.create_user(
                form.cleaned_data['username'], 
                form.cleaned_data['password'])
            login(request, user)
        return redirect("boutique")
            
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def login_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"))
            if user:
                login(request, user)
                return redirect("boutique")
    else:
        form = SignUpForm()

    return render(request, "accounts/login.html", {'form': form})


def logout_user(request):
    logout(request)
    return redirect('boutique')

"""
def signup(request):
    error_message = None
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect("index")
            except IntegrityError:
                # Gestion spécifique de l'erreur d'intégrité (username déjà existant)
                error_message = "Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre."
                # Conserver les données du formulaire sauf le username
                form.data = form.data.copy()
                form.data['username'] = ''  # Réinitialiser le champ username
        else:
            # Le formulaire n'est pas valide, on va afficher les erreurs
            pass
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {
        'form': form, 
        'error_message': error_message
    })
"""