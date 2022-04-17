# By J.P. Moreno
import requests
from tqdm import tqdm
from gen_data import *
from data import *
import random

baseurl = "http://localhost:8000/"

login_url = baseurl + "token/"
createuser_url = baseurl + "users/"
createrest_url = baseurl + "restaurants/"
addmenu_url = baseurl + "menus/"
comment_url = baseurl + "comments/"
follow_url = baseurl + "follows/"
like_url = baseurl + "restaurant_likes/"
blog_url = baseurl + "blogs/"
bloglike_url = baseurl + "blog_likes/"

owner_rest_pairs = gen_data()


for owner, rest, rest_type in owner_rest_pairs:
    res = requests.post(createuser_url, json = {"first_name": owner.first_name, "last_name": owner.last_name, "username": owner.username, "email": owner.email, "phonenumber":owner.phone_number, "password": "password"})

def send_requests(owner, rest, rest_type):
    res = requests.post(login_url, json = {"username": owner.username, "password": "password"})
    token = res.json()["access"]
    bearer = "Bearer " + token
    headers = {"Authorization": bearer, "Content-Type": "application/json"}
    body = {"name":rest.name, "desc":rest.desc, "address":rest.address, "phonenumber":rest.phone_number, "postalcode": rest.postal_code}
    res = requests.delete(createrest_url, headers=headers)
    res = requests.post(createrest_url, headers=headers, json=body)
    rest_id = res.json()["id"]
    foods = globals()[rest_type+"_foods"] + drinks
    #foods
    for food in foods:
        body = {"name":food[0], "desc":food[1], "price":food[2]}
        res = requests.post(addmenu_url, headers=headers, json=body)
    
    interacters = random.sample(owner_rest_pairs, 20)
    for i in range(15):
        body = {"name":f"Lorem Impsum #{i}", "text":lorem_ipsum}
        res = requests.post(blog_url, headers=headers, json=body)
        blog_id = res.json()["id"]
        for interacter in interacters:
            interacter = interacter[0]
            res = requests.post(login_url, json = {"username": interacter.username, "password": "password"})
            itoken = res.json()["access"]
            ibearer = "Bearer " + itoken
            iheaders = {"Authorization": ibearer, "Content-Type": "application/json"}
            liked = random.uniform(0,1)
            if liked <0.8:
                body = {"blog_id":blog_id}
                res = requests.post(bloglike_url, headers=iheaders, json=body)

    # Comments Likes Follows
    interacters = random.sample(owner_rest_pairs, 20)
    for person, r, rt in interacters:
        # login
        res = requests.post(login_url, json = {"username": person.username, "password": "password"})
        itoken = res.json()["access"]
        ibearer = "Bearer " + itoken
        iheaders = {"Authorization": ibearer, "Content-Type": "application/json"}
        liked = random.uniform(0,1)
        if liked <0.8:
            food = random.choice(foods)
            comment_choice = random.uniform(0,1)
            body = {"restaurant_id":rest_id}
            res = requests.post(follow_url, headers=iheaders, json=body)
            res = requests.post(like_url, headers=iheaders, json=body)

            if comment_choice < 0.33:
                comment = f"The {food[0]} was great! I would come back here again"
            elif comment_choice < 0.66:
                comment = f"I am a big fan of the {food[0]}, best I ever had!"
            else:
                comment = f"The owner {owner.first_name} is such a great person, great service!"



        else:
            food = random.choice(foods)
            comment = f"The {food} was terrible! I will never come back here again"
        body = {"restaurant_id":rest_id, "text": comment}
        res = requests.post(comment_url, headers=iheaders, json=body)
    

for owner, rest, rest_type in tqdm(owner_rest_pairs):
    send_requests(owner,rest,rest_type)

