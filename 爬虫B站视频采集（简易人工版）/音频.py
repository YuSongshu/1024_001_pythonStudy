import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'dnt': '1',
    'origin': 'https://www.bilibili.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bilibili.com/video/BV1jwSNBcETT/?spm_id_from=333.1391.0.0&vd_source=b76a56185762fcec370e4ef5e0ee9587',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Microsoft Edge";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
}

response = requests.get(
    'https://cn-sccd-fx-01-03.bilivideo.com/upgcxcode/51/68/34378416851/34378416851-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&platform=pc&mid=432214181&deadline=1769177788&uipk=5&trid=0000904289d329964357943063a62b215dbu&oi=2946081142&os=bcache&og=hw&nbs=1&gen=playurlv3&upsig=2b4d52d17219a3a08a42343196ca5464&uparams=e,platform,mid,deadline,uipk,trid,oi,os,og,nbs,gen&cdnid=3903&bvc=vod&nettype=0&bw=100828&qn_dyeid=9dcb735380cbce1800544e176973669c&agrr=0&buvid=A4D561FA-B34D-46B8-355B-0DB000DAD73D65882infoc&build=0&dl=0&f=u_0_0&np=151404637&orderid=0,3',
    headers=headers,
)


with open("yp.mp3","wb") as f:
    f.write(response.content)
