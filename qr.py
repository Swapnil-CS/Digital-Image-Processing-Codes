import qrcode


my_data = """
    you are a fool
"""

img = qrcode.make(my_data)
img.save("my_data.png")
