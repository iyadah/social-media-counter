from instaloader import Instaloader, Profile

L = Instaloader()
up = input('Enter your instagram handle default (mileycyrus): ') or 'mileycyrus'
profile = Profile.from_username(L.context, up)

print(profile.followers)
