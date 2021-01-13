def myemail_info(mail):
    if '@' in mail:
        ans = tuple(mail.split('@'))
        return ans

    else:
        return None
