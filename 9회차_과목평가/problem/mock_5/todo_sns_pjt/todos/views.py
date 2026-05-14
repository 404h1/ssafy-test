from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Comment
from .forms import TodoForm, CommentForm


def index(request):
    # Bug 01: 정렬 없음 → 최신순으로 표시되지 않음
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {'form': form}
    return render(request, 'todos/create.html', context)


def detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    comment_form = CommentForm()
    context = {
        'todo': todo,
        'comment_form': comment_form,
    }
    return render(request, 'todos/detail.html', context)


@login_required
def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user != todo.user:
        return redirect('todos:detail', pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', pk=pk)
    else:
        # Bug 03: instance=todo 누락 → 수정 폼에 기존 데이터 미표시
        form = TodoForm()
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'todos/update.html', context)


@login_required
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user == todo.user:
        todo.delete()
    return redirect('todos:index')


# Bug 02: @login_required 누락 → 비로그인 사용자 접근 가능
def comment_create(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.todo = todo
            # Bug 04: comment.user = request.user 누락 → IntegrityError
            comment.save()
            return redirect('todos:detail', pk=pk)
    return redirect('todos:detail', pk=pk)


@login_required
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('todos:detail', pk=pk)


@login_required
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user == todo.user:
        todo.completed = not todo.completed
        todo.save()
    return redirect('todos:index')
