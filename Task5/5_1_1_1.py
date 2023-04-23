import requests


def get_requests_not_200():

    url = "https://nghttp2.org/httpbin/"
    headers = {"User-Agent": "Python Learning Requests"}
    req = requests.get(url = url+'spec.json', headers = headers).json()
    paths = req['paths']
    new_dict = {}

    for path in paths:
        for method in paths[path]:
            for response in paths[path][method]['responses']:
                if response != 200:
                    new_dict[url+path] = response


    return new_dict

if __name__ == '__main__':
    print(get_requests_not_200())

