# coding = utf-8
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#使用headless无界面浏览模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com')
e = driver.find_element_by_xpath("/html/body/div[@id='wrapper']/div[@id='head']/div[@class='head_wrapper']/div[@id='u1']/a[@class='mnav'][1]")
print(e.text)  # 把页面title 打印出来
driver.quit()