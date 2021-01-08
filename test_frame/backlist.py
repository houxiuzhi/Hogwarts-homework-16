def black_wragger(fun):
    def wragger(*args,**kwargs):
        basepage = args[0]
        try:
            return fun(*args,**kwargs)
        #如果元素没找到去捕获异常
        except Exception as e:
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

    return wragger