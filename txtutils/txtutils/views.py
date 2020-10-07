from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'txt.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    checkbox1=request.POST.get('removepunc','off')
    checkbox2=request.POST.get('upper','off')
    checkbox3=request.POST.get('removespace','off')
    checkbox4=request.POST.get('newlinechar','off')
    checkbox5=request.POST.get('charcount','off')
    print(djtext,checkbox1,checkbox2)
    if (checkbox1=="off" and checkbox2=="off" and checkbox3=="off" and checkbox4=="off" and checkbox5=="off") or djtext=="": 
        return HttpResponse("<h1 style=font-size:40px;text-align:center;>You need to Type a text or Check any Customization Checkbox</h1><br>"
        "<br><br><br><a href='http://127.0.0.1:8000/'>Go to Home</a>")
    if djtext!="" and checkbox1=="on":
        hello2=""
        punclist='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in djtext:
            if i not in punclist:
                hello2+=i
        djtext=hello2
    if djtext!="" and checkbox2=="on":
        hello2=""
        for i in djtext:
            hello2+=i.upper()
        djtext=hello2
    if djtext!="" and checkbox3=="on":
        hello2=""
        for index,i in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                hello2+=i
        djtext=hello2
    if djtext!="" and checkbox4=="on":
        hello2=""
        for i in djtext:
            if i !="\n" and i!="\r":
                hello2+=i
        djtext=hello2
    if djtext!="" and checkbox5=="on":
        hello2=""
        for i in djtext:
            if i!="\n" and i!=" " and i!="\r" :
                hello2+=i
        hello=len(hello2)
        param={"purpose":"Your Customized Text","text2":[hello,hello2]}
        return render(request,'anal.html',param)
    param={"purpose":"Your Customized Text","text2":hello2}
    return render(request,'anal.html',param)