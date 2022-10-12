from django.http import HttpResponseRedirect
from django.shortcuts import render
from.forms import ReviewForm
from.models import Review


# Create your views here.

def review(request):
    if request.method == 'POST':
        form =ReviewForm(request.POST)
        
        if form. is_valid():
            
            # review = Review( we don't need thess steps when we use modelform method
            #   user_name = form.cleaned_data['user_name'],
            #   review_text = form.cleaned_data['review_text'],
            #   rating = form.cleaned_data['rating'])
            form.save()
            return HttpResponseRedirect("/thank-you")
       
    else:    
        form = ReviewForm()

    return render(request,"review.html",{
       "form": form
    })

def thank_you(request):
    return render(request,"thank.html")
