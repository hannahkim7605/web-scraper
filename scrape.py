from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, "lxml")

csv_file = open("scraped_from_source.csv", "w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "video_link"]) # headers to the csv file

for article in soup.find_all("article"): # equals to find_all("article", limit=1)

    headline = article.h2.a.text
    print(headline)
    summary = article.find("div", class_="entry-content").p.text
    print(summary)

    try:
        vid_src = article.find("iframe", class_="youtube-player")["src"] # like a dictionary
        vid_id = vid_src.split("/")[4] # To get the 5th element
        vid_id = vid_id.split("?")[0] # To get the first one
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except TypeError:
        yt_link = None
    
    print(yt_link)
    print()
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()