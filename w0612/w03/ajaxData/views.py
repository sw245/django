from django.shortcuts import render
from django.http import JsonResponse
from board.models import Board

# Create your views here.
def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    # json데이터 변환: serializers, list()
    l_qs = list(Board.objects.filter(bno=qs.bno))
    context = {'result':'success'}
    return JsonResponse(context)