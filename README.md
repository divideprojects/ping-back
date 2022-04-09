# ping-back

A simple API made to ping the url specified in url parameters

## Deploy your own

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FDivideProjects%2Fping-back&demo-title=Ping%20Back&demo-description=A%20simple%20ping-back%20website%20made%20using%20fastapi.&demo-url=https%3A%2F%2Fping-back.divideprojects.com?utm_source=divideprojects&utm_campaign=oss)

## Usage

Base domain: https://ping-back.divideprojects.com/

There are just 2 URL Parameters that are required:
 - link: the url to ping
 - method: the method to use to ping the link, default is GET, but you can use either GET or POST

A simple example looks like:

https://ping-back.divideprojects.com/pingback?link=https://divideprojects.com?method=GET

This will just ping the domain https://divideprojects.com url and return a 200 status code if the url is reachable.


[![Sponsor](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)](https://vercel.com/?utm_source=divideprojects&utm_campaign=oss)
