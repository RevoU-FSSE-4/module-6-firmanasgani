
def is_integer_id(id):
    try:
        int(id)
        return False
    except ValueError:
        return True
    