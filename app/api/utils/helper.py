
def updateobj(obj, data):
    for key, value in data.items():
        if value is not None:
            # print(value)
            setattr(obj, key, value)
