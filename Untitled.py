def my_function():
    from PIL import Image
    img = Image.open('Cristo_crucificado_black.png')
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (0, 0, 0, 0):
                pixdata[x, y] = (255, 255, 255, 255)

    img.save("recent.png", "PNG")
