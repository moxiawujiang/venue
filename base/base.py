__author__ = '芜疆'
#encoding=utf-8
from selenium import webdriver
import sys
sys.path.append("..\\util")
from get_by_local import  *
from selenium.webdriver.common.action_chains import ActionChains
import time
class ActionMethod:
    #打开浏览器
    def __init__(self):
        self.driver=None

    def open_browser(self,*args):
        if args[0]=="chrome":
            self.driver=webdriver.Chrome()
        else:
            self.driver=webdriver.Firefox()

        self.driver.implicitly_wait(5)

    def get_url(self,*args):
        url=args[0]
        self.driver.get(url)


    #定位元素的封装
    def get_element(self,*args):
        id=args[0]
        get_by_element=GetByLocal(self.driver)
        element=get_by_element.get_by_local(id)
        return element

    #对元素进行输入
    def element_send_keys(self,*args):
        id=args[0]
        value=args[1]
        element=self.get_element(id)
        element.send_keys(value)

    #点击元素
    def click_element(self,*args):
        id=args[0]
        element=self.get_element(id)
        element.click()

    #睡眠时间
    def sleep_time(self,*args):
        time.sleep(3)

    #退出浏览器
    def close_browser(self,*args):
        self.driver.quit()

    #检查元素状态
    def check_status(self,*args):
        id=args[0]
        element=self.get_element(id)
        element.is_displayed()

    #鼠标悬浮
    def move_to_element(self,*args):
        id=args[0]
        element=self.get_element(id)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(3)

    #切换iframe
    def iframe_switch(self,*args):
        id=args[0]
        self.driver.switch_to.frame(id)

    #获取元素的值
    def get_element_value(self,*args):
        id=args[0]
        element=self.get_element(id)
        return element.text

    #验证信息
    def assert_local(self,*args):
        by=args[0].split('&')[0]
        id=args[0].split("&")[1]
        value=self.get_element_value(id)
        value1=args[0].split("&")[2]
        if by=='equl':
            assert value==value1
        elif by=='notequl':
            assert value!=value1












