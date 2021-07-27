import requests

url = "http://roadsandpits.ispringlearn.ru/catalog/course/get_requests?course=7bd78a78-eec8-11eb-a7cf-224c9100cc82"

payload = "page=1&rows=10&order_field=request_date&order_asc=1"
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?1',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Origin': 'https://roadsandpits.ispringlearn.ru',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://roadsandpits.ispringlearn.ru/catalog/course/requests?course=7bd78a78-eec8-11eb-a7cf-224c9100cc82',
  'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,it;q=0.6',
  'Cookie': '_ym_d=1626256566; _ym_uid=1626256566573078026; _ga=GA1.2.1856173668.1626256567; _fbp=fb.1.1626256567004.515462324; _lk=560a82a7ba1d37a7351ae8117205d7a4; _gid=GA1.2.489360085.1627284928; _ym_isad=2; browser_has_html5_support=true; browser_has_local_storage_support=true; learnsid=a3vukbgs48pkhol0ns8b0fvr3c; locale=ru-RU; _ym_visorc=w; _gat_UA-4863694-53=1; learnsid=a3vukbgs48pkhol0ns8b0fvr3c; locale=0; onboarding_popup_was_shown=0'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
