import instaloader

v = instaloader.Instaloader()

username ='yourusername'

print(v.download_profile(username,profile_pic_only=True))
