# (c) @AbirHasan2005

import os
import random
from PIL import Image
from helpers.assets.emojis_map import emojis_index


def make_captcha(id):
    # Ensure the directory exists
    cache_dir = "helpers/cache/"
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    
    background.save(f"{cache_dir}{id}.png", "PNG", quality=100)
    return data, f"{cache_dir}{id}.png"
