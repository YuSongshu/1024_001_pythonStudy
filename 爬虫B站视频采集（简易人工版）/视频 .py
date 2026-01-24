import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'dnt': '1',
    'origin': 'https://www.bilibili.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bilibili.com/video/BV1jwSNBcETT/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=b76a56185762fcec370e4ef5e0ee9587',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Microsoft Edge";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
}

response = requests.get(
    'https://cn-sccd-fx-01-01.bilivideo.com/upgcxcode/51/68/34378416851/34378416851-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&platform=pc&trid=0000ba874818bf1b4da499ebd5df77ca8e5u&og=ali&deadline=1769273421&nbs=1&uipk=5&gen=playurlv3&os=bcache&mid=432214181&oi=1023396212&upsig=17e3411b15124cb0387db2cda03ad27d&uparams=e,platform,trid,og,deadline,nbs,uipk,gen,os,mid,oi&cdnid=3901&bvc=vod&nettype=0&bw=763124&qn_dyeid=23ea702690fe9d7f00ce42df6974dc2d&agrr=0&buvid=A4D561FA-B34D-46B8-355B-0DB000DAD73D65882infoc&build=0&dl=0&np=151404637&f=u_0_0&orderid=0,3',
    headers=headers,
)




with open("sp.mp4","wb") as f:
    f.write(response.content)
