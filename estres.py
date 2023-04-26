import requests
import concurrent.futures

url = "https://faceidtest-production.up.railway.app/face/getFaces"
# url = "http://localhost:3001/face/getFaces"



def send_request():
    files = {
        'ine': open('test.jpg', 'rb')
    }
    response = requests.post(url, files=files)
    print(response.status_code) 

def concurrent(n):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        _ = [executor.submit(send_request) for _ in range(n)]


def not_concurrent(n):
    for _ in range(n):
        send_request()


if __name__ == "__main__":
    n = 20
    
    not_concurrent(n)








