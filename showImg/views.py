from django.shortcuts import render,render_to_response
from disk.models import User
from collections import defaultdict
from django.http import HttpResponse
def show(request):
    image=defaultdict(list)
    '''image['eat'].append(User.objects.filter(tag="eat")[:1])'''
    user_list = User.objects.all()
    '''for user in User
    	user_list=user'''

    # user=User()
    # user_list=user.username

    # return HttpResponse("<p>" + user_list + "</p>")
    # return HttpResponse("<p>" + ' '.join(User.objects.all()) + "</p>")
    #return image.item()'''
    return render_to_response('show.html',{'user_list':user_list,'tag':'record'})
# Create your views here.
