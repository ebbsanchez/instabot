""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
import random
import os

# login credentials
insta_username = os.getenv("IG_USER")  # <- enter username here
insta_password = os.getenv("IG_PW")  # <- enter password here

target_tags = ["facefilters", 'instagramfilters', 'vsco']
# read dont include
dont_include_list = []
with open('users.txt', 'r') as f:
    for i in f.readlines():
        dont_include_list.append(i[:-1])
assert len(dont_include_list) > 250



# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  )



with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=100,
                                    min_following=77)

    session.set_dont_include(dont_include_list)
    session.set_dont_like(["pizza", "#store"])

    # activity
    session.like_by_tags(random.sample(target_tags,1), amount=100)