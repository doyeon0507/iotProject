# Install DHT11 sensor
```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt update
sudo apt install build-essential python-dev python-openssl
sudo python setup.py install

cd Adafruit_Python_DHT
cd examples
python AdafruitDHT.py 11 4
```

# vim dht11.py
```
import time
import Adafruit_DHT
sensor=Adafruit_DHT.DHT11
pin=4
try:
    while True :
        h, t = Adafruit_DHT.read_retry(sensor,pin)
        if h is not None and t is not None :
            print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t,h))
        else :
          print('Read error')
         time.sleep(1)
except KeyboardInterrupt:
    print("Terminated by Keyboard")
 
finally:
    print("End of Program")
```

# influxdb
```
# 1.

curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -

#2. 

echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list 

#3.

sudo apt update
sudo apt install influxdb

#4.

sudo service influxdb start
```


# 데이터베이스 만들기
```
create database <데이터베이스 이름>



확인 : show databases
```


# Grafana Installation

## 1. Repository의 GPG key를 더하기


curl https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -


## 2. Repository를 더하기


echo "deb https://dl.bintray.com/fg2it/deb stretch main" | sudo tee -a/atc/apt/sources.list.d/grafana.list


## 3. 프로그램 설치


sudo apt update
sudo apt install grafana


## 4. 프로그램 실행

sudo service grafana-server start


## influxdb import with python
```
sudo pip install influxdb
```

## gpio pin map
```
cd /tep
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
```


## pwd
```
/home/pi

pwd
/home/pi
git
cd /home/pi/
cd ~
git clone https://github.com/doyeon0507/iotProject
```

## Git hub Use

 - Repository down load

 git clone https://github.com/doyeon0507/iotProject
 

# vim 편집기 사용법
 ```
 set nu       // Line numner
 set cindent  // C language indent
 set ts=4     // tab size 4
 set softtabtop=4
 set bg=dark
 set expandtab
 let python_version_2 = 1
 let python_highlight_all = 1
 filetype indent plugin on
 
 if has("syntax") // sysntax on
  systax on
  endif
```

```
#!/user/bin/python

import time
improt RPI.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO_IN)

def intterrupt_fired(channel):
 print("interrupt Fired")
 print(channel)
 
 GPIO.add_event_detect(4, GPIO.FALLING, callback=interrupt_firde)
 
 while(True);
  time.sleep(1)
  print("timer fired")
````

# 명령어
```
vim pir.py
python pir.py
git add .
git commit -m pirsoftware
git push


sudo apt raspi-config
SNC Viewer
sncserver

cp pir.py Documents/
cp pir.py Documents/pir.py
cd Documents/
ls
>>pir.py


pwd
/home/pi/Documents

cd ..
pwd
/home/pi
```

# bluetooth disable
```
sudo systemctl disable hciuart
```

# grafana
```
sudo service grafana-server start
```
# telegram install
```
pip3 install python-telegram-bot --upgrade

git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive

ls
cd python-telegram-bot/examples/

ls
vim timerbot.py

>> 85 : 1346081175:AAHryYn6BrTHQ_UOabcVyKqOtXmh_KCHQdM

python3 timerbot.py 
vim timerbot.py

>> 35 : Hi Do yeon!!!!!!!!


import RPi.GPIO as GPIO
import time

channel = 4

GPIO
```

### 라즈베리파이 복사-----------------------------------------------------------------------------------------------------------------
```
pi@raspberrypi:~ $ influxdb
bash: influxdb: command not found
pi@raspberrypi:~ $ influx
Connected to http://localhost:8086 version 1.8.0
InfluxDB shell version: 1.8.0
> create database co2
> exit
pi@raspberrypi:~ $ sudo service grafana-server start
pi@raspberrypi:~ $ pip3 install python-telegram-bot--upgrade
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting python-telegram-bot--upgrade
Could not install packages due to an EnvironmentError: 404 Client Error: Not Found for url: https://pypi.org/simple/python-telegram-bot-upgrade/

pi@raspberrypi:~ $ pip3 install python-telegram-bot --upgrade
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting python-telegram-bot
  Downloading https://files.pythonhosted.org/packages/a6/2d/c72fc9a28144277f6170f2fcbfd3bd9427943497522b2689846596eb86cf/python_telegram_bot-12.8-py2.py3-none-any.whl (375kB)
    100% |################################| 378kB 902kB/s 
