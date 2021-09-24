import requests
from bs4 import BeautifulSoup
import re  # Regular Expression Manipulation (pattern matching)
import sys  # for argument parsing

# Exception Handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# url = "https://www.ted.com/talks/ma_jun_an_interactive_map_to_track_and_end_pollution_in_china"
# url = "https://www.ted.com/talks/jamie_c_beard_the_untapped_energy_source_that_could_power_the_planet"

r = requests.get(url)
print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.find_all("script"):
    if (re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
mp4_url = result_mp4.split('"')[0]

print("Downloading video from ..." + mp4_url)
file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ... "+ file_name)

r = requests.get(mp4_url)

with open(file_name, 'wb') as f:
    f.write(r.content)

print("Download process finished")