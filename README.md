# Tools

A simple API made to ping the url specified in url parameters

## Usage

Base domain: https://ping-back.divkix.me/

There are just 2 URL Parameters that are required:
 - remote_url: the url to ping
 - method: the method to use to ping the url, by default it is GET, you can use either GET or POST

A simple example looks like:

https://ping-back.divkix.me/ping-back?url=https://divkix.me

This will just ping the domain https://divkix.me url and return a 200 status code if the url is reachable.