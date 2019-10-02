import re
import vk
from time import sleep
from tqdm import tqdm_notebook
# parser init params
TOKEN = "KEY"
session = vk.Session(access_token=TOKEN)
vk_api = vk.API(session)

# target init params
GROUP_ID = 78280187



def get_data(group_id=GROUP_ID, offset_coeff=10):

    group_id = group_id * -1
    
    
    first_init = vk_api.wall.get(owner_id=group_id, v=5.84)
    content = first_init["items"]
    count = first_init["count"] // offset_coeff

    for i in tqdm_notebook(range(1, count+1)):
        content = content + vk_api.wall.get(owner_id=group_id, v=5.84, offset=i*offset_coeff, filter="other")["items"]


    print("Total posts: {} | Offset coefficient: {}".format(len(content), offset_coeff))

    return content
