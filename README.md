# Pi Speedtest

https://www.reddit.com/r/technology/comments/43fi39/i_set_up_my_raspberry_pi_to_automatically_tweet/


## Setup

Clone repo
```
cd /home/pi
git clone ...
cd pi-speedtest

touch /var/www/speedtest/data.csv
```

Download [speedtest-cli](https://github.com/sivel/speedtest-cli)
```
mkdir -p /home/pi/speedtest-cli
cd /home/pi/speedtest-cli
wget -O speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest_cli.py
chmod +x speedtest-cli
```

Add a crontab entry
```
TODO
```