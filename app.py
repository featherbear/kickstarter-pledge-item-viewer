#!/usr/bin/python3

PROJECT_URL = "https://www.kickstarter.com/projects/flipper-devices/flipper-zero-tamagochi-for-hackers"

from urllib.request import urlopen
from urllib.parse import quote
from lxml import etree

resp = urlopen(PROJECT_URL)
tree = etree.parse(resp, etree.HTMLParser())

def extract(xml):
    for pledge in xml.xpath("/html/body/main/div/div/div[2]/section[1]/div/div/div/div[2]/div/div[2]/div/ol/li"):
        e = [*pledge.xpath("div[2]/h3"), None][0]
        if e is None: continue
        remaining = [*pledge.xpath("div[2]/div[3]/span[1]"), None][0]
        if remaining is None: continue
        yield (e.text.strip(), remaining.text.strip())

remainingDays = tree.xpath("/html/body/main/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[3]/div/div/span[1]")[0].text.strip()

textbuffer = ""

# print("Days remaining:", remainingDays)
textbuffer += f"Days remaining: {remainingDays}\n\n"

for pledge in extract(tree):
    # print(*pledge)
    textbuffer += f"* {pledge[0]} - {pledge[1]}\n"

print(textbuffer)
