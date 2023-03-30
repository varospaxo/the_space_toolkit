import requests
import time
import datetime
def scheduler():
    # t = time.localtime()
    # current_hour = time.strftime("%H", t)
    # current_minute = time.strftime("%M", t)
    # print(current_hour)
    # print(current_minute)
    # # t = datetime.time(19, 4)
    # t = datetime.time(int(current_hour), int(current_minute))
    # # print(t)
    # result = datetime.datetime.combine(datetime.date.today(), t) + datetime.timedelta(minutes=2)
    # # print(result)
    # only_t = result.time()
    # # print(only_t)
    # timelast = datetime.datetime.strptime(str(only_t), '%H:%M:%S')
    # hour = timelast.hour
    # minute = timelast.minute
    # print (hour)
    # print (minute)

    username = 'launchmail'
    token = 'd2e02d0bb23ab2c182949328224fc9df906e5c20'
    host = 'www.pythonanywhere.com'
    # command="python LaunchNotifier.py"
    # enabled='true'
    # interval= "daily"
    # description='quac'
    # id=356533
    # response = requests.patch(f'https://{host}/api/v0/user/{username}/schedule/{id}/'.format(
            # host=host, username=username, id=id
        # ),
    response = requests.get(f'https://{host}/api/v0/user/{username}/schedule/'.format(
            host=host, username=username
        ),
    headers={'Authorization': f'Token {token}'.format(token=token)})

    # headers={'Authorization': f'Token {token}'.format(token=token)}, json={'hour': '{hour}'.format(hour=hour), 'minute': '{minute}'.format(minute=minute), 'description' : '{description}'.format(description=description)})
    if response.status_code == 200:
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

scheduler()