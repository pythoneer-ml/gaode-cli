# pypi-gaode-api
pypi tools for gaode api, https://lbs.amap.com/api/webservice/summary

## Install

```
pip install gaode-api-cli
```

## Intersection

路口信息检索

### searchOne

```
gaode-api-intersection searchOne 天目山路

gaode-api-intersection searchOne 天目山路 hanzhou

gaode-api-intersection searchOne 天安门 hanzhou
```

### searchByFile

准备 input.txt 放在当前目录下

```
天目山路高教路口
文一西路高教路口
...
```

执行

```shell
# 生成 output.csv
gaode-api-intersection searchByFile input.txt

# 生成 output.csv
gaode-api-intersection searchByFile input.txt output1.csv
```



