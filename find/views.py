from django.shortcuts import render
from .models import Para, File , Word, Unique

from django.contrib import messages
import re


def home(request):  
    return render(request,'msg.html')

def add(request): 
    if request.method == 'POST':
        para = request.POST["para"]
        para = para.lower()   #change to lowercase
        para = re.sub(r'[^\w\s]','', para)  #remove all punctuation
        paras = para.split("\r\n\r\n\r\n") #split a paragraph into new paragraph if there is two newlines
        for para in paras:  
            words = para.split() 
            print(words)
            paragraph = Para.objects.create(para=para)
            for word in words:
                obj, created = Unique.objects.get_or_create(word=word)     #get_or_created if word is already in db it doesnot create a new word the 'created' becomes false..if the word not inside a db it create a new one in Unique model
                obj.location.add(paragraph)            
        return render(request, 'msg.html',)
    else:
        return render(request, 'msg.html',)



def find(request):
    if request.method == 'POST':
        input_word = request.POST['search']
        
        if input_word:
            texts = Para.objects.filter(para__contains = input_word).values()
            s = request.POST['search'] 
            for text in texts:
                print(text)
            if texts:
                return render(request,'list.html', {'result':texts})
                
            else:
                messages.info(request,'No Results found')
                return render(request,'list.html') 
               
    else:
        return render(request,'list.html')


def file(request):
    if request.method == 'POST':
       file = request.POST["file"]
       c = File.objects.create(file=file)
       c.save()
       return render(request,'product.html',)
     
    return render(request,'product.html')


def inverted(request):
     if request.method == 'POST':
        word = request.POST['search'] #get the word from user
        word = word.lower() #convert into Lowercase
        unique = Unique.objects.filter(word=word).first()
        
        if unique:
            return render(request, 'user.html', {'result':unique.location.all().values()})
        else:
            messages.info(request, 'No Results found')
            return render(request, 'user.html')
     else:
        return render(request,'user.html')
    
# unique = Unique.objects.filter(unique=word).first().location.all().values('id', 'para')
# above first match the given word in unique db.then select the first word and match their locations in location field and return the all values