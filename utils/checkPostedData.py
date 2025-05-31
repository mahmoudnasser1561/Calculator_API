
""" validate request parameters """
def ValidatePostedData(postedData):
    if "x" not in postedData or "y" not in postedData:
        return 301 #Missing parameter
    try:
        int(postedData["x"])
        int(postedData["y"])
    except ValueError:
        return 302  # Non-integer input
    return 200