Requirement already satisfied, skipping upgrade: tornado>=5.1 in /usr/lib/python3/dist-packages (from python-telegram-bot) (5.1.1)
Requirement already satisfied, skipping upgrade: certifi in /usr/lib/python3/dist-packages (from python-telegram-bot) (2018.8.24)
Requirement already satisfied, skipping upgrade: cryptography in /usr/lib/python3/dist-packages (from python-telegram-bot) (2.6.1)
Collecting decorator>=4.4.0 (from python-telegram-bot)
  Downloading https://files.pythonhosted.org/packages/ed/1b/72a1821152d07cf1d8b6fce298aeb06a7eb90f4d6d41acec9861e7cc6df0/decorator-4.4.2-py2.py3-none-any.whl
Installing collected packages: decorator, python-telegram-bot
Successfully installed decorator-4.4.2 python-telegram-bot-12.8
pi@raspberrypi:~ $ mv python-telegram-bot/ ../python-telegram-bot/
mv: cannot stat 'python-telegram-bot/': 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ ls
Bookshelf  Documents  Music     Public     Videos  iotProject  work
Desktop    Downloads  Pictures  Templates  co2.py  pir.py
pi@raspberrypi:~ $ cd python-telegram-bot/
bash: cd: python-telegram-bot/: 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ git clone https://github/com/python-telegram-bot/python-telegram-bot--recursive
'python-telegram-bot--recursive'에 복제합니다...
fatal: unable to access 'https://github/com/python-telegram-bot/python-telegram-bot--recursive/': Could not resolve host: github
pi@raspberrypi:~ $ mv python-telegram-bot/ ../python-telegram-bot/
mv: cannot stat 'python-telegram-bot/': 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ cd python-telegram-bot/
bash: cd: python-telegram-bot/: 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ git clone https://github/com/python-telegram-bot/python-telegram-bot --recursive
'python-telegram-bot'에 복제합니다...
fatal: unable to access 'https://github/com/python-telegram-bot/python-telegram-bot/': Could not resolve host: github
pi@raspberrypi:~ $ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
'python-telegram-bot'에 복제합니다...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 15876 (delta 7), reused 4 (delta 1), pack-reused 15859
오브젝트를 받는 중: 100% (15876/15876), 6.21 MiB | 3.81 MiB/s, 완료.
델타를 알아내는 중: 100% (12519/12519), 완료.
'telegram/vendor/ptb_urllib3' 경로에 대해 'telegram/vendor/urllib3' (https://github.com/python-telegram-bot/urllib3.git) 하위 모듈 등록
'/home/pi/python-telegram-bot/telegram/vendor/ptb_urllib3'에 복제합니다...
remote: Enumerating objects: 12388, done.        
remote: Total 12388 (delta 0), reused 0 (delta 0), pack-reused 12388        
오브젝트를 받는 중: 100% (12388/12388), 3.07 MiB | 2.15 MiB/s, 완료.
델타를 알아내는 중: 100% (8699/8699), 완료.
하위 모듈 경로 'telegram/vendor/ptb_urllib3': '1954df03958b164483282330b3a58092c070bc7a' 체크아웃
pi@raspberrypi:~ $ ls
Bookshelf  Downloads  Public     co2.py      python-telegram-bot
Desktop    Music      Templates  iotProject  work
Documents  Pictures   Videos     pir.py
pi@raspberrypi:~ $ cd python-telegram-bot/examples/
pi@raspberrypi:~/python-telegram-bot/examples $ ls
LICENSE.txt           echobot.py                 nestedconversationbot.py
README.md             echobot2.py                passportbot.html
conversationbot.png   errorhandlerbot.py         passportbot.py
conversationbot.py    inlinebot.py               paymentbot.py
conversationbot2.png  inlinekeyboard.py          persistentconversationbot.py
conversationbot2.py   inlinekeyboard2.py         pollbot.py
deeplinking.py        nestedconversationbot.png  timerbot.py
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $  python3-telegram-bot/
bash: python3-telegram-bot/: 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 telegram bot
python3: can't open file 'telegram': [Errno 2] No such file or directory
pi@raspberrypi:~/python-telegram-bot/examples $ python timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 23, in <module>
    from telegram.ext import Updater, CommandHandler
ImportError: No module named telegram.ext
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 23, in <module>
    from telegram.ext import Updater, CommandHandler
ImportError: No module named telegram.ext
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ timerbot.py
bash: timerbot.py: command not found
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 109, in <module>
    main()
  File "timerbot.py", line 100, in main
    updater.start_polling()
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/ext/updater.py", line 259, in start_polling
    self.job_queue.start()
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/ext/jobqueue.py", line 446, in start
    name="Bot:{}:job_queue".format(self._dispatcher.bot.id))
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/bot.py", line 51, in decorator
    self.get_me()
  File "<decorator-gen-1>", line 2, in get_me
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/bot.py", line 67, in decorator
    result = func(*args, **kwargs)
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/bot.py", line 289, in get_me
    result = self._request.get(url, timeout=timeout)
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/utils/request.py", line 276, in get
    result = self._request_wrapper('GET', url, **urlopen_kwargs)
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/utils/request.py", line 242, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Unauthorized
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 15:45:16,556 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 15:47:14,772 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
pi@raspberrypi:~/python-telegram-bot/examples $ ^C
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 15:56:10,770 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 36
    try
      ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 36
    try:
      ^
