import requests
import ffmpeg

def yp():
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
        'https://cn-sccd-fx-01-01.bilivideo.com/upgcxcode/51/68/34378416851/34378416851-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&nbs=1&gen=playurlv3&og=hw&platform=pc&trid=00000c8d90095dc14c9283e291f1eb8b938u&mid=432214181&deadline=1769519183&oi=1023396212&os=bcache&uipk=5&upsig=746ba97401f118d6d7ff1e624f55fc04&uparams=e,nbs,gen,og,platform,trid,mid,deadline,oi,os,uipk&cdnid=3901&bvc=vod&nettype=0&bw=100828&buvid=A4D561FA-B34D-46B8-355B-0DB000DAD73D65882infoc&np=151404637&build=0&dl=0&f=u_0_0&qn_dyeid=bf700c7050f9e82f00d15e7069789c2f&agrr=0&orderid=0,3',
        headers=headers,
    )

    with open("yp.mp3", "wb") as f:
        f.write(response.content)

def sp():
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
        'https://cn-sccd-fx-01-02.bilivideo.com/upgcxcode/51/68/34378416851/34378416851-1-100024.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&oi=1023396212&platform=pc&trid=00000c8d90095dc14c9283e291f1eb8b938u&uipk=5&gen=playurlv3&os=bcache&og=ali&mid=432214181&deadline=1769519183&nbs=1&upsig=c0412ff6cf3d6166f872ff133ebefed4&uparams=e,oi,platform,trid,uipk,gen,os,og,mid,deadline,nbs&cdnid=3902&bvc=vod&nettype=0&bw=763124&np=151404637&build=0&dl=0&f=u_0_0&qn_dyeid=bf700c7050f9e82f00d15e7069789c2f&agrr=0&buvid=A4D561FA-B34D-46B8-355B-0DB000DAD73D65882infoc&orderid=0,3',
        headers=headers,
    )

    with open("sp.mp4", "wb") as f:
        f.write(response.content)

def combined():
    ffmpeg.input("sp.mp4").output(
        ffmpeg.input("yp.mp3"),
        filename="斩断昔日旧枷锁 今日方知我是我.mp4",
        vcodec="copy"
    ).run()

if __name__ == '__main__':
    yp()
    sp()
    combined()