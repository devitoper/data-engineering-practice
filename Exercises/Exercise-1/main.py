import requests
import os
import zipfile


download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

# file_names = []
file_paths = []

def main():
    try:
        # 1. cree el directorio `downloads` si no existe
        downloads_folder = os.path.join(os.path.expanduser('.'), 'Downloads')
        os.makedirs(downloads_folder, exist_ok=True)

        # 2. descargue los archivos uno por uno.
        for download_uri in download_uris:
            response = requests.get(download_uri)
            if response.status_code != 200:
                print(f"Error al descargar el archivo: {download_uri}")
                return
            else:
                file_name = download_uri.split('/')[-1]
                file_path = os.path.join(downloads_folder, file_name)
                open(f"{file_path}", "wb").write(response.content)
                # 3. separe el nombre del archivo de la uri, 
                #    para que el archivo mantenga su nombre de archivo original.                
                file_paths.append(file_path)

        # 4. Cada archivo es un `zip`, extraiga el `csv` del `zip` y elimínelo.
        #    el archivo `zip`.
        for file_path in file_paths:
            path_file_zip = f"{file_path}"
            with zipfile.ZipFile(file_path, 'r') as zip_archive:
                list_of_file_names = zip_archive.namelist()
                for file in list_of_file_names:
                    print(file)
                    if file.startswith('__MACOSX'):
                        continue
                    if file.endswith('.csv'):
                        zip_archive.extract(file, path=downloads_folder)
                    os.remove(file_path)
        


    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
