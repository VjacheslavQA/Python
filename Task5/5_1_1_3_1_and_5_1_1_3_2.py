import requests



def find_languages_code():
    url = 'https://restcountries.com/v3/all'
    headers = {'user-agent': 'Python Learning Requests'}
    response = requests.get(url=url, headers=headers).json()
    lang = set()
    lang_code = []
    for country in response:
        if 'languages' in country:
            lang.update(country['languages'])
            lang_code = list(lang)
    return lang_code



def number_of_people_using_language(lang_code):
    url = 'https://restcountries.com/v3/lang/'
    headers = {'user-agent': 'Python Learning Requests'}

    result = {}
    population = 0
    for language in lang_code:
        response = requests.get(url=url + language, headers=headers).json()
        for country in response:
            population += country['population']
            result[language] = population
    return result




if __name__ == '__main__':
    print(find_languages_code())
    print(number_of_people_using_language(['ukr', 'swe']))