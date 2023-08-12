predefined_images = [
    {"url": "../static/assets/images/BlackHole.jpg", "alt": "Black hole in space"},
    {"url": "../static/assets/images/Apollo_NA.jpg", "alt": "Astronaut on moon"},
    {"url": "../static/assets/images/roverselfie.jpg", "alt": "Rover selfie on mars"},
    {"url": "../static/assets/images/SpaceTeam to the moon..jpg", "alt": "Artemis 2 team"},
    {"url": "../static/assets/images/RoguePlanet1600.jpg", "alt": "Rogue planet in space"},
    {"url": "../static/assets/images/Milky_way.jpeg", "alt": "Milky way galaxy"},
    {"url": "../static/assets/images/bhm_bluford_sts-8_on_treadmill_s08-13-0361.jpg", "alt": "Guy in spaceship"},
    {"url": "../static/assets/images/darkMatter.jpg", "alt": "Dark matter in space"},
    {"url": "../static/assets/images/iss068e036313_orig.jpg", "alt": "Image of moon"}
]


def get_img_links():
    api_images = []
    for item in data:
        links =item.get("links", [])
        if links:
            preview_link = links[0].get("href")
            api_images.append(preview_link)