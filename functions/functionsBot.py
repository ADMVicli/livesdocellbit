from base64 import b64encode

def compareImages():
        with open('./404.jpg', 'rb') as notFound:
            imageNotFound = b64encode(notFound.read())
        with open('gameImg.jpg', 'rb') as gameImage:
            img = b64encode(gameImage.read())
        if imageNotFound == img:
            return True
        else:
            return False