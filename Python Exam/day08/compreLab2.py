def mycompredict(**args):
    result = {}
    result = {'my'+key:value for key,value in args.items()}
    return result
