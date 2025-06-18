from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests

# Create your views here.
def oauth(request):
    code = request.GET.get('code')
    print('code:',code)
    content_type = ''
    client_id = ''
    redirect_uri = ''
    kakao_token_url = ''
    
    # 카카오로그인 토큰 요청
    token_data = requests.post()
    
    
    # 개인정보 받기
    kakao_profile_url = 'https://kapi.kakao.com/v2/user/me'
    auth_headers = {
        'Authorization':f'Bearer ${access_token}',
        'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
    }

    # 개인정보 요청
    user_info = requests.get(kakao_profile_url,headers=auth_headers)
    
    # json타입으로 변경
    user_info_json = user_info.json()
    
    
    
    user_info_json.get('id')    # 회원번호
    kakao_account = user_info_json.get('kakao_account')     # 카카오계정 전체정보
    kakao_profile = kakao_account.get('profile')
    kakao_nickname = kakao_profile.get('nickname')
    kakao_thumbnail_image_url = kakao_profile.get('thumbnail_image_url')
    kakao_profile_image_url = kakao_profile.get('profile_image_url')
    
    request.session.session_id = user_info_json.get('id')
    return redirect('/')
    
    return HttpResponse(f'code : {code}, token json : {token_json}<br>닉네임 : {kakao_nickname},<br> 프로필 사진 : {kakao_profile_image_url}')