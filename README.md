简体中文版 [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)
========================

在完成飞花令的过程中，使用了 [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) 这个库的数据，但是其数据使用了繁体不符合项目需求，所以手动写脚本进行了转换。

繁简体转换使用的数据位于 `./zhtools/zh_wiki.py`, 有更准确的库的话可以替换此文件然后重新运行 `convert.py` 即可。