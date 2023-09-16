import requests

URL = "http://api.mathjs.org/v4/"
HEADERS = {"User-Agent": "Python Learning Requests"}


def get_request(expr, rounding_index):
    data = {"expr": f"sqrt({expr})", "precision": rounding_index}
    response = requests.get(url=URL, headers=HEADERS, params=data).text
    return response


def post_request(expr, rounding_index):
    data = {"expr": expr, "precision": rounding_index}
    response = requests.post(url=URL, headers=HEADERS, json=data).json()
    return response["result"]


"""if __name__ == "__main__":
    print(get_request(5, 3))
    print(post_request(["3+2", "3*2", "pow(3.3, 2)"], 3))"""