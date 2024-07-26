

import requests
from bs4 import BeautifulSoup
import os

def clone_github_repos(topic_url):
    response = requests.get(topic_url)
    soup = BeautifulSoup(response.content, "html.parser")

    repo_links = []
    for repo in soup.find_all("h3", {"class": "f3 color-fg-muted text-normal lh-condensed"}):
        a_tag = repo.find("a")
        if a_tag:
            repo_links.append(f"https://github.com{a_tag['href']}.git")

    for repo in repo_links:
        os.system(f"git clone {repo}")

    print("All projects have been cloned.")

if __name__ == "__main__":
    topic_url = input("Enter the GitHub topic URL: ")
    clone_github_repos(topic_url)
