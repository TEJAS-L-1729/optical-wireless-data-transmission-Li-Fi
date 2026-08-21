import base64

def image_to_base64(image):
    with open(image, 'rb') as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string

image = "C:\\Users\\THEJAS\\OneDrive\\Desktop\\EL\\images.png"
base64_string = image_to_base64(image)
print(base64_string)