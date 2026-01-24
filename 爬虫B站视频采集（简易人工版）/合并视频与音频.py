import ffmpeg

ffmpeg.input("sp.mp4").output(
    ffmpeg.input("yp.mp3"),
    filename="斩断昔日旧枷锁 今日方知我是我.mp4",
    vcodec="copy"
).run()