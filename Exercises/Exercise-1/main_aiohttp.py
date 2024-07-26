import aiohttp
import asyncio
import os
import zipfile
import time


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

semaphore = asyncio.Semaphore(10)
downloads_folder = os.path.join(os.path.expanduser('.'), 'Downloads')


async def make_request(async_session: aiohttp.ClientSession, url:str):
    # Semaphore for limiting concurrent requests to 8
    file_name = url.split('/')[-1]
    file_path = os.path.join(downloads_folder, file_name)    
    async with semaphore:
        # Asynchronous GET request
        async with async_session.get(url=url) as _response:
            if _response.status != 200:
                print(f"Error al descargar el archivo: {url}")                        
            else:
                with open(f"{file_path}", "wb") as f:
                # 3. separe el nombre del archivo de la uri, 
                #    para que el archivo mantenga su nombre de archivo original.
                    async for chunk in _response.content.iter_chunked(1024):
                        f.write(chunk)
                await extract_csv(file_path)
                   

async def extract_csv(file_path: str):
    # 4. Cada archivo es un `zip`, extraiga el `csv` del `zip` y elimínelo.
    #    el archivo `zip`.
    with zipfile.ZipFile(file_path, 'r') as zip_archive:
        list_of_file_names = zip_archive.namelist()
        for file in list_of_file_names:
            if file.startswith('__MACOSX'):
                continue
            if file.endswith('.csv'):
                zip_archive.extract(file, path=downloads_folder)
            os.remove(file_path) 


async def makes_all_requests(urls: list[str]):
    # Stores all tasks that will later be used on `asyncio.gather`
    async with aiohttp.ClientSession() as async_session:
        tasks = []
        for url in urls:
            # Creates asyncio.Task that will return a future
            task = asyncio.create_task(
                coro=make_request(
                    async_session=async_session,
                    url=url,
                )
            )

            tasks.append(task)
        
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    # Marca el tiempo inicial
    start_time = time.perf_counter()
    os.makedirs(downloads_folder, exist_ok=True)
    asyncio.run(makes_all_requests(urls=download_uris))
    # Marca el tiempo final
    end_time = time.perf_counter()
    # Calcula el tiempo transcurrido
    elapsed_time = end_time - start_time

    print(f"El código tardó {elapsed_time:.5f} segundos en ejecutarse.")

# run-1  | Error al descargar el archivo: https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip
# run-1  | El código tardó 52.64710 segundos en ejecutarse.