import uuid

def get_order_number():
    return str(int(str(uuid.uuid4().int)[:5])) 