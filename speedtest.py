#!/usr/bin/python

# From https://www.reddit.com/r/technology/comments/43fi39/i_set_up_my_raspberry_pi_to_automatically_tweet/

import os
import sys
import csv
import datetime
import time
 
data_file = "/var/www/speedtest/data.csv"
st_cli = "/home/pi/speedtest-cli/speedtest-cli"
#data_file = "./data.csv"
#st_cli = "./speedtest-cli"

def test():
 
    #run speedtest-cli
    print("running test")
    a = os.popen("python " + st_cli + " --simple").read()
    #a = "Ping: 33.044 ms\nDownload: 6.30 Mbit/s\nUpload: 9.09 Mbit/s"
    print("ran")
    #split the 3 line result (ping,down,up)
    lines = a.split('\n')
    print(a)
    date = datetime.datetime.now().isoformat()
    #if speedtest could not connect set the speeds to 0
    if "Cannot" in a:
        ping = 0
        down = 0
        up = 0
    #extract the values for ping down and up values
    else:
        ping = lines[0][6:11]
        down = lines[1][10:14]
        up = lines[2][8:12]
    print(date, ping, down, up)
    #save the data to file for local network plotting
    with open(data_file, "a") as out_file:
        writer = csv.writer(out_file)
        writer.writerow((date, ping, down, up))

    return
       
if __name__ == '__main__':
    test()
    print 'completed'
