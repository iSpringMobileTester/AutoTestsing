import requests


def get_enrollments():
    url = "http://api-learn.ispringlearn.ru/enrollment/?learnerIds[]=c0851374-ee10-11eb-8bfc-36298447d46b"

    payload = {}
    headers = {
        'X-Auth-Account-Url': 'https://roadsandpits.ispringlearn.ru',
        'X-Auth-Email': 'testApi@mail.ru',
        'X-Auth-Password': '12345Q'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def enroll_course():
    url = "http://api-learn.ispringlearn.ru/enrollment"

    payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<request>\r\n    <courseIds>\r\n        " \
              "<id>2a474024-ee12-11eb-8461-969860858e51</id>\r\n    </courseIds>\r\n    <learnerIds>\r\n        " \
              "<id>c0851374-ee10-11eb-8bfc-36298447d46b</id>\r\n    </learnerIds>\r\n    <accessDate>2021-05-16 " \
              "06:30:00</accessDate>\r\n    <dueDateType>unlimited</dueDateType>\r\n</request> "
    headers = {
        'X-Auth-Account-Url': 'https://roadsandpits.ispringlearn.ru',
        'X-Auth-Email': 'testApi@mail.ru',
        'X-Auth-Password': '12345Q',
        'Content-Type': 'application/xml'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def enroll_material():
    url = "http://api-learn.ispringlearn.ru/enrollment"

    payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<request>\r\n    <courseIds>\r\n        <id>6f0bd75a-eeb8-11eb-b601-fe30eba2ff50</id>\r\n    </courseIds>\r\n    <learnerIds>\r\n        <id>c0851374-ee10-11eb-8bfc-36298447d46b</id>\r\n    </learnerIds>\r\n    <accessDate>2021-05-16 06:30:00</accessDate>\r\n    <dueDateType>unlimited</dueDateType>\r\n</request>"
    headers = {
        'X-Auth-Account-Url': 'https://roadsandpits.ispringlearn.ru',
        'X-Auth-Email': 'testApi@mail.ru',
        'X-Auth-Password': '12345Q',
        'Content-Type': 'application/xml'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def delete_enrollment():
    url = "http://api-learn.ispringlearn.ru/enrollment/delete"

    # Тут нужно изменить <id> на тот, который нужно удалить
    payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<request>\r\n    <enrollmentIds>\r\n        " \
              "<id>2a474024-ee12-11eb-8461-969860858e51</id>\r\n"\
              "</enrollmentIds>\r\n</request> "
    headers = {
        'X-Auth-Account-Url': 'https://roadsandpits.ispringlearn.ru',
        'X-Auth-Email': 'testApi@mail.ru',
        'X-Auth-Password': '12345Q',
        'Content-Type': 'application/xml'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def edit_enrollment_status():