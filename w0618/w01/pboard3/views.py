from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json

# Create your views here.
def list_p3(request):
    service_key = '6c5ddcf429f5f5c5f3cd05571911c14e'
    targetDt = '20250617'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={service_key}&targetDt={targetDt}'
    
    
    response = requests.get(url) 
    json_data = json.loads(response.text)
    
    # print(json_data)
    
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    
    print(mlist)
    
    context = {'list':mlist}
    return render(request, 'pboard3/list_p3.html',context)



def view(request,movieCd):
    service_key = '6c5ddcf429f5f5c5f3cd05571911c14e'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={service_key}&targetDt=20250617'
    
    response = requests.get(url) 
    json_data = json.loads(response.text)
    
    # print(json_data)
    
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    
    for m in mlist:
        if m['movieCd'] == movieCd:
            context = {'movie':m}        
            return render(request, 'pboard3/view.html',context)
        
    return HttpResponse("잘못된 접근입니다.")


dlist = []

# ajax통신 - 리턴타입: json
def searchAjax(request):
    targetDt = request.POST.get('searchInput','20250617')
    print('targetDt :',targetDt)    
    service_key = '6c5ddcf429f5f5c5f3cd05571911c14e'

    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={service_key}&targetDt={targetDt}'
    
    
    response = requests.get(url) 
    json_data = json.loads(response.text)
    
    # print(json_data)
    
    dlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    
    print(dlist)
    
    
    
    context = {'list':dlist}
    
    return JsonResponse(context)