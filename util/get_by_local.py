__author__ = '芜疆'
#encoding=utf-8


class GetByLocal:
    def __init__(self,driver):
        self.driver=driver
    def get_by_local(self,key):
        by=key.split('=')[0]
        by_value=key.split("=")[1]
        if by=='id':
            return self.driver.find_element_by_id(by_value)
        elif by=='name':
            return self.driver.find_element_by_name(by_value)
        elif by=="classname":
            return  self.driver.find_element_by_class_name(by_value)
        elif by=="xpath":
            return self.driver.find_element_by_xpath(by_value)
        elif by=="css":
            return self.driver.find_element_by_css_selector(by_value)
        elif by=="linkname":
            return self.driver.find_element_by_link_name(by_value)
        elif by=="linktext":
            return self.driver.find_element_by_link_text(by_value)
        else:
            raise Exception("没有这种定位方式")

