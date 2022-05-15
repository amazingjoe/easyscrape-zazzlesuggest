import requests
import urllib.parse
import json

def query(term):
    term=urllib.parse.quote(term.lower())
    # set headers
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36','Referer':'https://www.etsy.com/'}

    # define url
    url = f"https://www.zazzle.com/svc/z3/search/getSuggestedSearch?cv=1&ps=10&skey={term}&strending=true&client=js"

    # store http request into html variable
    html = requests.get(url,params=None,headers=header)
    results = html.json()

    resultlist = []

    for result in results["data"]["sections"][0]["suggestions"]:
        resultlist.append(result["term"])

    # Remove last element
    return resultlist