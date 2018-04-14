"""Script to text me when certain items are available in Splatnet."""
import os
import re

from twilio.rest import Client
from twitter import OAuth2, Twitter
from twitter.oauth_dance import oauth2_dance

# TODO: Update this to have functions and tests. Update this to also look for
# manufactures and certain abilities


def main(event, context):
    """Query twitter for splatnet items and send a SMS if necessary."""
    bearer_token = oauth2_dance(os.environ["TWITTER_KEY"], os.environ["TWITTER_SECRET"])
    twitter = Twitter(auth=OAuth2(bearer_token=bearer_token))

    recent_tweet = twitter.statuses.user_timeline(screen_name="splatnetstore", count=1)
    tweet_content = recent_tweet[0]["text"]

    # If desired we can use this to find specific manufacturers/abilities/items.
    tweet_match = re.match("^(.+?)\\n(.+?)\\n(.+?)\\n(.+?)\\n(.+?)https", tweet_content)
    if "3" not in tweet_match.group(5):
        return tweet_content

    client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_SECRET"])
    client.messages.create(
        to=os.environ["RECIPIENT_NUMBER"],
        from_=os.environ["TWILIO_NUMBER"],
        body=tweet_content,
    )
    return True


if __name__ == "__main__":
    main(None, None)
