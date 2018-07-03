# pypi-gaode-api
pypi tools for gaode api, https://lbs.amap.com/api/webservice/summary

## Install

```shell
> pip install gaode-api-cli

> gaode-api-intersection

Usage:       gaode-api-intersection
             gaode-api-intersection searchByFile
             gaode-api-intersection searchOne
```

## Intersection Usage
> Searching for intersection information from Gaode [Search API](https://lbs.amap.com/api/webservice/guide/api/search/?)

### searchOne

```shell
> gaode-api-intersection searchOne 天目山路

> gaode-api-intersection searchOne 天目山路 hanzhou

> gaode-api-intersection searchOne 天安门 hanzhou
```

### searchByFile
> To search intersections of a batch data.

1. edit `input.txt` in current dir.

```
天目山路高教路口
文一西路高教路口
...
```

2. execute command like below.

```shell
# outputs going into output.csv
> gaode-api-intersection searchByFile input.txt

# outputs going into output1.csv
> gaode-api-intersection searchByFile input.txt output1.csv
```

