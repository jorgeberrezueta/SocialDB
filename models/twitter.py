
class Tweet:
    def __init__(self, tweet_id, text, user_id, created_at, favorite_count, retweet_count):
        self.tweet_id = tweet_id
        self.text = text
        self.user_id = user_id
        self.created_at = created_at
        self.favorite_count = favorite_count
        self.retweet_count = retweet_count

class Profile:
    def __init__(self, user_id, name, screen_name, location, description, followers_count, friends_count, listed_count, created_at, favourites_count, statuses_count, profile_image_url):
        self.user_id = user_id
        self.name = name
        self.screen_name = screen_name
        self.location = location
        self.description = description
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.listed_count = listed_count
        self.created_at = created_at
        self.favourites_count = favourites_count
        self.statuses_count = statuses_count
        self.profile_image_url = profile_image_url