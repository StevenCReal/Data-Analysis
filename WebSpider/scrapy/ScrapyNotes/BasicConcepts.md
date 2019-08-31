# Basic concepts

## Command line tool
### Creating projects
```
[shell] scrapy startproject myproject [project_dir]
```
If project_dir wasn’t specified, project_dir will be the same as myproject.
### Controlling projects
- get info about each command and see all available commands by running:
```
[shell] scrapy <command> -h
```
```
[shell] scrapy -h
```
- to create a new spider:
```
[shell] scrapy genspider mydomain mydomain.com
```
#### Global commands
Global commands work <u>without an active Scrapy project</u>, though they may behave slightly different when running from inside a project (as they would use the project overridden settings).

- [startproject](startproject)  
- [genspider](genspider)  
- [settings](settings)  
- [runspider](runspider)  
- [hell](hell)  
- [fetch](fetch)  
- [view](view)  
- [version](version)

#### Project-only commands
Project-only commands only work from <u>inside a Scrapy project</u>.

- [crawl](crawl)  
- [check](check)  
- [list](list)  
- [edit](edit)  
- [parse](parse)  
- [bench](bench)

--------------------------

## Spider
Spiders are classes which define how a certain site (or a group of sites) will be scraped, including:  
- how to perform the crawl (i.e. follow links)  
- how to extract structured data from their pages (i.e. scraping items).
### scrapy.Spider