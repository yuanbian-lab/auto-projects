# -*- coding=utf-8 -*-
from lxml import html

html_string = """
<div>
这是老六写的笔记,
   <span>中间夹着废话,</span>
   分享老六的爬虫心得,
   <span>有很多废话</span>
</div>
"""

dom = html.fromstring(html_string)
el = dom.cssselect("div")[0]
print(el.text_content())


"""
<!-- html代码编辑区域 -->
<style>
   b, span {
     display: none;
   }
</style>


<div>
   <p>地址:某某路<b>100废话</b>25号</p>
   <p>tel:<span>88废话</span>99999999<b>废话</b>
   </p>
</div>
"""
"""
style>
   #div1 {
     position: relative;
     width: 300px;
     height: 300px;
     border: 3px solid #f00;    
   }
   #div2 {
       position: absolute;
       left: 100px;
       height: 100px;
       width: 100px;
       border: 3px solid #0ff;
   }
   #div3 {
       position: absolute;
       top: 10px;
       left: 10px;
       border: 3px solid #f0f;
   }
</style>
<div id="div1">
   <div id="div2">方块2</div>
   <div id="div3">方块3</div>
</div>
"""