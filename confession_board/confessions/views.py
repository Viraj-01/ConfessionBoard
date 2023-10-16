from django.shortcuts import render

# Create your views here.
# confessions/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Confession, Comment

def confession_list(request):
    confessions = Confession.objects.all().order_by('-likes')  # Order by likes in descending order
    comments = Comment.objects.all()

    return render(request, 'home.html', {'confessions': confessions, 'comments': comments})
def submit_confession(request):
    if request.method == 'POST':
        confession_text = request.POST.get('confessionText', '')
        if confession_text:
            new_confession = Confession.objects.create(text=confession_text)
            Comment.objects.create(confession=new_confession, text='Initial comment')  # You can set an initial comment if needed
    return redirect('confession_list')

def add_comment(request, confession_id):
    if request.method == 'POST':
        confession = get_object_or_404(Confession, pk=confession_id)
        comment_text = request.POST.get('commentText', '')
        if comment_text:
            Comment.objects.create(confession=confession, text=comment_text)
    return redirect('confession_list')

def like_dislike_confession(request, confession_id, action):
    confession = get_object_or_404(Confession, pk=confession_id)

    # Check if the user has already liked or disliked this confession
    if not request.session.get(f'confession_{confession_id}_liked', False):
        if action == 'like':
            confession.likes += 1
            request.session[f'confession_{confession_id}_liked'] = True
        elif action == 'dislike':
            confession.dislikes += 1

        confession.save()

    return redirect('confession_list')

def like_dislike_comment(request, comment_id, action):
    comment = get_object_or_404(Comment, pk=comment_id)

    # Check if the user has already liked or disliked this comment
    if not request.session.get(f'comment_{comment_id}_liked', False):
        if action == 'like':
            comment.likes += 1
            request.session[f'comment_{comment_id}_liked'] = True
        elif action == 'dislike':
            comment.dislikes += 1

        comment.save()

    return redirect('confession_list')