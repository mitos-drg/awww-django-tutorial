from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Comment
from .forms import CommentForm


def index(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('comments:index'))
    else:
        form = CommentForm()
    comment_list = Comment.objects.filter(date_published__lte=timezone.now()).order_by("-date_published")
    context = {
        "comment_list": comment_list,
        "form": form
        }
    return render(request, "comments/index.html", context)


def edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('comments:index'))
    else:
        form = CommentForm(instance=comment)
    context = {
        "comment": comment,
        "form": form
        }
    return render(request, "comments/edit.html", context)
