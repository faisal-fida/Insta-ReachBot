import requests
from rich import print
from statistics import mean

def human_format(num):
    if num > 5000:
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num = round(num / 1000.0, 2)
        return '{:.{}f}{}'.format(num, 2, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])
    else:
        return num

def get_userDetail(username):
    proxies = {"https": 'billylu2.ddns.net:3333'}
    base_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
    }
    comments,likes = [],[]
    try:
        res = requests.get(base_url.format(id),headers=headers,proxies=proxies)
        user_info = res.json()
        data = user_info['data']['user']
        followers = data['edge_followed_by']['count']
        posts = data['edge_owner_to_timeline_media']['edges']
        num = 1
        like = 0
        coment = 0 
        for x in posts[:9]:
            comments_c = x['node']['edge_media_to_comment']['count']
            likes_c = x['node']['edge_liked_by']['count']
            coment += comments_c
            like += likes_c
            num += 1
            comments.append(comments_c)
            likes.append(likes_c)
        total = like + coment
        total = int(total/9)
        total = int(followers/total)
        total = str(total) + '%'
        comments = human_format(round(mean(comments)))
        likes = human_format(round(mean(likes)))
        
        return {'Total Reach':total,'Followers':human_format(followers),'Comments':comments,'Likes':likes}
        
    except Exception as e:
        return "getting user failed, due to '{}'".format(e.message)
