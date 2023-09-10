import tweepy
import os
from model import Model
import random

from dotenv import load_dotenv
load_dotenv()

def get_twitter_score(user_name:str):
    # API keyws that yous saved earlier
    api_key = os.getenv("API_KEY")
    api_secrets = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN_KEY")
    access_secret = os.getenv("ACCESS_TOKEN_SCECRET")

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key,api_secrets)
    auth.set_access_token(access_token,access_secret)

    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print('Successful Authentication')
    except:
        print('Failed authentication')

    # user_name = "CryptomeriaCap" # put 
    # _id = "103770785"
    #user = api.get_user(id = _id)
    user =api.get_user(screen_name = user_name)

    return [user.followers_count, user.listed_count, user.statuses_count]

def generate_proof(features : list):

    model = Model()
    score = model.forward(features)
    score_ranges = [(6, 10, (100, 300)),
                    (10, 20, (300, 500)),
                    (20, 50, (500, 1300)),
                    (50, 1000000000, (1300, 5000))]

    for min_score, max_score, rand_range in score_ranges:
        if min_score <= score < max_score:
            random_number = random.randint(*rand_range)
            break
    else:
        random_number = random.randint(30, 100)

    print(random_number)
    
    return random_number

def get_rank_proof(rank : str):
    
