from slackbot.bot import respond_to
import requests
import random
import sys
sys.path.append('..')

import settings
CHANNEL_ID = settings.CHANNEL_ID
SLACK_API_TOKEN = settings.SLACK_API_TOKEN

@respond_to('')
def main(message):
    url = 'https://slack.com/api/channels.info?token={0}&channel={1}&pretty=1'.format(SLACK_API_TOKEN, CHANNEL_ID)
    response = requests.get(url).json()
    channel_info = response["channel"]
    member_id = channel_info["members"]
    member_id_list = [id for id in member_id]
    name_active_dict = member(member_id_list)
    active_member = []

    for key, value in name_active_dict.items():
        if value == 'active':
            active_member.append(key)

    active_member = random.sample(active_member, len(active_member))
    member_text = ''

    for i, active_name in enumerate(active_member):
        member_text = member_text + '{} : {}\n'.format(i+1, active_name)
            
    message.reply(member_text)


def member(member_id_list):
    member_dict = {}
    user_list = []
    is_active_list = []

    for name_id in member_id_list:
        user_url = 'https://slack.com/api/users.info?token={0}&user={1}&pretty=1'.format(SLACK_API_TOKEN, name_id)
        active_user_url = 'https://slack.com/api/users.getPresence?token={0}&user={1}&pretty=1'.format(SLACK_API_TOKEN, name_id)

        user_response = requests.get(user_url).json()
        active_user_response = requests.get(active_user_url).json()

        user_list.append(user_name(user_response))
        is_active_list.append(is_active_user(active_user_response))

    for user, active in zip(user_list, is_active_list):
        member_dict[user] = active
    
    return member_dict


def user_name(user_response_json):
    user = user_response_json["user"]
    user_profile = user["profile"]
    name = user_profile["real_name"]
    return name


def is_active_user(active_user_response_json):
    is_active = active_user_response_json["presence"]
    return is_active
