from datetime import datetime


def add_log(request, uid, client, message):
    item = request.tl.new_item(
        hash_key=uid,
        range_key=str(datetime.now()),
        attrs={'client': client, 'message': message})
    item.put()
