#/bin/python3
def checkin(Email,passwd):
    import requests
    url="https://go.runba.cyou/auth/login"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69'
    }
    data={
        "email":Email,
        "passwd":passwd
    }
    resp=requests.post(url,headers=headers,data=data)
    to_set_cookie = requests.utils.dict_from_cookiejar(resp.cookies)
    if not (resp.status_code==200 and resp.json().get('ret')==1):
        print("登陆失败",resp.text)
        exit(0)
    else:
        print('用户==>',to_set_cookie.get('email'),'登陆成功')
    checkin_url="https://go.runba.cyou/user/checkin"
    resp2=requests.post(checkin_url,headers=headers,cookies=to_set_cookie)
    if resp2.status_code==200:
        if resp2.json().get("ret")==1:
            print("*"*10+"签到成功"+10*"*")
            print("签到获得流量==>",res[0])
            print("剩余流量==>",res[0])
            print("已经使用==>",res[0])
            print("已经使用==>",res[0])
        else:
            print(resp2.json().get("msg"))
checkin('xxxx@qq.com','xxxx')


