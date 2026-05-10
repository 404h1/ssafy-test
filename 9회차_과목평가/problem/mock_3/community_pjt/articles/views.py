from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.order_by('created_at')  # BUG 09: 오름차순
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all()
    context = {'article': article, 'comment_form': comment_form, 'comments': comments}
    return render(request, 'articles/detail.html', context)


@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.user:
        return redirect('articles:detail', article.pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST)  # BUG 01: instance=article 없음
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)


@login_required
def delete(request, pk):  # BUG 03: @require_POST 없음
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        # BUG 02: comment.user = request.user 없음
        comment.save()
    return redirect('articles:detail', article_pk)


@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
