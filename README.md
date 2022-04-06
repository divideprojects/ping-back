# Tools

A simple API made to ping the url specified in url parameters

## Usage

Base domain: https://ping-back.divkix.me/

There are just 2 URL Parameters that are required:
 - link: the url to ping
 - method: the method to use to ping the link, default is GET, but you can use either GET or POST

A simple example looks like:

https://ping-back.divkix.me/pingback?link=https://divkix.me?method=GET

This will just ping the domain https://divkix.me url and return a 200 status code if the url is reachable.
