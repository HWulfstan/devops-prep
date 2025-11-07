from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from django.core.files.storage import FileSystemStorage

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-id')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})

def add_tweet(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')
        if text:
            tweet = Tweet(text=text)
            if image:
                tweet.image = image
            tweet.save()
        return redirect('tweet_list')
    return render(request, 'tweets/add_tweet.html')

def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        tweet.text = request.POST.get('text')
        if 'image' in request.FILES:
            tweet.image = request.FILES['image']
        tweet.save()
        return redirect('tweet_list')
    return render(request, 'tweets/edit_tweet.html', {'tweet': tweet})

def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    tweet.delete()
    return redirect('tweet_list')
