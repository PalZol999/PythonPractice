import bs4, requests

def getAlzaPrice(productURL):
    res = requests.get(productURL)
    #res.raise_for_status()   not requiered, but ggod to have if any request error

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('#__layout > div > header > div > div > div > nav > ul > li:nth-child(1) > a')

    return elems[0].text.strip() if elems else None

elem = getAlzaPrice('https://nexus.hexagon.com/')

if elem:
    print(f'The name of the selected elememt is {elem}')
else:
    print("No elements found with the specified selector.")
