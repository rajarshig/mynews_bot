# mynews_bot
By Rajarshi Ghosh <rajarshig89@gmail.com>

Introduction
------------
mynews_bot is a python command line application. It's objective is to collect news from various sources (using corresponding RSS feeds) & provide a terminal interface for viewing the collected data.

Installation
------------
```
pip install mynews-bot
```


Usage
------------
```
usage: mynews-bot [-h] [-s SOURCE] [-t TOP] [-v]

Get news items from multiple news sources

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Name of the news source. Available options are: TOI,
                        NYT, IT, GNEWS, QUINT, REDDIT, BBC, BUZZFEED,
                        ALJAZEERA, YAHOONEWS, CNN, GUARDIAN, WASHINGTON_POST,
                        CNBC, REUTERS, INDEPENDENT, BUSINESS_STANDARD
  -t TOP, --top TOP     Count of news items to show from top order. Default:
                        10
  -v, --version         show program's version number and exit
```

Example
------------
- Get news for source BBC
```
mynews_bot -s BBC
```
- Get top 10 news for source CNBC
```
mynews_bot -s CNBC -t 10
``` 
- Get news from all sources
```
mynews_bot -t 2
```
## News Sources
- Times Of India
- New York Times 
- India Today
- Google News
- Quint
- Reddit
- BBC
- Buzzfeed
- AlJazeera
- Yahoo News
- CNN
- Guardian
- Washington Post
- CNBC
- Reuters
- Independent
- Business Standard
