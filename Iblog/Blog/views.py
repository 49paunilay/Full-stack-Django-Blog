from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages 
from Blog.forms import CommentForm
from .models import ContactUser, Post
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    
    if request.POST:
        print(request.user)
        searched_keyword = request.POST.get('search')
        posts = Post.objects.filter(content__icontains = searched_keyword)
    else:
        posts = Post.objects.all()
    totalUser = User.objects.all().count()
    print('Total User '+str(totalUser))
    return render(request,'home.html',{'posts':posts,'totalUser':totalUser})

def contact_information(request):
    if request.POST!=None:
        email = request.POST.get('contact_email')
        user_comment = request.POST.get('contact_textarea_comment')
        if( email != None and user_comment !=None):
            newuserComment = ContactUser() 
            newuserComment.name = email
            newuserComment.email = email
            newuserComment.contact_comment = user_comment

            send_mail(
            'Thanks for your comment',
            'Here is what we got \n'+ user_comment,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,)

            try:
                newuserComment.save()
                return redirect('/')
            except:
                pass
    
    return render(request,'contact.html')


def singlePostInformation(request,url):
    if str(url).isnumeric():
        requiredPost = Post.objects.get(postId = url)
        comments = requiredPost.comments.filter(active=True)
        new_comment = None
        comment_form = CommentForm()
        if request.method=='POST':
            if request.user.is_authenticated:
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                    new_comment = comment_form.save(commit=False)
                    new_comment.post = requiredPost
                    new_comment.username = request.user.username
                    if len(new_comment.body)>5:
                        new_comment.save()
                        messages.success(request, "Comment submitted for moderation ")
                    else:
                        pass
            
            else:
                messages.error(request,'Please Sign Up to comment')
        else:
            comment_form = CommentForm()

        return render(request,'postDetails.html',{'singlepost':requiredPost, 'comments':comments,'commentform':comment_form,'new_comment':new_comment})