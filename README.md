**checkURL** Detects evil url using IDN Homograph Attack
===================

--------------
> **Install:**
--------------

> - #git clone https://github.com/UndeadSec/checkURL.git
> - #cd checkURL
> - #python checkURL.py

----------
Usage
----------

```
# cd checkURL
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
----------
Requirements
----------

* python3


----------
Screenshot
----------

![Shot](https://github.com/UndeadSec/checkURL/blob/master/screenshot.png)


