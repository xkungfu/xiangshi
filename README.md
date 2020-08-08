# 相识(Xiangshi)

#### 中文文本相似度计算器
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi)](https://img.shields.io/pypi/v/xiangshi)
[![Downloads](https://pepy.tech/badge/xiangshi)](https://pepy.tech/project/xiangshi)
[![Pypi license](https://img.shields.io/github/license/kiwirafe/xiangshi)](https://img.shields.io/github/license/kiwirafe/xiangshi)
[![Language](https://img.shields.io/github/languages/top/kiwirafe/xiangshi)](https://github.com/kiwirafe/xiangshi)

相识是一款专门为中文打造的文本相似度计算器。这是唯一也是最好的中文文本相似度计算器

相识的优势有：
  - 支持多个文本相似度比较
  - 使用余弦计算
  - 使用Python语言
  - 可以TFIDF过滤
  - 可以单独计算TF和IDF
  - 支持List和File两种类型
  - 高效、迅速
  - 安装容易

### 下载与安装
```sh
$ pip3 install jeiba
$ pip3 install xiangshi
```
 - [Jeiba](https://github.com/fxsjy/jieba)是一个中文分词软件
 - [pip3也可以是pip根据个人环境选择](https://stackoverflow.com/questions/40832533/pip-or-pip3-to-install-packages-for-python-3) 

#### 版本1.2.0来了！
  - 增加文本余弦相似度计算
   - 可以使用cal
  - 增加SortDict Function

### 使用方法
##### 计算文本相似度
```
import xiangshi as xs
xs.cal(Input1, Input2, UseLog=True, InputTarget1=None, InputTarget2=None):
```
 - 计算文本相似度时自动由TFIDF过滤
 - Input1 - 第一个输入值，可以是文件的地址或是一个列表
 - Input2 - 第二个输入值，可以是文件的地址或是一个列表
 - UseLog - 是否使用L，默认是使用，不使用的话设定为True
 - InputTarget1 - 文件类型不需要，使用None就可以了（不填也行），如果是列表一定要填，UseLog也一定要填
 - InputTarget2 - 文件类型不需要，使用None就可以了（不填也行），如果是列表一定要填，UseLog也一定要填

##### 计算TF，IDF，TFIDF
```
import xiangshi as xs
xs.GetTF(Input)
xs.GetIDF(Input, UseLog， InputTarget)
xs.GetTFIDF（Input, UseLog， InputTarget)
```
  - Input - 输入值，可以是文件的地址或是一个列表
  - UseLog - 是否使用L，默认是使用，不使用的话设定为True
  - InputTarget - 文件类型不需要，使用None就可以了（不填也行），如果是列表一定要填，UseLog也一定要填

### 版本历史
  - v0.0.1: 初始版本
    - 只有TFIDF计算
    - 计算量较大
  - v0.0.2: 版本修改
  - v0.0.3: 病毒修复
  - v0.0.4: 细节修改
  - v0.0.5: TF，IDF和TFIDF彻底脱节
  - v0.1.0: Github上Alpha版本
    - 去掉多余的循环
    - 利用Python的库函数
    - 计算时间增加30倍
  - v0.1.1: Pip准备
  - v0.1.2: Pip发布
  - v0.1.3: Pip上增加README
  - v0.1.4: README增加下载和使用说明
  - v0.1.5: Pip上修改，让用户可以直接使用各种函数
  - v0.1.6: 病毒修复
  - v1.0.0: 支持文本相似度计算
### MIT License
Copyright (c) [2020] [相识]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

