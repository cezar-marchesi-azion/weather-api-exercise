import json
import os
import hashlib
import glob
import time
import pycountry


def save_city_to_json(data: dict, city_name: str) -> None:
    create_tmp_folder()
    hashed_city_name = hash_city_name(city_name)
    with open('tmp/' + hashed_city_name + '.json', 'w') as outfile:
        json.dump(data, outfile)


def create_tmp_folder() -> None:
    if not os.path.exists('tmp'):
        os.makedirs('tmp')


def hash_city_name(city_name: str) -> str:
    city_name = city_name.encode('utf-8')
    return hashlib.sha256(city_name).hexdigest()


def get_cached_jsons_from_tmp_folder(max_number):
    list_of_all_cached_files = glob.glob('tmp/*')
    city_info_list = []
    count = 0

    if len(list_of_all_cached_files) < max_number:
        max_number = len(list_of_all_cached_files)

    while count < max_number:
        latest_file = max(list_of_all_cached_files, key=os.path.getmtime)
        with open(latest_file) as json_file:
            data = json.load(json_file)
            city_info_list.append(data)
            list_of_all_cached_files.remove(latest_file)
            count += 1

    return city_info_list


def housekeep_cached_jsons(cache_ttl):
    list_of_all_cached_files = glob.glob('tmp/*')

    for file in list_of_all_cached_files:
        modified_time = os.path.getmtime(file)
        if time.time() - modified_time > cache_ttl:
            os.remove(file)

def get_country_alpha_3(country_alpha_2):
    country = pycountry.countries.get(alpha_2=country_alpha_2)
    return country.alpha_3