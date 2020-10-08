# 环境配置

## 环境介绍

本文使用了基于 `Anaconda3` 的 `Python 3.8.2` 作为编译环境，假定读者已安装该环境。

本文将会指引读者安装以下包：

- Selenium 
- 浏览器Driver

## Selenium 安装

在 `Anaconda3` 运行：

```
conda install selenium
```

## 浏览器Driver

** 注意：不同的浏览器安装不同的 Driver **

根据自己的浏览器，以及版本，下载对应的 Driver。

- (Chrome)[https://chromedriver.storage.googleapis.com/index.html] 
- (Edge)[https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/]

下载完成后解压缩，将 '*driver.exe' 放在任意文件夹下，然后将该目录配置至程序中。

### 测试

配置环境完成后，运行 `code1_env_test.py` 测试，效果为打开 Bing 搜索 Python3。

### 问题

- 浏览器不能打开 -> Selenium 配置问题
- 浏览器打开不能打开网页 -> Driver 配置问题