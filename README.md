<h1 align="center">CheckURL</h1>
<p align="center">
  Detect evil urls that uses IDN Homograph Attack.
</p>

### MAINTAINERS
* **Vandré Augusto** | 
Twitter: <a href="https://twitter.com/dr1nKoRdi3">@dr1nKoRdi3</a>
Github: <a href="https://github.com/dr1nk0rdi3">@dr1nK0Rdi3</a>

## VIDEO DEMO
<p align="center">
<a href="https://youtu.be/joQxGtuyfZU">
  <img src="https://raw.githubusercontent.com/UndeadSec/checkURL/master/video.png" />
</a></p>

### CLONE
```
# git clone https://github.com/UndeadSec/checkURL.git
```

### RUNNING
```
# cd checkURL
```

```
# python3 checkURL.py --help
usage: checkURL.py [-h] [--url URL | --url-list URL_list] [--check-url]

Check IDN Homograph Attack - UndeadSec

optional arguments:
  -h, --help           show this help message and exit
  --url URL            Enter to check if it is Evil URL
  --url-list URL_list  Specify a file with a list of Evil URL
  --check-url          Check socket URL

Examples:
    python3 checkURL.py --url google.com
    python3 checkURL.py --url google.com --check-url
    python3 checkURL.py --url-list urls.txt
    python3 checkURL.py --url-list urls.txt --check-url

Telegram: https://t.me/UndeadSec
```
### PREREQUISITES

* python 3.x 

## TESTED ON
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - ROLLING EDITION**

### SCREENSHOT
![Shot](https://github.com/UndeadSec/checkURL/blob/master/screenshot.png)
