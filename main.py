import markovify
import yaml
import tweepy
import os
import json


def generate_model():
    if not os.path.isfile('model.json'):
        with open('homestuck.txt', 'r') as txtfile:
            text = txtfile.read()

        text_model = markovify.NewlineText(text)
        model_json = text_model.to_json()

        with open('model.json', 'w') as model_file:
            json.dump(model_json, model_file)
    else:
        with open('model.json', 'r') as model_file:
            model_json = json.load(model_file)
        text_model = markovify.Text.from_json(model_json)
    return text_model


def get_markov(text_model, max_chars, min_chars):
    return text_model.make_short_sentence(max_chars, min_chars)


if not os.path.isfile('config.yaml'):
    with open('config.yaml', 'w') as configfile:
        default_config = dict.fromkeys(['consumer_key', 'consumer_secret', 'access_token', 'access_token_secret'])
        yaml.safe_dump(default_config, configfile, default_flow_style=False)
    exit("A new config file has been generated for you. Fill it with the appropriate values, then restart the application.")

with open('config.yaml', 'r') as configfile:
    config = yaml.safe_load(configfile)

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

text_model = generate_model()

while True:
    status = get_markov(text_model, 280, 40)
    if status:
        api.update_status()
        print(status)
        break
