from django.shortcuts import render
from django.http import HttpResponse
from .models import game
from .models import result
from .forms import FindForm
from PIL import Image, ImageDraw
from django.db.models import Q

def index(request):
    params = {
            'title': 'SofttennisDB',
            'msg':'ようこそ！',
            'goto':'index',
            'goto1':'add',
            'goto3':'video',
            'goto2':'find',
        }
    return render(request, 'score/index.html', params)


def add(request):
    params = {
            'title':'ソフトテニスデータベース',
            'msg':'戻るを押したらタイトルに戻れるよ！',
            'goto':'index',
        }
    return render(request, 'score/index_add.html', params)


def video(request):
    params = {
            'title':'ソフトテニスデータベース',
            'msg':'戻るを押したらタイトルに戻れるよ！',
            'goto':'index',
        }
    return render(request, 'score/index_video.html', params)




def analys(request, num):
    data =game.objects.filter(id=num).values_list('gamename','score').get()
    data1 =list(data)

    rdata4 = result.objects.filter(gameid=num).values_list('result', flat=True)
    re = list(rdata4)
    IN = re.count('IN')
    N = re.count('N')
    RS = re.count('RS')
    LS = re.count('LS')
    T = re.count('T')
    B = re.count('B')
    
    
    
    rdata2 = result.objects.filter(gameid=num).values_list('course', flat=True)
    
    rdata3 = result.objects.filter(gameid=num).values_list('before', flat=True)
    
    rdata5 = result.objects.filter(gameid=num).values_list('playername', flat=True)
    
    rdata6 = result.objects.filter(gameid=num).values_list('position', flat=True)
    
    
    pos = list(rdata6)
    course = list(rdata2)
    before = list(rdata3)
    skill = list(rdata5)
    
    im = Image.new('RGB', (650, 900), (248, 249, 250))
    draw = ImageDraw.Draw(im)

    draw.rectangle((40, 40, 600, 840),fill=(255,255,255),outline=(0,0,0))
    draw.line((20, 440, 620, 440), fill=(255,0,0))
    draw.line((150, 40, 150, 840),fill=(0,0,0))
    draw.line((490, 40, 490, 840),fill=(0,0,0))
    draw.line((150, 250, 490, 250),fill=(0,0,0))
    draw.line((150, 630, 490, 630),fill=(0,0,0))
    draw.line((320, 250, 320, 630),fill=(0,0,0))

    im.save('score/static/score/tenniscourt.jpg', quality=95)

    params = {
        'title': 'Hello',
        'id':num,
        'data1':data1,
        'course':course,
        'before':before,
        're':re,
        'skill':skill,
        'pos':pos,
        'IN':IN,
        'N':N,
        'RS':RS,
        'LS':LS,
        'T':T,
        'B':B,
    }
    
    return render(request, 'score/analys.html', params)


def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = game.objects.filter(Q(keio1__contains=str)|Q(keio2__contains=str))
    else:
        msg = 'search words...'
        form = FindForm()
        data =game.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,
    }
    return render(request, 'score/find.html', params)