IndentationError: expected an indented block
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 44
    except Exception as e:
         ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 44
    except Exception as e:
         ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 44
    except Exception as e:
         ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp_handler(CommandHandler("co2",co2))
                                        ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 109
    dp.adp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp.adp.add_handler(CommandHandler("co2",co2))
                                                ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp.add_handler(CommandHandler("co2",co2))
                                            ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp.add_handler(CommandHandler("co2",co2))
                                            ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling(
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 32, in <module>
    device = srial.Serial('/dev/ttyAMA0', 38400, timeout = 5)
NameError: name 'srial' is not defined
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 121, in <module>
    main()
  File "timerbot.py", line 109, in main
    dp.adp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
AttributeError: 'Dispatcher' object has no attribute 'adp'
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 16:44:28,986 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
^C2020-07-10 16:44:37,511 - telegram.ext.updater - WARNING - Exiting immediately!
pi@raspberrypi:~/python-telegram-bot/examples $ 


import logging
 22 
 23 from telegram.ext import Updater, CommandHandler
 24 
 ## import sys, serial, time

 ## device = serial.Serial('/dev/ttyAMA0', 38400, timeout = 5)
 33 # Define a few command handlers. These usually take the two arguments update and
 34 # context. Error handlers also receive the raised TelegramError object in error.
 35 def co2(update, context):
 ## try:
 37  ```             rcBuf = bytearray()
 38                 device.reset_input_buffer()
 39                 rcvBuf = device.read_until(size=12)
 40                 temp = str(rcvBuf)
 41                 a = temp.find('m')
 42                 t = temp[0:a+1]
 43                 update.message.reply_text(t)
 44         except Exception as e:
 45                 
 print("Exception read") + str(e)
 ```
 ```
 
 46 def start(update, context):
 47     update.message.reply_text('Hi! Do yeon!!!!!! /set <seconds> to set a timer')
 48 



 on different commands - answer in Telegram
103     dp.add_handler(CommandHandler("start", start))
104     dp.add_handler(CommandHandler("help", start))
105     dp.add_handler(CommandHandler("set", set_timer,
106                                   pass_args=True,
107                                   pass_job_queue=True,
108                                   pass_chat_data=True))
109     dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))

## dp.add_handler(CommandHandler("co2",co2))

111 
112     # Start the Bot
113     updater.start_polling( )


pi@raspberrypi:~ $ influxdb
bash: influxdb: command not found
pi@raspberrypi:~ $ influx
Connected to http://localhost:8086 version 1.8.0
InfluxDB shell version: 1.8.0
> create database co2
> exit
pi@raspberrypi:~ $ sudo service grafana-server start
pi@raspberrypi:~ $ pip3 install python-telegram-bot--upgrade
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting python-telegram-bot--upgrade
Could not install packages due to an EnvironmentError: 404 Client Error: Not Found for url: https://pypi.org/simple/python-telegram-bot-upgrade/

pi@raspberrypi:~ $ pip3 install python-telegram-bot --upgrade
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting python-telegram-bot
  Downloading https://files.pythonhosted.org/packages/a6/2d/c72fc9a28144277f6170f2fcbfd3bd9427943497522b2689846596eb86cf/python_telegram_bot-12.8-py2.py3-none-any.whl (375kB)
    100% |################################| 378kB 902kB/s 
Requirement already satisfied, skipping upgrade: tornado>=5.1 in /usr/lib/python3/dist-packages (from python-telegram-bot) (5.1.1)
Requirement already satisfied, skipping upgrade: certifi in /usr/lib/python3/dist-packages (from python-telegram-bot) (2018.8.24)
Requirement already satisfied, skipping upgrade: cryptography in /usr/lib/python3/dist-packages (from python-telegram-bot) (2.6.1)
Collecting decorator>=4.4.0 (from python-telegram-bot)
  Downloading https://files.pythonhosted.org/packages/ed/1b/72a1821152d07cf1d8b6fce298aeb06a7eb90f4d6d41acec9861e7cc6df0/decorator-4.4.2-py2.py3-none-any.whl
Installing collected packages: decorator, python-telegram-bot
Successfully installed decorator-4.4.2 python-telegram-bot-12.8
pi@raspberrypi:~ $ mv python-telegram-bot/ ../python-telegram-bot/
mv: cannot stat 'python-telegram-bot/': 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ ls
Bookshelf  Documents  Music     Public     Videos  iotProject  work
Desktop    Downloads  Pictures  Templates  co2.py  pir.py
pi@raspberrypi:~ $ cd python-telegram-bot/
bash: cd: python-telegram-bot/: 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ git clone https://github/com/python-telegram-bot/python-telegram-bot--recursive
'python-telegram-bot--recursive'에 복제합니다...
fatal: unable to access 'https://github/com/python-telegram-bot/python-telegram-bot--recursive/': Could not resolve host: github
pi@raspberrypi:~ $ mv python-telegram-bot/ ../python-telegram-bot/
mv: cannot stat 'python-telegram-bot/': 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ cd python-telegram-bot/
bash: cd: python-telegram-bot/: 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~ $ git clone https://github/com/python-telegram-bot/python-telegram-bot --recursive
'python-telegram-bot'에 복제합니다...
fatal: unable to access 'https://github/com/python-telegram-bot/python-telegram-bot/': Could not resolve host: github
pi@raspberrypi:~ $ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
'python-telegram-bot'에 복제합니다...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 15876 (delta 7), reused 4 (delta 1), pack-reused 15859
오브젝트를 받는 중: 100% (15876/15876), 6.21 MiB | 3.81 MiB/s, 완료.
델타를 알아내는 중: 100% (12519/12519), 완료.
'telegram/vendor/ptb_urllib3' 경로에 대해 'telegram/vendor/urllib3' (https://github.com/python-telegram-bot/urllib3.git) 하위 모듈 등록
'/home/pi/python-telegram-bot/telegram/vendor/ptb_urllib3'에 복제합니다...
remote: Enumerating objects: 12388, done.        
remote: Total 12388 (delta 0), reused 0 (delta 0), pack-reused 12388        
오브젝트를 받는 중: 100% (12388/12388), 3.07 MiB | 2.15 MiB/s, 완료.
델타를 알아내는 중: 100% (8699/8699), 완료.
하위 모듈 경로 'telegram/vendor/ptb_urllib3': '1954df03958b164483282330b3a58092c070bc7a' 체크아웃
pi@raspberrypi:~ $ ls
Bookshelf  Downloads  Public     co2.py      python-telegram-bot
Desktop    Music      Templates  iotProject  work
Documents  Pictures   Videos     pir.py
pi@raspberrypi:~ $ cd python-telegram-bot/examples/
pi@raspberrypi:~/python-telegram-bot/examples $ ls
LICENSE.txt           echobot.py                 nestedconversationbot.py
README.md             echobot2.py                passportbot.html
conversationbot.png   errorhandlerbot.py         passportbot.py
conversationbot.py    inlinebot.py               paymentbot.py
conversationbot2.png  inlinekeyboard.py          persistentconversationbot.py
conversationbot2.py   inlinekeyboard2.py         pollbot.py
deeplinking.py        nestedconversationbot.png  timerbot.py
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $  python3-telegram-bot/
bash: python3-telegram-bot/: 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 telegram bot
python3: can't open file 'telegram': [Errno 2] No such file or directory
pi@raspberrypi:~/python-telegram-bot/examples $ python timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 23, in <module>
    from telegram.ext import Updater, CommandHandler
ImportError: No module named telegram.ext
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 23, in <module>
    from telegram.ext import Updater, CommandHandler
ImportError: No module named telegram.ext
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ timerbot.py
bash: timerbot.py: command not found
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 109, in <module>
    main()
  File "timerbot.py", line 100, in main
    updater.start_polling()
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/ext/updater.py", line 259, in start_polling
    self.job_queue.start()
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/ext/jobqueue.py", line 446, in start
    name="Bot:{}:job_queue".format(self._dispatcher.bot.id))
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/bot.py", line 51, in decorator
    self.get_me()
  File "<decorator-gen-1>", line 2, in get_me
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/bot.py", line 67, in decorator
    result = func(*args, **kwargs)
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/bot.py", line 289, in get_me
    result = self._request.get(url, timeout=timeout)
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/utils/request.py", line 276, in get
    result = self._request_wrapper('GET', url, **urlopen_kwargs)
  File "/home/pi/.local/lib/python3.7/site-packages/telegram/utils/request.py", line 242, in _request_wrapper
    raise Unauthorized(message)
telegram.error.Unauthorized: Unauthorized
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 15:45:16,556 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 15:47:14,772 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
pi@raspberrypi:~/python-telegram-bot/examples $ ^C
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 15:56:10,770 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 36
    try
      ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 36
    try:
      ^
IndentationError: expected an indented block
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 44
    except Exception as e:
         ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 44
    except Exception as e:
         ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 44
    except Exception as e:
         ^
SyntaxError: invalid syntax
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp_handler(CommandHandler("co2",co2))
                                        ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 109
    dp.adp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling()
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp.adp.add_handler(CommandHandler("co2",co2))
                                                ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp.add_handler(CommandHandler("co2",co2))
                                            ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 110
    dp.add_handler(CommandHandler("co2",co2))
                                            ^
TabError: inconsistent use of tabs and spaces in indentation
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
  File "timerbot.py", line 113
    updater.start_polling(
    ^
IndentationError: unexpected indent
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 32, in <module>
    device = srial.Serial('/dev/ttyAMA0', 38400, timeout = 5)
NameError: name 'srial' is not defined
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
Traceback (most recent call last):
  File "timerbot.py", line 121, in <module>
    main()
  File "timerbot.py", line 109, in main
    dp.adp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
AttributeError: 'Dispatcher' object has no attribute 'adp'
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ python3 timerbot.py 
^C2020-07-10 16:44:28,986 - telegram.ext.updater - INFO - Received signal 2 (SIGINT), stopping...
^C2020-07-10 16:44:37,511 - telegram.ext.updater - WARNING - Exiting immediately!
pi@raspberrypi:~/python-telegram-bot/examples $ vim timerbot.py 
pi@raspberrypi:~/python-telegram-bot/examples $ cd iotProject/
bash: cd: iotProject/: 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~/python-telegram-bot/examples $ git config --global user.name "사용자이름"
pi@raspberrypi:~/python-telegram-bot/examples $ [출처] [200313 GITHUB] 내가 까먹기전에 올리는 깃허브 업로드!|작성자 dig^C
pi@raspberrypi:~/python-telegram-bot/examples $ git config--global user.name"doyeon0507"
git: 'config--global'은(는) 깃 명령이 아닙니다. 'git --help'를 참고하십시오.
pi@raspberrypi:~/python-telegram-bot/examples $ git--version
bash: git--version: command not found
pi@raspberrypi:~/python-telegram-bot/examples $ git status
현재 브랜치 master
브랜치가 'origin/master'에 맞게 업데이트된 상태입니다.

커밋하도록 정하지 않은 변경 사항:
  (무엇을 커밋할지 바꾸려면 "git add <파일>..."을 사용하십시오)
  (작업 폴더의 변경 사항을 버리려면 "git checkout -- <파일>..."을 사용하십시오)

	수정함:        timerbot.py

커밋할 변경 사항을 추가하지 않았습니다 ("git add" 및/또는 "git commit -a"를
사용하십시오)
pi@raspberrypi:~/python-telegram-bot/examples $ git add *
pi@raspberrypi:~/python-telegram-bot/examples $ git status
현재 브랜치 master
브랜치가 'origin/master'에 맞게 업데이트된 상태입니다.

커밋할 변경 사항:
  (스테이지 해제하려면 "git reset HEAD <파일>..."을 사용하십시오)

	수정함:        timerbot.py

pi@raspberrypi:~/python-telegram-bot/examples $ git commit-m"add new file"
git: 'commit-madd new file'은(는) 깃 명령이 아닙니다. 'git --help'를 참고하십시오.
pi@raspberrypi:~/python-telegram-bot/examples $ git commit -m"add new file"
경고: 커밋 메시지가 UTF-8 인코딩에 맞지 않습니다.
메시지를 수정한 다음 커밋을 수정하거나, 설정의 i18n.commitencoding
변수를 프로젝트가 사용 중인 인코딩으로 맞추십시오.
[master efea554] add new file
 1 file changed, 19 insertions(+), 7 deletions(-)
pi@raspberrypi:~/python-telegram-bot/examples $ git commit -m "add new file"
현재 브랜치 master
브랜치가 'origin/master'보다 1개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

커밋할 사항 없음, 작업 폴더 깨끗함
pi@raspberrypi:~/python-telegram-bot/examples $ git remote add origin https://github.com/github_id/github_repository 
fatal: origin 리모트가 이미 있습니다.
pi@raspberrypi:~/python-telegram-bot/examples $ git remote add origin https://github.com/doyeon0507/iotProject
fatal: origin 리모트가 이미 있습니다.
pi@raspberrypi:~/python-telegram-bot/examples $ git remote-v
git: 'remote-v'은(는) 깃 명령이 아닙니다. 'git --help'를 참고하십시오.

가장 비슷한 명령은
	remote-fd
pi@raspberrypi:~/python-telegram-bot/examples $ gitremote-v
bash: gitremote-v: command not found
pi@raspberrypi:~/python-telegram-bot/examples $ git push
Username for 'https://github.com': doyeon0507
Password for 'https://doyeon0507@github.com': 
remote: Permission to python-telegram-bot/python-telegram-bot.git denied to doyeon0507.
fatal: unable to access 'https://github.com/python-telegram-bot/python-telegram-bot/': The requested URL returned error: 403
pi@raspberrypi:~/python-telegram-bot/examples $ $ git config --global user.name
bash: $: command not found
pi@raspberrypi:~/python-telegram-bot/examples $ [출처] [Git, 깃] 처음으로 사용해서 Github, 깃허브에 업로드하는 방법, 콘솔 linux 리눅스 (init, add, status, commit, remote, push)|작성자 쥰
bash: syntax error near unexpected token `('
pi@raspberrypi:~/python-telegram-bot/examples $ 
pi@raspberrypi:~/python-telegram-bot/examples $ git config --global user.name
사용자이름
pi@raspberrypi:~/python-telegram-bot/examples $ [출처] [Git, 깃] 처음으로 사용해서 Github, 깃허브에 업로드하는 방법, 콘솔 linux 리눅스 (init, add, status, commit, remote, push)|작성자 쥰
bash: syntax error near unexpected token `('
pi@raspberrypi:~/python-telegram-bot/examples $ 
pi@raspberrypi:~/python-telegram-bot/examples $ git config--global user.name
git: 'config--global'은(는) 깃 명령이 아닙니다. 'git --help'를 참고하십시오.
pi@raspberrypi:~/python-telegram-bot/examples $ git config --globla user.name"doyeon0507"
error: unknown option `globla'
사용법: git config [<옵션>]

설정 파일 위치
    --global              공통 설정 파일을 사용합니다
    --system              시스템 설정 파일을 사용합니다
    --local               저장소 설정 파일을 사용합니다
    --worktree            use per-worktree config file
    -f, --file <파일>     지정한 설정 파일을 사용합니다
    --blob <블롭-id>      지정한 블롭 오브젝트에서 설정을 읽습니다

동작
    --get                 값을 가져옵니다: <이름> [<값-정규식>]
    --get-all             모든 값을 가져옵니다: <키> [<값-정규식>]
    --get-regexp          정규식에 대한 값을 가져옵니다: <이름-정규식> [<값-정규식>]
    --get-urlmatch        <URL>에 특정되는 값을 가져옵니다: <섹션>[.<변수>] <URL>
    --replace-all         해당하는 변수를 모두 제거합니다: <이름> <값> [<값-정규식>]
    --add                 새 변수를 추가합니다: <이름> <값>
    --unset               변수를 제거합니다: <이름> [<값-정규식>]
    --unset-all           해당하는 항목을 모두 제거합니다: <이름> [<값-정규식>]
    --rename-section      섹션의 이름을 바꿉니다: <옛-이름> <새-이름>
    --remove-section      섹션을 제거합니다: <이름>
    -l, --list            전체 목록을 표시합니다
    -e, --edit            편집기를 엽니다
    --get-color           설정한 색을 찾습니다: slot [<기본값>]
    --get-colorbool       색 설정을 찾습니다: slot [<표준출력이-TTY인지-여부>]

값 종류
    -t, --type <>         값이 해당 종류로 주어집니다
    --bool                값이 "true" 또는 "false"입니다
    --int                 값이 십진수입니다
    --bool-or-int         값이 --bool 또는 --int입니다
    --path                값이 경로(파일 또는 디렉터리 이름)입니다
    --expiry-date         값이 만료 시각입니다

기타
    -z, --null            값을 NUL 바이트로 끝냅니다
    --name-only           변수 이름만 표시합니다
    --includes            찾아볼 때 include 지시어를 고려합니다
    --show-origin         설정의 출처를 표시합니다 (파일, 표준 입력, 블롭, 명령행)
    --default <값>        --wget 옵션에서, 해당 항목이 없으면 기본값을 사용합니다

pi@raspberrypi:~/python-telegram-bot/examples $ git config --global user.name"doyeon0507"
pi@raspberrypi:~/python-telegram-bot/examples $ git config --global user.email"idoyeon0507@gmail.com"
pi@raspberrypi:~/python-telegram-bot/examples $ git config color.ui true
pi@raspberrypi:~/python-telegram-bot/examples $ git init
/home/pi/python-telegram-bot/examples/.git/ 안의 빈 깃 저장소를 다시 초기화했습니다
pi@raspberrypi:~/python-telegram-bot/examples $ git add *c
fatal: '*c' 경로명세가 어떤 파일과도 일치하지 않습니다
pi@raspberrypi:~/python-telegram-bot/examples $ git add
아무 것도 지정하지 않았으므로 아무 것도 추가하지 않습니다.
'git add .' 명령을 실행하려고 한 것 아니었습니까?
pi@raspberrypi:~/python-telegram-bot/examples $ git add *python3 timer.py
fatal: '*python3' 경로명세가 어떤 파일과도 일치하지 않습니다
pi@raspberrypi:~/python-telegram-bot/examples $ git add *
pi@raspberrypi:~/python-telegram-bot/examples $ git status
현재 브랜치 master

아직 커밋이 없습니다

커밋할 변경 사항:
  (스테이지 해제하려면 "git rm --cached <파일>..."을 사용하십시오)

	새 파일:       LICENSE.txt
	새 파일:       README.md
	새 파일:       conversationbot.png
	새 파일:       conversationbot.py
	새 파일:       conversationbot2.png
	새 파일:       conversationbot2.py
	새 파일:       deeplinking.py
	새 파일:       echobot.py
	새 파일:       echobot2.py
	새 파일:       errorhandlerbot.py
	새 파일:       inlinebot.py
	새 파일:       inlinekeyboard.py
	새 파일:       inlinekeyboard2.py
	새 파일:       nestedconversationbot.png
	새 파일:       nestedconversationbot.py
	새 파일:       passportbot.html
	새 파일:       passportbot.py
	새 파일:       paymentbot.py
	새 파일:       persistentconversationbot.py
	새 파일:       pollbot.py
	새 파일:       timerbot.py

pi@raspberrypi:~/python-telegram-bot/examples $ git commit -m
error: switch `m' requires a value
pi@raspberrypi:~/python-telegram-bot/examples $ git commit -m "project update"
경고: 커밋 메시지가 UTF-8 인코딩에 맞지 않습니다.
메시지를 수정한 다음 커밋을 수정하거나, 설정의 i18n.commitencoding
변수를 프로젝트가 사용 중인 인코딩으로 맞추십시오.
[master (최상위-커밋) a0ff42b] project update
 21 files changed, 2206 insertions(+)
 create mode 100644 LICENSE.txt
 create mode 100644 README.md
 create mode 100644 conversationbot.png
 create mode 100644 conversationbot.py
 create mode 100644 conversationbot2.png
 create mode 100644 conversationbot2.py
 create mode 100644 deeplinking.py
 create mode 100644 echobot.py
 create mode 100644 echobot2.py
 create mode 100644 errorhandlerbot.py
 create mode 100644 inlinebot.py
 create mode 100644 inlinekeyboard.py
 create mode 100644 inlinekeyboard2.py
 create mode 100644 nestedconversationbot.png
 create mode 100644 nestedconversationbot.py
 create mode 100644 passportbot.html
 create mode 100644 passportbot.py
 create mode 100644 paymentbot.py
 create mode 100644 persistentconversationbot.py
 create mode 100644 pollbot.py
 create mode 100644 timerbot.py
pi@raspberrypi:~/python-telegram-bot/examples $ git remote add origin https://github.com/doyeon0507/iotProject
pi@raspberrypi:~/python-telegram-bot/examples $ git push -u origin master
Username for 'https://github.com': doyeon0507
Password for 'https://doyeon0507@github.com': 
To https://github.com/doyeon0507/iotProject
 ! [rejected]        master -> master (fetch first)
error: 레퍼런스를 'https://github.com/doyeon0507/iotProject'에 푸시하는데 실패했습니다
힌트: 리모트에 로컬에 없는 사항이 들어 있으므로 업데이트가
힌트: 거부되었습니다. 이 상황은 보통 또 다른 저장소에서 같은
힌트: 저장소로 푸시할 때 발생합니다.  푸시하기 전에
힌트: ('git pull ...' 등 명령으로) 리모트 변경 사항을 먼저
힌트: 포함해야 합니다.
힌트: 자세한 정보는 'git push --help'의 "Note about fast-forwards' 부분을
힌트: 참고하십시오.
pi@raspberrypi:~/python-telegram-bot/examples $ git push
fatal: 현재 브랜치 master에 업스트림 브랜치가 없습니다.
현재 브랜치를 푸시하고 해당 리모트를 업스트림으로 지정하려면
다음과 같이 하십시오.

    git push --set-upstream origin master

pi@raspberrypi:~/python-telegram-bot/examples $ git add python
fatal: 'python' 경로명세가 어떤 파일과도 일치하지 않습니다
pi@raspberrypi:~/python-telegram-bot/examples $ gir status
bash: gir: command not found
pi@raspberrypi:~/python-telegram-bot/examples $ cd ~
pi@raspberrypi:~ $ ls
Bookshelf  Documents  Music     Public     Videos  iotProject  python-telegram-bot
Desktop    Downloads  Pictures  Templates  co2.py  pir.py      work
pi@raspberrypi:~ $ cd iotProject/
pi@raspberrypi:~/iotProject $ ls
README.md  co2.py  grafana_6.5.1_armhf.deb  pir.py  test.c
pi@raspberrypi:~/iotProject $ vim co2.py 
pi@raspberrypi:~/iotProject $ git add .
pi@raspberrypi:~/iotProject $ git commit -m upload
경고: 커밋 메시지가 UTF-8 인코딩에 맞지 않습니다.
메시지를 수정한 다음 커밋을 수정하거나, 설정의 i18n.commitencoding
변수를 프로젝트가 사용 중인 인코딩으로 맞추십시오.
[master 21b8f61] upload
 2 files changed, 26 insertions(+)
 create mode 100644 co2.py
 create mode 100644 grafana_6.5.1_armhf.deb
pi@raspberrypi:~/iotProject $ git push
Username for 'https://github.com': doyeon0507
Password for 'https://doyeon0507@github.com': 
To https://github.com/doyeon0507/iotProject
 ! [rejected]        master -> master (fetch first)
error: 레퍼런스를 'https://github.com/doyeon0507/iotProject'에 푸시하는데 실패했습니다
힌트: 리모트에 로컬에 없는 사항이 들어 있으므로 업데이트가
힌트: 거부되었습니다. 이 상황은 보통 또 다른 저장소에서 같은
힌트: 저장소로 푸시할 때 발생합니다.  푸시하기 전에
힌트: ('git pull ...' 등 명령으로) 리모트 변경 사항을 먼저
힌트: 포함해야 합니다.
힌트: 자세한 정보는 'git push --help'의 "Note about fast-forwards' 부분을
힌트: 참고하십시오.
pi@raspberrypi:~/iotProject $ git pull
remote: Enumerating objects: 38, done.
remote: Counting objects: 100% (38/38), done.
remote: Compressing objects: 100% (36/36), done.
remote: Total 36 (delta 11), reused 0 (delta 0), pack-reused 0
오브젝트 묶음 푸는 중: 100% (36/36), 완료.
https://github.com/doyeon0507/iotProject URL에서
   39f6201..498942b  master     -> origin/master
경고: 커밋 메시지가 UTF-8 인코딩에 맞지 않습니다.
메시지를 수정한 다음 커밋을 수정하거나, 설정의 i18n.commitencoding
변수를 프로젝트가 사용 중인 인코딩으로 맞추십시오.
Merge made by the 'recursive' strategy.
 README.md | 400 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 389 insertions(+), 11 deletions(-)
pi@raspberrypi:~/iotProject $ git add .
pi@raspberrypi:~/iotProject $ git commit -m upload
현재 브랜치 master
브랜치가 'origin/master'보다 2개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

커밋할 사항 없음, 작업 폴더 깨끗함
pi@raspberrypi:~/iotProject $ git push
Username for 'https://github.com': doyeon0507
Password for 'https://doyeon0507@github.com': 
오브젝트 나열하는 중: 8, 완료.
오브젝트 개수 세는 중: 100% (8/8), 완료.
Delta compression using up to 4 threads
오브젝트 압축하는 중: 100% (6/6), 완료.
오브젝트 쓰는 중: 100% (6/6), 31.61 MiB | 4.22 MiB/s, 완료.
Total 6 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/doyeon0507/iotProject
   498942b..0354953  master -> master
pi@raspberrypi:~/iotProject $ cp /home/pi/python-telegram-bot/examples/timerbot.py 
cp: missing destination file operand after '/home/pi/python-telegram-bot/examples/timerbot.py'
Try 'cp --help' for more information.
pi@raspberrypi:~/iotProject $ cp timerbot.py /home/pi/python-telegram-bot/examples/timerbot.py 
cp: cannot stat 'timerbot.py': 그런 파일이나 디렉터리가 없습니다
pi@raspberrypi:~/iotProject $ cp /home/pi/python-telegram-bot/examples/timerbot.py .
pi@raspberrypi:~/iotProject $ ls
README.md  co2.py  grafana_6.5.1_armhf.deb  pir.py  test.c  timerbot.py
pi@raspberrypi:~/iotProject $ git add .
pi@raspberrypi:~/iotProject $ git commit -m upload
경고: 커밋 메시지가 UTF-8 인코딩에 맞지 않습니다.
메시지를 수정한 다음 커밋을 수정하거나, 설정의 i18n.commitencoding
변수를 프로젝트가 사용 중인 인코딩으로 맞추십시오.
[master 16a3f93] upload
 1 file changed, 121 insertions(+)
 create mode 100644 timerbot.py
pi@raspberrypi:~/iotProject $ git push
Username for 'https://github.com': doyeon0507
Password for 'https://doyeon0507@github.com': 
오브젝트 나열하는 중: 4, 완료.
오브젝트 개수 세는 중: 100% (4/4), 완료.
Delta compression using up to 4 threads
오브젝트 압축하는 중: 100% (3/3), 완료.
오브젝트 쓰는 중: 100% (3/3), 1.91 KiB | 652.00 KiB/s, 완료.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/doyeon0507/iotProject
   0354953..16a3f93  master -> master
pi@raspberrypi:~/iotProject $ 

```
