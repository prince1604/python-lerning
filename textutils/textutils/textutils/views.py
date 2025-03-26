# I HAVE CERATED THIS FILE - PRINCE
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params =  {'name':'eminent', 'age':20 , 'city':'Rajkot'}
    return render(request, 'index.html')
    # return HttpResponse ("Home")


def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremove = request.GET.get('newlineremove','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')

# def removepunc(request):
    if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char

            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}

            return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


#def capitlizefirst(request):
#    return HttpResponse("capfirst")

#def newlineremove(request):
#    return HttpResponse("new line remove")

#def spaceremove(request):
#    return HttpResponse("space remove <a href='/'>back</a>")

#def charcount(request):
#    return HttpResponse("char count")