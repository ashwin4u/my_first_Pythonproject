
#return can Return any type of data.

def return_manytypes_data(data):
    """Example for demonstrating that "return" can return any Type of Data"""
    if isinstance(data, int):
        return data + 5
    elif isinstance(data, float):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, bool):
        return not data
    elif isinstance(data, (list, tuple, set)):
        return None
    else:
        return None



res=return_manytypes_data("Ashwin")
print(res)
print("The Result is:",res)
print("Good Evening Everyone.Happy Learning")
print("Hello")


