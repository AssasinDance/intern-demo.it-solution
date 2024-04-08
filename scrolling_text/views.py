from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import io

# Create your views here.
from scrolling_text.runtext import scrolling_text

def index(request):
    return HttpResponse("<form action='http://127.0.0.1:8000/scrolling_text'><input type='search' name='text'><input type='submit' value='Вывести на экран'></form>")
  
def user(request):
    text = request.GET.get("text")
    scrolling_text(text)
    return FileResponse(open('scrolling_text.webm','rb'))

