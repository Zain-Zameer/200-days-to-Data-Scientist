import multiprocessing
import requests
import concurrent.futures

def downloadFile(name):
    print(f"started downloading {name}")
    url = 'https://picsum.photos/2000/3000'
    r = requests.get(url, allow_redirects=True)
    open(f"./files/{name}.jpg", 'wb').write(r.content)
    print(f"Finished downloading {name}")

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executer:
        results = executer.map(downloadFile,[1,2,3])
        for r in results:
            print(r)