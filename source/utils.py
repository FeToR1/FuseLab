
from PIL import Image
import os

IMG_FORMATS_CONVERT = {
    ".jpg": ".png",
    ".jpeg": ".png",
    ".png": ".jpg",
}

class PictureConverter:
    def __init__(self):
        pass

    def convert_if_needed(self, path) -> str:
        if not self.need_to_convert(path):
            return path
        
        img = Image.open(path)
        converted_img = self.converted_name(path)
        img.save(converted_img)
        return converted_img

    def is_img(self, path) -> bool:
        for i in IMG_FORMATS_CONVERT.keys():
            if path.endswith(i):
                return True
        return False

    def converted_name(self, path) -> str:
        for i in IMG_FORMATS_CONVERT.keys():
            if path.endswith(i):
                return path.replace(i, IMG_FORMATS_CONVERT[i])
        return path

    def need_to_convert(self, path) -> bool:
        return self.is_img(path) and os.path.exists(path)


    def is_converted(self, path) -> bool:
        for i in IMG_FORMATS_CONVERT.values():
            if path.endswith(i) and not os.path.exists(path):
                return True
        return False

    def get_parent_name(self, path) -> str:
        for i in IMG_FORMATS_CONVERT.keys():
            if path.replace(i, IMG_FORMATS_CONVERT[i]) != path and os.path.exists(path.replace(i, IMG_FORMATS_CONVERT[i])):
                return path.replace(i, IMG_FORMATS_CONVERT[i])
