import tweepy
import json
import os
import random
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TwitterBot:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.api = None
        if not dry_run:
            self._authenticate()
        self._load_content()

    def _authenticate(self):
        consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            raise ValueError('Missing Twitter API credentials in environment variables')
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def _load_content(self):
        with open('content.json', 'r') as f:
            self.content = json.load(f)

    def get_todays_post(self):
        day_of_week = datetime.now().weekday()  # Monday=0, Sunday=6
        if day_of_week < 5:  # Weekday
            post_type = 'tool_spotlight'
        else:  # Weekend
            post_type = 'code_tip'
        
        # Simple rotation: use a counter file to keep track, or random
        # For demo, select random from list
        posts = self.content.get(post_type, [])
        if not posts:
            logger.warning(f'No posts of type {post_type} found')
            return None
        post = random.choice(posts)
        # Format post with random tool if needed
        if post_type == 'tool_spotlight':
            tools = self.content.get('tools', [])
            if tools:
                tool = random.choice(tools)
                post['text'] = post['template'].format(tool_name=tool['name'], tool_desc=tool['description'], tool_lines=tool['lines'])
        elif post_type == 'code_tip':
            tips = self.content.get('tips', [])
            if tips:
                tip = random.choice(tips)
                post['text'] = post['template'].format(tip=tip['text'])
        return post

    def post_tweet(self, post):
        if post is None:
            logger.info('No post to send')
            return
        text = post.get('text', '')
        # Ensure within 280 characters, but templates should be short
        if len(text) > 280:
            text = text[:277] + '...'
        if self.dry_run:
            logger.info(f'[DRY RUN] Would tweet: {text}')
            return
        try:
            self.api.update_status(text)
            logger.info(f'Tweet posted: {text[:50]}...')
        except tweepy.TweepyException as e:
            logger.error(f'Failed to post tweet: {e}')

    def handle_mentions(self):
        # Check mentions since last run (simplified - in production use streaming or webhook)
        # This is a placeholder for interactive functionality
        pass

    def run_daily(self):
        post = self.get_todays_post()
        self.post_tweet(post)
        # Optionally, also post a contributor shoutout randomly
        if random.random() < 0.3:  # 30% chance
            shoutout = self.content.get('shoutouts', [])
            if shoutout:
                shout = random.choice(shoutout)
                self.post_tweet(shout)

if __name__ == '__main__':
    dry_run = os.environ.get('DRY_RUN', 'false').lower() == 'true'
    bot = TwitterBot(dry_run=dry_run)
    bot.run_daily()
