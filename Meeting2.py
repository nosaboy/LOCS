"""
Explanation:

Import requests: We must first import the request module( smth thats not built into python) so that we can use it to send requests to the server. After doing this, we must wait a few seconds for the download.
Requests.get(url) will send a GET request to the url provided. A GET request will then request data from the server( in this case, we are requesting a random quote from our url).
data.json(): We have our response data in JSON format. We want to now convert it into a dictionary so that we can access a certain part of the information we want( which is the random quote)
response[“quote”][“body”]: opening the link https://favqs.com/api/qotd, we note that the actual quote is stored under “quote”:{ “body”: }, so the key to access the quote would be [“quote”][“body”].
print(quote): we output the quote, note that we get a different quote each time even though we didn't write any of it. This is why APIs are useful, it can save us a lot of time and energy.
We can also print out the author by getting response["quote]["author"] from the dict.
"""

import requests  # imports request module so we can use it to send requests
# takes a few seconds to download
url = "https://favqs.com/api/qotd"  # link to the Application we will be using
data = requests.get(url)  # send a request to API and store it in variable named data
response = data.json()  # convert our request into a python dictionary
# print(response)
quote = response["quote"]["body"]  # get the quote itself
author = response["quote"]["author"]  # get author of quote
print(quote)  # print out quote
print("-", author)  # print out author name
