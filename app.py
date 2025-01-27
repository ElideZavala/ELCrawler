# ***********************-------------------------- Web Scraping --------------------------***********************
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")


questions = soup.select(".s-post-summary")
# print(type(questions))
# print(questions)
# print(questions[0].attrs)
# print(questions[0].get("id", 0))
# print(questions[0].select_one(".s-link"))
# print(questions[0].select_one(".s-link").getText())

# questions = soup.select(".s-link")
for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".todo-no-class-here").getText())