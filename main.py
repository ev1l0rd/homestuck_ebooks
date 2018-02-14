# homestuck_ebooks - Generate Homestuck tweets with markov chains
# Copyright (C) 2018 Valentijn "Ev1l0rd"
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   Additional Terms 7.b and 7.c of AGPLv3 apply to this file:
#       * Requiring preservation of specified reasonable legal notices or
#         author attributions in that material or in the Appropriate Legal
#         Notices displayed by works containing it.
#       * Prohibiting misrepresentation of the origin of that material,
#         or requiring that modified versions of such material be marked in
#         reasonable ways as different from the original version.
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
        api.update_status(status)
        break
