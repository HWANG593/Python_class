def mydict(**args):
    result = {}
    for key,value in args.items():
        result['my'+key] = value

    return result

