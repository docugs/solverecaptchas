
import requests
def get_enumproxy():
    url = "https://ephemeral-proxies.p.rapidapi.com/v2/datacenter/proxy"

    headers = {
        "X-RapidAPI-Key": "60f7bdf787msh61ddbd43812c12cp1059a4jsnd4564938be2c",
        "X-RapidAPI-Host": "ephemeral-proxies.p.rapidapi.com"}

    
    goodproxy = None
    while not goodproxy:
        print("fetching new proxy...")
        response = requests.request("GET", url, headers=headers).json()
        print(response)
        req = requests.Session()
        host = response["proxy"]["host"]
        port = response["proxy"]["port"]
        proxies =  f"http://{host}:{port}"
        req.proxies = {"http": proxies,
                        "https": proxies}
        res = req.request("GET", "http://ipinfo.io/ip", headers=headers)
        if res.status_code == 200:
            print(res.text)
            goodproxy = True
            print("fetching done.. proxy is good now.")
            return proxies
        else:
            goodproxy = False
            pass
