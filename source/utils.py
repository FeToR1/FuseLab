
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
        if not self.is_converted(path):
            return path
        Image.open(self.get_parent_name(path)).convert('RGB').save(path)

        return path

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
        return self.is_img(path) and os.path.exists(path) and not os.path.exists(self.converted_name(path))


    def is_converted(self, path) -> bool:
        for i in IMG_FORMATS_CONVERT.values():
            if path.endswith(i) and not os.path.exists(path):
                return True
        return False

    def get_parent_name(self, path) -> str:
        for i in IMG_FORMATS_CONVERT.keys():
            if path.replace(i, IMG_FORMATS_CONVERT[i]) != path and os.path.exists(path.replace(i, IMG_FORMATS_CONVERT[i])):
                return path.replace(i, IMG_FORMATS_CONVERT[i])
        return path
