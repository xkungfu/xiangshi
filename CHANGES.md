### 版本历史
  - v0.1.0: 初始版本
    - 只有TFIDF计算
    - 计算量较大
    - 计算时间较大、长
  - v0.1.1: 版本修改
  - v0.1.2: 病毒修复
  - v0.1.3: 细节修改
  - v0.1.4: TF，IDF和TFIDF彻底脱节，分别为独立的函数
  - v0.2.0: Github上Alpha版本
    - 去掉多余的循环
    - 利用Python的库函数
    - 计算时间增加30倍
  - v0.2.1: Pip准备
  - v0.2.2: 病毒修复
  - v0.2.3: Github上正式发布
  - v0.3.0: Pip发布
  - v0.3.1: Pip上增加README
  - v0.3.2: README增加下载和使用说明
  - v0.3.3: Pip上修改，让用户可以直接使用所有的函数
  - v1.0.0: 支持文本相似度计算
    - 支持余弦相似度
    - 余弦相似度： 是通过计算两个向量的夹角余弦值来评估他们的相似度
    - 使用 - xs.cossim(Input1, Input2)
  - v1.0.1: 
    - 不再使用set，因为使用的话两个文本的顺序就会不同，导致结果差别巨大
    - 保持一开始Dict的顺序，这样子计算中就没有随机性了
  - v1.0.2: 增加Decimal精确计算
  - v1.0.3: 增加StopText，之前缺少
  - v1.0.4: 函数自动变成Pip函数
  - v1.1.0: 增加dict2file函数
  - v1.2.0:
    - 增加相识极速版，只支持余弦相似度和File类型，但速度增加10%
  - v1.2.1: README更新，更多注释
  - v1.2.2: 取消Decimal计算，与保留区别不大
  - v1.3.0:
    - Gitee(中国版的Github)上发布，让国内用户更加方便的使用
    - 余弦和TFIDF的Input变成Class的变量，使调用函数时更加方便
  - v1.3.1: 病毒修复
  - v1.3.2: 支持清华镜像，让国内用户更加方便的下载
  - v1.3.3(v2.0.0 Beta): Github和Gitee上发布v2.0.0 Beta
  - v2.0.0: 支持Simhash和Minhash
    - 增加Simhash算法
      - Simhash算法适用于大文本分析，建议大于500字使用
      - 使用 - xs.simhash(Input1, Input2)
    - 增加Minhash算法
      - Minhash算法与Simhash类似。
      -  使用 - xs.minhash(Input1, Input2)
  - v2.0.1: 停止支持xs.cal(Input1, Input2)
  - v2.0.2: Github上更新2.0.0版本
  - v2.0.3: 增加README(Eng).md
  - v2.1.0：Pip上更新真正的2.0.0版本，之前发布了错误版本
  - v2.1.1: 支持只有TF的加权
  - v2.1.2：Minhash加权选定用Quantization-Based来实现
  - v2.1.3: Minhash由set转为dict，与v1.0.1原因一样
  - v2.2.0：
    - Minhash加权成功
    - 使用Quantization-Based算法
    - 具体用Multiset实现
  - v2.2.1: 增加CHANGES.md
  - v2.2.2: README更新，更多注释
  - v2.3.0: 使用Logging，所有运算记录均保存在xiangshi.log
  - v2.3.1: 发现Stoptext无法使用
  - v2.3.2: Pip加入Stoptext
  - v2.3.3: Stoptext由所相识文件里调用，而不是从运行地点里调用
  - v2.4.0：
    - 相识极速版并入相识
    - 减少时间，20~30s减少至10~15s
    - 完全支持列表