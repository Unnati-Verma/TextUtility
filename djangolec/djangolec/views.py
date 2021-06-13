from django.http import HttpResponse
from django.shortcuts import render


def files(request):
    return render(request, 'index..html')


def analyze(request):
    text = request.POST.get('textana', 'def')
    removepunc = request.POST.get('removepunc', 'off')
    caps = request.POST.get('caps', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    if removepunc == 'on':
        punctuations = '''.,;:'"!@#$%^&*){}[]_-?/><|'''
        analyzed = ""
        for i in text:
            if i not in punctuations:
                analyzed = analyzed + i
        param = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', param)
    if caps == 'on':
        analyzed = ""
        for i in text:
            analyzed = analyzed + i.upper()
        param = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', param)
    if newlinerem == 'on':
        analyzed = ""
        for i in text:
            if i != "\n" and i != "\r":
                analyzed = analyzed + i
        param = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        text = analyzed

    return render(request, 'analyze.html', param)