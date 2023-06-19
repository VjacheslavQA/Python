from page_objects import PageObject, PageElement

class FormPage(PageObject):
    customer_name = PageElement(name='custname')
    tel = PageElement(name='custtel')
    email = PageElement(name='custemail')
    medium_size = PageElement(xpath="//input[@type='radio' and @value='medium']")
    bacon_topping = PageElement(xpath="//input[@type='checkbox' and @value='bacon']")
    cheese_topping = PageElement(xpath="//input[@type='checkbox' and @value='cheese']")
    mushroom_topping = PageElement(xpath="//input[@type='checkbox' and @value='mushroom']")
    delivery = PageElement(xpath="//input[@name='delivery']")
    comments = PageElement(name='comments')
    submit = PageElement(xpath='//button')