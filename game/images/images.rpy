# 이카루스
# Image by <a href="https://pixabay.com/users/gdj-1086657/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=6520669">Gordon Johnson</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=6520669">Pixabay</a>

# 잉크가 퍼지는 동영상
image inkExpandIdle = Movie(play="images/transitions/expand400_sephia.webm", mask="images/transitions/expand400a.webm", loop=False, keep_last_frame=True)
image inkExpandHover = Movie(play="images/transitions/expand400_border.webm", mask="images/transitions/expand400a.webm", loop=False, keep_last_frame=True)

image firstEvent = "images/events/1.png"
image secondEvent = "images/events/2.png"
image thirdEvent = "images/events/3.png"

image gardenScatter:
    "images/bgs/garden.png"
    Solid("#000") with ImageDissolve("gui/transitions/whitenoise.png", 7.5)