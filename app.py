import streamlit as st
import plotly as px
import pandas as pd

from collections import Counter
from itertools import combinations

import cloudinary_service

@st.cache
def get_images_with_tags():
    return cloudinary_service.get_all_images_with_tags()

all_images = get_images_with_tags()

all_tags = []
all_tags_lists = []
for image in all_images:
    tags = image['tags']
    if not tags or "person" in tags:
        continue
    all_tags.extend(tags)
    all_tags_lists.append(tags)

tag_counter = Counter(all_tags)

print(tag_counter)
print(all_tags_lists)
