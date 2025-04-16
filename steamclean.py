import os
import requests
import re
import shutil

# PATH TO YOUR STEAMAPPS FOLDER HERE
directory = 'COPY PASTE PATH HERE'
if os.name == 'nt':
  common = rf'{directory}\common'
if os.name == 'posix':
  common = f'{directory}/common'
extension = '.acf'

steamids = []

for f in os.listdir(directory):
    full_path = os.path.join(directory, f)
    if os.path.isfile(full_path) and f.endswith(extension):
        steamids.append(f[12:-4])

def get_game_name(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if str(appid) in data and 'data' in data[str(appid)] and 'name' in data[str(appid)]['data']:
            return data[str(appid)]['data']['name']
        else:
            return None
    else:
        print("An issue has occurred. No support will be provided, exiting...")
        exit()

def clean(gamename):
    gamename = re.sub(r'\(.*?\)', '', gamename)
    gamename = re.sub(r'[™®]', '', gamename)
    gamename = gamename.strip()
    return gamename

def get_dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if total_size < 1024.0:
            break
        total_size /= 1024.0
    return f"{total_size:.2f} {unit}"


steamgames = []
for x in steamids:
  appid = x
  gamename = get_game_name(appid)
  if gamename is not None:
    steamgames.append(clean(gamename))

folders = [d for d in os.listdir(common) if os.path.isdir(os.path.join(common, d))]
folders = [d for d in folders if d not in steamgames]
print('The following game folders do not match the Steam app names for your installed games. Please check if you have them installed, and if not, you may remove them by typing their name here. If you wish to exit, type "Exit". This may take a while if you have large folders.')

if os.name == 'nt':
  for x in folders:
    size = get_dir_size(rf"{common}\{x}")
    print(f"{x}  {size}")
if os.name == 'posix':
  for x in folders:
    size = get_dir_size(f"{common}/{x}")
    print(f"{x}  {size}")


userinput = ""
while 1 == 1:
  print("Choose a game to delete, or exit")
  userinput = input()
  if userinput == "Exit":
    exit()
  else:
    if os.name == 'nt':
      shutil.rmtree(rf"{common}\{userinput}")
    if os.name == 'posix':
      shutil.rmtree(f"{common}/{userinput}")
