
from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Category
from .forms import GameForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    categories = Category.objects.all()
    selected = request.GET.get('category','all')
    q = request.GET.get('q','')
    games = Game.objects.all()
    if selected and selected != 'all':
        games = games.filter(category__slug=selected)
    if q:
        games = games.filter(Q(title__icontains=q) | Q(description__icontains=q))
    latest = games.order_by('-updated_at')[:12]
    return render(request, 'home.html', {'latest': latest, 'categories': categories, 'selected': selected, 'q': q})

def games_list(request):
    categories = Category.objects.all()
    selected = request.GET.get('category','all')
    q = request.GET.get('q','')
    games = Game.objects.all()
    if selected and selected != 'all':
        games = games.filter(category__slug=selected)
    if q:
        games = games.filter(Q(title__icontains=q) | Q(description__icontains=q))
    return render(request, 'games_list.html', {'games': games, 'categories': categories, 'selected': selected, 'q': q})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, 'game_detail.html', {'game': game})

@login_required
def upload_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('games:list')
    else:
        form = GameForm()
    return render(request, 'upload.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

@login_required
def dashboard(request):
    games = Game.objects.all()
    return render(request, 'dashboard.html', {'games': games})
