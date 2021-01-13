from functools import wraps

import allure
import logging
logging.basicConfig(level=logging.INFO)

def black_wrapper(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        basepage = args[0]
        try:
            logging.info('开始找blacklist元素\nargs:'+str(args)+'kwargs:'+str(kwargs))
            return fun(*args,**kwargs)
        #如果元素没找到去捕获异常
        except Exception as e:
            with allure.step("截图"):
                basepage.driver.save_screenshot('tmp.png')
                with open('tmp.png','rb') as f:
                    data = f.read()
                allure.attach.file("tmp.png",attachment_type=allure.attachment_type.PNG)
            for black in basepage.blacklist:
                #现在black是个元祖
                print(black)
                #*解包tuple，**解包dict，finds一定要return
                eles = basepage.finds(*black)
                #finds不return就是none
                print(eles)
                #TypeError: object of type 'NoneType' has no len()就会报错
                print(type(eles))
                if len(eles) >0:
                    eles[0].click()
                    return fun(*args,**kwargs)
            raise e

    return wrapper