from instapy import InstaPy
from instapy import smart_run
import os
# login credentials

insta_username = os.getenv("IG_USER")  # <- enter username here
insta_password = os.getenv("IG_PW")  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

# read dont include
dont_include_list = []
with open('users.txt', 'r') as f:
    for i in f.readlines():
        dont_include_list.append(i[:-1])
assert len(dont_include_list) > 250

# setting target
target_list = ['smarfilter.tw', 'work.as.life', 'nonsdesign.pw']

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(dont_include_list)
    session.set_dont_like(["pizza", "#store"])

    # activities

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)...
    """
    session.follow_user_followers(target_list, amount=100,randomize=False, interact=False)

    """ First step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Second step of Massive Follow...
    """
    session.follow_user_followers(target_list, amount=800,
                                  randomize=False, interact=False)

    """ Second step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Clean all followed user - Unfollow all users followed by InstaPy...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=601)

    """ Joining Engagement Pods...
    """
    photo_comments = ['Nice work! @{}',
                      'Awesome! @{}',
                      'Cool :thumbsup:',
                      'Just incredible :open_mouth:',
                      'What camera did you use @{}?',
                      'Love your posts @{}',
                      'Looks awesome @{}',
                      'Nice @{}',
                      ':raised_hands: Yes!',
                      'I can feel your passion @{} :muscle:']

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(photo_comments, media='Photo')
    session.join_pods(topic='food', engagement_mode='no_comments')
