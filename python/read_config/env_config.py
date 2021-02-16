import os 


print("""
using `os.environ.get('TEMPLATES_FAV_FRUIT')` get will return `None` if a key is not present rather than raise a `KeyError`
""")

print(
    os.environ.get('TEMPLATES_FAV_FRUIT'))


print(
    """
    `os.getenv('TEMPLATES_FAV_COLOR', 'purple')` is equivalent, and can also give a default value, purple, instead of `None`
    """)

print(
    os.getenv('TEMPLATES_FAV_COLOR', 'purple'))


if 'TEMPLATES_FAV_COLOR' in os.environ:
    fav_color = os.environ.get('TEMPLATES_FAV_COLOR')
else:
    print("What is your favorite color?")
    os.environ['TEMPLATES_FAV_COLOR'] = input()

if 'TEMPLATES_FAV_FRUIT' in os.environ:
    fav_fruit = os.environ.get('TEMPLATES_FAV_FRUIT')
else:    
    print("What is your favorite fruit?")
    os.environ['TEMPLATES_FAV_FRUIT'] = input()

print(f"Your favorite thing must be {os.environ.get('TEMPLATES_FAV_COLOR')} {os.environ.get('TEMPLATES_FAV_FRUIT')}")



