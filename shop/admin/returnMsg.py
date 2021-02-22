def Success(data=None, total=None, msg='成功'):
    data = {"code": 0,
            "msg": msg,
            'count': total,
            'data': data
            }
    return data


def Error(msg='接口访问失败'):
    content = {
        "code": -1
        , "msg": msg
    }
    return content


def change(msg):
    if msg is None:
        msg = ''
    return msg
