from django.shortcuts import render
import requests
import json
from django.http import HttpResponse




# Create your views here.
def list_p(request):
    datalist = publicData()
    
    context = {'list':datalist}
    
    return render(request,'pboard/list_p.html',context)


def view(request,galContentId):
    datalist = publicData()
    print('데이터 호출 :',datalist)
    dData = ''
    for d in datalist:
        if d['galContentId'] == galContentId:
            context = {'d':d}
            print('d :',d)
            return render(request,'pboard/view.html',context)

    return HttpResponse("해당 콘텐츠를 찾을 수 없습니다.")


# 공공데이터 가져오기 함수
def publicData():
    public_key = '%2FjAVLJGJZwHZGVorf%2Fajiyz7RdhV3oK%2Fblc9UUxnyUtQHw6smo%2B%2BPq4zUs4viIvtUAxG6Zj3YNu%2Bnt6xQ8WnZw%3D%3D'
    pageNo = 1
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={public_key}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    # 웹스크래이핑 requests
    response = requests.get(url)
    # print('공공데이터 :',response.text)  # str타입
    # 문자열 >> json타입으로 변경
    json_data = json.loads(response.text)
    datalist = json_data['response']['body']['items']['item']
    # print('json데이터 :',json_data['response']['body']['items']['item'])     # json타입
    # print('json데이터 1개 :',json_data['response']['body']['items']['item'][0])
    
    return datalist