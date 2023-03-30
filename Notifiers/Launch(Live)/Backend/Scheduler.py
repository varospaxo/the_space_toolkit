import requests
username = 'launchmail'
token = 'd2e02d0bb23ab2c182949328224fc9df906e5c20'
host = 'www.pythonanywhere.com'
command="python LaunchNotifier.py"
enabled='true'
interval= "daily"
hour='19'
minute= '00'
description='quac'
id=356533
response = requests.patch(f'https://{host}/api/v0/user/{username}/schedule/{id}/'.format(
        host=host, username=username, id=id
    ),
headers={'Authorization': f'Token {token}'.format(token=token)}, json={'hour': '{hour}'.format(hour=hour), 'minute': '{minute}'.format(minute=minute), 'description' : '{description}'.format(description=description)})
if response.status_code == 200:
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))