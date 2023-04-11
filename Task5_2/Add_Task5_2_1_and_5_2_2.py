from zeep import Client

client = Client('http://secure.smartbearsoftware.com/samples/testcomplete10/webservices/Service.asmx?WSDL')
headers = {'User-Agent': 'Python Learning Requests'}


# Task1

def get_object():
    client.transport.session.headers.update(headers)
    sample = client.service.GetSampleObject(3)
    sample['Name'] = 'My Test'
    sample['X'], sample['Y'] = sample['Y'], sample['X']
    return sample


def return_object():
    result = client.service.SetSampleObject(get_object())
    return result


# Task2

def get_info_book():
    client.transport.session.headers.update(headers)
    data_info = client.service.GetXmlData()
    books_info = {}
    for book in data_info:
        books_info['Id - ' + book.get("id")] = [
            'Title - ' + book.find("title").text,
            'Genre - ' + book.find('genre').text,
            'Review - ' + book.find("review").text,
            'Price - ' + book.find('price').text]
    return books_info


if __name__ == '__main__':
    print(return_object())
    print(get_info_book())
