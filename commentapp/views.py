from django.shortcuts import render , redirect
from .models import *
from .forms import *
# Create your views here.


def index(request):
    if request.method == 'POST': #Html deki formun posr ise
        form = CommentForm(request.POST)# mrthodu post olan formu çek
        if form.is_valid(): # Formdaki alanlar doğru girildiyse
            user_comment = form.save(commit=False) #kayıt et ama yayınlama  
            user_comment.user = request.user 
            user_comment.save()
            form.save() #Formu kaydet
            return redirect('index') # Ve ilgili sayfayı tekrar çağır
        else:
            return render(request,'index.html',context)
        
    comment = Comment.objects.all() # bir modelin içindeki her value değerini sayfaya göndermek için kullanırız.
    tersComment = reversed(comment)
    
        
    form = CommentForm()
    context = {
        'yorum':tersComment,
        'form' : form,
    }
    return render(request,'index.html',context)

def sil(request):
    if request.method == 'POST':
        silId = request.POST['silValue']
        silComment = Comment.objects.filter(id = silId)
        silComment.delete()
        return redirect('index')
        
        