import streamlit as st
import plotly as px
import pandas as pd

from collections import Counter
from itertools import combinations

import cloudinary_service

@st.cache_data
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

#print(tag_counter)
#print(all_tags_lists)
sorted_tags = [item for item in sorted(tag_counter.items(), key=lambda x: -x[1])]
sorted_tag_strings = [f"{item[0]} ({item[1]})" for item in sorted_tags]

combs = []
for tags_per_image in all_tags_lists:
    for comb in combinations(tags_per_image, 2):
        combs.append(comb)

most_common_combs = Counter(combs).most_common(20)

def show_images(images):
    columns = st.columns(3)
    for idx, img in enumerate(images):
        col = columns[idx % 3]
        url = img['url']
        if url.endswith(".heic"):
            url = url[:-5] + ".jpg"
        with col:
            st.image(url)
            st.markdown(f"[Links]({url})")

def image_page():
    show_images(all_images)

def stats_page():
    pass

if __name__ == "__main__":
    options = ("Image Gallery", "Image Stats")
    selection = st.selectbox("Menu", options)

    if selection == "Image Gallery":
        st.title("Image Gallery")
        image_page()
    else:
        st.title("Image Stats")
        stats_page()