import json
import requests


def retrieve_messages(channel_id):
    token = 'MjU5MTk3MTkyNDk2MDg3MDQw.YHJKqQ.8fYWw-HDwBu5rPDB1Z2YFI7PI4o'
    headers = {
        'authorization': token
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    json_object = json.loads(r.text)

    return json_object
    # for value in json_object:
        # print(value, '\n')
        # content is stored in json object 'value' under 'content', so value['content'] wwill retrieve it

if __name__ == '__main__':
    dm_list = ['817893084632186890', '232150811445166080', '437644030386372611', '627586407552253952',
               '187310476483493888', '243880026586611713', '298270435785572353']

    for dm in dm_list[1]:
        content = retrieve_messages(dm)
        print(type(content))
        for k,v in content.items():
            print(k, v)