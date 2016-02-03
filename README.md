# Pi Speedtest

https://www.reddit.com/r/technology/comments/43fi39/i_set_up_my_raspberry_pi_to_automatically_tweet/


## Setup

Clone repo
```
cd /home/pi
git clone https://github.com/kevana/pi-speedtest.git
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
crontab -e
# Add the following line:
*/15 * * * *  cd /home/pi/pi-speedtest && /home/pi/pi-speedtest/speedtest.py
# Save and exit the editor
```
