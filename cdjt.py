import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from fake_useragent import UserAgent

url = r"http://172.25.249.64/eportal/index.jsp?userip=100.66.201.47&wlanacname=&nasip=171.88.130.251&wlanparameter=12-b8-d1-79-21-de&url=http://www.msftconnecttest.com/redirect&userlocation=ethtrunk/3:462.3201"  # 测试网址

async def run():
    driver = await launch({
        # 谷歌浏览器的安装路径
        'executablePath': r'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
        # Pyppeteer 默认使用的是无头浏览器
        'headless': False,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1480,760', '--disable-infobars'],
        'dumpio': True,
    })

    # 用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await driver.newPage()
    # 简称换头
    await page.setUserAgent(
        UserAgent().random)

    await page.setViewport({'width': 1480, 'height': 760})
    # 反爬虫跳入网页
    await stealth(page)
    await page.goto(url)  # 问卷星网址

    # 模拟输入 账号密码  {'delay': rand_int()} 为输入时间
    await page.type('#username_tip', "账号")
    await page.type('#pwd_tip', "12345678") #密码默认为12345678

    await page.click("#loginLink_div")



asyncio.get_event_loop().run_until_complete(run())
