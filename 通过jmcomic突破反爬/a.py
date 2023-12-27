from jmcomic import  *

# url = "https://18comic.vip/album/438696"
# url = "https://www.bilibili.com/"
url = "https://www.luogu.com.cn/"
jm_op = create_option("config.yml")

html = get_html(url, jm_op)
print(html)

