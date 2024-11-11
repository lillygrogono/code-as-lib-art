# Import the requests library
import requests

# Import BeautifulSoup
from bs4 import BeautifulSoup

# Request to retrieve poetry from four different websites
the_guest_house = requests.get("https://www.poemhunter.com/poem/the-guest-house-2/")
sidewalk_ends = requests.get("https://www.poemhunter.com/poem/where-the-sidewalk-ends-4/")
wild_geese = requests.get("https://livelovesimple.com/wild-geese-mary-oliver/")
the_city = requests.get("https://www.poetryfoundation.org/poems/51295/the-city-56d22eef2f768")
road_taken = requests.get("https://www.poemhunter.com/poem/the-road-not-taken/")
caged_bird = requests.get("https://www.poemhunter.com/poem/caged-bird-21/")

# Parse the HTML for each from each file
the_guest_house_html = BeautifulSoup(the_guest_house.text, "html.parser")
sidewalk_ends_html = BeautifulSoup(sidewalk_ends.text, "html.parser")
wild_geese_html = BeautifulSoup(wild_geese.text, "html.parser")
the_city_html = BeautifulSoup(the_city.text, "html.parser")
road_taken_html = BeautifulSoup(road_taken.text, "html.parser")
caged_bird_html = BeautifulSoup(caged_bird.text, "html.parser")

# Extract the text and save it as a name
the_guest_house_text = the_guest_house_html.get_text()
sidewalk_ends_text = sidewalk_ends_html.get_text()
wild_geese_text = wild_geese_html.get_text()
the_city_text = the_city_html.get_text()
road_taken_text = road_taken_html.get_text()
caged_bird_text = caged_bird_html.get_text()


# write the text in each txt file to the name I've given it
with open('the_guest_house.txt', 'w') as guest_data:
    guest_data.write(the_guest_house_text)

with open('sidewalk_ends.txt', 'w') as sidewalk_data:
    sidewalk_data.write(sidewalk_ends_text)

with open('wild_geese.txt', 'w') as geese_data:
    geese_data.write(wild_geese_text)

with open('the_city.txt', 'w') as city_data:
    city_data.write(the_city_text)

with open('road_taken.txt', 'w') as road_data:
    road_data.write(road_taken_text)

with open('caged_bird.txt', 'w') as caged_data:
    caged_data.write(caged_bird_text)

# Function to get poetry content from <p> tags (bc I wanted the whole body of text)
def getPoetryContent(soupdata):  
    paragraphs = soupdata.select("p")  
    if paragraphs:
        for para in paragraphs:
            print(para.text)

# Print the poetry content from <p> tags
print("Guest House........")
getPoetryContent(the_guest_house_html)

print("\nWhere the Sidewalk Ends.........")
getPoetryContent(sidewalk_ends_html)

print("\nWild Geese........")
getPoetryContent(wild_geese_html)

print("\nThe City.........")
getPoetryContent(the_city_html)

print("\nRoad Taken.........")
getPoetryContent(road_taken_html)

print("\nCaged Bird.........")
getPoetryContent(caged_bird_html)
