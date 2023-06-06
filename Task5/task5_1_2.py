import requests


url = "http://httpbin.org/post"
headers = {"User-Agent": "Python Learning Requests"}
form = {"comments": "Test post",
        "custemail": "putler@kaput",
        "custname": "Tester",
        "custtel": "+38097654321",
        "delivery": "12:15",
        "size": "large",
        "topping": ["bacon", "mushroom"]
        }

def post_request():
    request = requests.post(url = url, headers = headers, data = form).json()
    return request["form"], request["headers"]

if __name__ == '__main__':
    print(post_request())