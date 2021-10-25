# Python Selenium Note

<img src="https://img.shields.io/badge/license-MIT-green.svg" />

基于 Python 语言的 Selenium 笔记。

## 简介

> Selenium 是一系列工具和库的综合项目，这些工具和库支持 web 浏览器的自动化。

在21世纪，信息技术蓬勃发展。在一些涉及网页的重复操作，我们可以用一些技术实现自动化。Selenium 直接运行在浏览器中，就像真正的用户在操作一样。

本文简单介绍了一些 Selenium 的使用技巧，并给了一个示例代码。更多内容可以前往[Selenium 浏览器自动化项目文档](https://www.selenium.dev/zh-cn/documentation/)了解。

## 环境配置

### 环境介绍

本文使用了基于 `Anaconda` 的 `Python 3.8.2` 作为编译环境，假定读者已安装该环境。

本节将会指引读者安装以下程序支撑我们编写程序的运行：

- Selenium
- 浏览器Driver

### Selenium 安装

在 `Anaconda3` 运行：

```
conda install selenium
```

### 浏览器Driver

** 注意：不同的浏览器安装不同的 Driver **

根据自己的浏览器，以及版本，下载对应的 Driver。

- (Chrome)[https://chromedriver.storage.googleapis.com/index.html]
- (Edge)[https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/]

下载完成后解压缩，将 `*driver.exe` 放在任意文件夹下，然后将该目录配置至程序中。

### 环境测试

配置环境完成后，运行 `code1_env_test.py` 测试，效果为打开 Bing 搜索 Python3。

可能的问题如下：

- 浏览器不能打开 -> Selenium 配置问题
- 浏览器打开不能打开网页 -> Driver 配置问题

## Selenium 介绍

### 浏览器

启动浏览器（详见[代码1](../code/code1_env_test.py)）
```
driver = webdriver.Edge()
```

打开网页
```
driver.get("https://selenium.dev")
```

获取当前网页信息
```
driver.current_url
driver.title
```

网页刷新
```
driver.refresh()
```

切换窗口或标签页（[查看详情](https://www.selenium.dev/zh-cn/documentation/webdriver/browser_manipulation/#%E5%88%87%E6%8D%A2%E7%AA%97%E5%8F%A3%E6%88%96%E6%A0%87%E7%AD%BE%E9%A1%B5)）
```
all_handles = driver.window_handles
for handle in all_handles:
    if handle != main_windows:
        driver.switch_to.window(handle)
driver.close()
driver.switch_to_window(main_windows)
```

### 定位

#### 定位的建议

- 如果 HTML 的 `id` 是唯一的、可用的，那么它就是在页面上定位元素的首选方法。
- 如果 id 不合适使用，那么请选择 `xpath`。
- 有时需要定位一组元素，有时也需要按文字搜索定位元素。
- 定位并操作有时需要时间，因此要使用 `time.sleep()` 方法。
- 定位并不总是成功，因此需要做好异常处理。

#### 元素与元素们的定位

定位 id 元素示例
```
driver.find_element(By.ID, 'cheese')
```

定位 xpath(s) 元素示例
```
driver.find_elements(By.XPATH, '//span[contains(text(),"cheese")]')[0]
```

## 另见

本文仅是笔记，读者可以参见[Selenium 浏览器自动化项目文档](https://www.selenium.dev/zh-cn/documentation/)获取更详细的资料。

## 许可证

[MIT](LICENSE)
