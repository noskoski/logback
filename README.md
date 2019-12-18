# logback

Prints lines from backward in the corresponding period 

usage: logback.py [options] /path/logfile.log

Parse log file lines of the last X minutes ( -t X )

positional arguments:
  logfile               Log file to read

optional arguments:
  -h, --help            show this help message and exit
  -o ONLY [ONLY ...], --only ONLY [ONLY ...]
                        print only match strings
  -t TIME, --time TIME  match lines in this time interval (in minutes)
  --version             show program's version number and exit
