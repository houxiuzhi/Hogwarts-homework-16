import requests



def get_token():
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww3afe5004186b4ce6&corpsecret=Y_VXRfSURFb3L2GDeuwB-CvsbpNdAyERmZ7B-au2zjg')
    mytoken = r.json()['access_token']
    return mytoken

def test_get_member():
    userid = 'wang1'
    getmemberurl = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid={userid}'
    r = requests.get(getmemberurl)
    print(r.json())
    resjson = r.json()
    assert resjson['errcode'] == 0

def test_update_member():
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    jsondata = {
        "userid": "wang1",
        "name": "李四啊"
    }
    r = requests.post(url=update_member_url,json=jsondata)
    print(r.json())
    assert r.json()['errcode'] == 0

def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "000123",
        "name": "wang12",
        "mobile": "12100002323",
        "department": [1]
    }
    r = requests.post(url=create_member_url,json=data)
    print(r.json())
    assert r.json()['errcode'] == 0

def test_delete_member():
    userid = '000123'
    delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid={userid}'
    r = requests.get(delete_member_url)
    print(r.json())
    assert r.json()['errcode'] == 0
