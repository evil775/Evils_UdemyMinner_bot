# UdemyBot - A Simple Udemy Free Courses Scrapper

#  EvilerX https://github.com/evil775/Evils_UdemyMinner_bot/

import os

token = os.environ.get('TOKEN')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

START = """
Hey, I'm an UdemyMinner. ⚡

I can send you paid Udemy Courses Links for Free.

Commands:
    /discudemy page
    /udemy_freebies page
    /tutorialbar page
    /real_discount page
    /coursevania
    /idcoupons page

page - which page you wanted to scrap and send links. Default is 1
Repo - evil775/Evils_UdemyMinner_bot
"""

CMD = "(discudemy|coursevania|udemy_freebies|tutorialbar|real_discount|idcoupons)"
