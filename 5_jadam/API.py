import json
import requests

# API 키 -- kakao map 변환 이용
apikey = "0a4931e1a3e3940892882cd645969233"

# 주소 입력받아서 좌표로 변환
def addr_to_w_k(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
    headers = {"Authorization": "KakaoAK " + apikey}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address']

    return float(match_first['x']), float(match_first['y']) # 튜플 형태로 위도, 경도 반환

