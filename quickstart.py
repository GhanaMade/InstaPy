from instapy import InstaPy

insta_username = ''
insta_password = ''

# set headless_browser=True if you want to run InstaPy on a server
try:
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False,
                      multi_logs=True)
    session.login()

    # settings
    session.set_upper_follower_count(limit=2700)
    session.set_lower_follower_count(limit = 600)

    # actions
    session.like_by_tags(['melanin', 'africanfood', 'accra', 'ghanawedding', 'thisisafrica', 'africanhistory', 'afrika', 'proudghanian', 'africamen', 'africanculture', '21ninety', 'ghanaat60', 'ghanagirls', 'africandance', 'westafrica', 'afrobeats', 'iamghana', 'okayafrica', 'checkoutafrica'], amount=8)

    # For 50% of new follows, like their recent 5 photos
    session.set_user_interact(amount=5, randomize=False, percentage=50, media='Photo')

    # Following
    # Follow accounts from these users by random
    session.follow_user_followers(['ghanaposts', 'theonlywayisghana', 'ebabykobby', 'mrcocoyam', 'kofisiriboe', 'blavity', 'urge2pose', 'sarkodie', 'nakufoaddo', 'stonebwoyb'], amount=20, randomize=True, sleep_delay=600, interact=True)

    #Unfollowing
    #
    session.set_dont_unfollow_active_users(enabled=False, posts=200)
    session.unfollow_users(amount=10, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=600)

    # Won't unfollow the core list:
    session.set_dont_include(['freddydvo', 'djneizer', 'lynelibale', 'ayee_its_aquaa'])

    # Liking
    # Liking by Tags
    session.like_by_tags(['thisisaccra', 'accra', 'ghanaposts', 'kumasi', 'idoghana', 'ghana'], amount=10)
finally:
    # end the bot session
    session.end()
