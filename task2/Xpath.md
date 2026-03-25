# XPATH

## 一. XPATH是什么？

1. 解析XML的一种语言（HTML其实是XML的子集），广泛用于解析HTML数据
2. 几乎所有语言都能便用XPath，比如Java和C语言
3. 除了XPath还有其他手段用于XML解析，比如：BeautifulSoup、lxml、DOM、SAX、JSDOM、DOM4J、minlxml等

在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。

* 基本值（或称原子值，Atomic value）基本值是无父或无子的节点。
* 项目（Item）项目是基本值或者节点。
* 父（Parent）每个元素以及属性都有一个父。

    在下面的例子中，book 元素是 title、author、year 以及 price 元素的父：
```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
* 子（Children）元素节点可有零个、一个或多个子。

    在下面的例子中，title、author、year 以及 price 元素都是 book 元素的子：
```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
* 同胞（Sibling）
拥有相同的父的节点

    在下面的例子中，title、author、year 以及 price 元素都是同胞
```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
* 先辈（Ancestor）
某节点的父、父的父，等等。

    在下面的例子中，title 元素的先辈是 book 元素和 bookstore 元素：
```xml
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```
* 后代（Descendant）
某个节点的子，子的子，等等。

    在下面的例子中，bookstore 的后代是 book、title、author、year 以及 price 元素：
```xml
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```

## 二. XPATH的语法

* 层级：/直接子集，//跳级
* 属性：@属性名
* 函数：text()、contains()、starts-with()、ends-with()等
* 谓语：[]，可以用来过滤节点，比如：//div[@class='example']表示选择所有class属性为example的div元素
```xml
<?xml version="1.0" encoding="UTF-8"?>
 
<bookstore>
 
<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>
 
<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>
 
</bookstore>
```
XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。 下面列出了最有用的路径表达式：
| 路径表达式 | 描述 |
|:------------:|:--------:|
| nodename | 选取此节点的所有子节点 |
|/| 选取根节点 |
|//| 选取文档中的节点，不考虑它们的位置 |
|. | 选取当前节点 |
|..| 选取当前节点的父节点 |
|@| 选取属性 |

示例
| 路径表达式 | 结果 |
|:------------:|:--------:|
|bookstore| 选取所有名为bookstore的节点 |
| /bookstore | 	选取根元素 bookstore。注释：假如路径起始于正斜( / )，则此路径始终代表到某元素的绝对路径！ |
| bookstore/book | 选取属于 bookstore 的子元素的所有 book 元素。 |
| //book | 选取所有 book 子元素，而不管它们在文档中的位置。 |
|bookstore//book|选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
|//@lang|选取所有名为 lang 的属性。|

### 谓语

谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：
| 路径表达式 | 结果 |
|:------------:|:--------:|
|/bookstore/book[1]|选取属于 bookstore 的第一个 book 元素。|
|/bookstore/book[last()]|选取属于 bookstore 的最后一个 book 元素。|
|/bookstore/book[last()-1]|	选取属于 bookstore 子元素的倒数第二个 book 元素。|
|/bookstore/book[position()<3]|选取属于 bookstore 的前两个 book 元素。|
|//title[@lang]|选取所有拥有名为 lang 的属性的 title 元素。|
|//title[@lang='eng']|选取所有 lang 属性值为 eng 的 title 元素。|
|/bookstore/book[price>35.00]|选取 bookstore 元素的 book 子元素，且该 book 元素的 price 子元素的值必须大于 35.00。|
|/bookstore/book[price>35.00]//title|选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。|

### 选取未知节点
XPath 通配符可用来选取未知的 XML 元素。
|通配符|描述|
|:------------:|:--------:|
|*|选取所有元素节点。|
|@*|选取所有属性节点。|
|node()|选取所有类型的节点。|

在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：
| 路径表达式 | 结果 |
|:------------:|:--------:|
|/bookstore/*|选取 bookstore 元素的所有子元素。|
|//*|选取文档中的所有元素。|
|//title[@*]|选取所有拥有属性的 title 元素。|
|//title[@*='eng']|选取所有拥有属性值为 eng 的 title 元素。|

### 选取若干路径
通过在路径表达式中使用"|"运算符，您可以选取若干个路径。

在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：
| 路径表达式 | 结果 |
|:------------:|:--------:| 
|//book/title \| //book/price|选取 book 元素的所有 title 和 price 元素。|
|//title \| //price|选取文档中的所有 title 和 price 元素。|
|/bookstore/book/title \| //price|选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。|

## 三. XPATH 轴

轴定义了在 XML 文档中选取节点的不同关系。下面列出了 XPath 中的轴：
|轴|描述|
|:------------:|:--------:|
|ancestor|选取当前节点的所有先辈（父、祖父等）。|
|ancestor-or-self|选取当前节点的所有先辈以及当前节点自己。|
|attribute|选取当前节点的所有属性。|
|child|选取当前节点的所有子节点。|
|descendant|选取当前节点的所有后代（子、孙等）。|
|descendant-or-self|选取当前节点的所有后代以及当前节点自己。|
|following|选取文档中当前节点的结束标签之后的所有节点。|
|following-sibling|选取当前节点之后的所有同级节点。|
|namespace|选取当前节点的所有命名空间节点。|
|parent|选取当前节点的父节点。|
|preceding|选取文档中当前节点的开始标签之前的所有节点。|
|preceding-sibling|选取当前节点之前的所有同级节点。|
|self|选取当前节点。|

## 四 XPath运算符

|运算符|描述|实例|返回值|
|:------------:|:--------:|:--------:|:--------:|
| \||计算两个节点集|//book \| //cd|	返回所有拥有 book 和 cd 元素的节点集|
|+|加法	|6 + 4	|10|
|-|减法|6 - 4|2|
|*|乘法|6 * 4|24|
|div|除法|6 div 4|1.5|
|=|等于|price=9.80|如果 price 是 9.80，则返回 true。如果 price 是 9.90，则返回 false。|
|!=|不等于|price!=9.80|如果 price 是 9.80，则返回 false。如果 price 是 9.90，则返回 true。|
|<|小于|price<9.80|如果 price 小于 9.80，则返回 true。如果 price 是 9.80 或者大于 9.80，则返回 false。|
|>|大于|price>9.80|如果 price 大于 9.80，则返回 true。如果 price 是 9.80 或者小于 9.80，则返回 false。|
|<=|小于或等于|price<=9.80|如果 price 小于或者等于 9.80，则返回 true。如果 price 大于 9.80，则返回 false。|
|>=|大于或等于|price>=9.80|如果 price 大于或者等于 9.80，则返回 true。如果 price 小于 9.80，则返回 false。|
|or|	或|price=9.80 or price=9.70|如果 price 是 9.80 或者 price 是 9.70，则返回 true。如果 price 既不是 9.80 也不是 9.70，则返回 false。|
|and|与|price>9.80 and price<10.00|如果 price 大于 9.80 并且 price 小于 10.00，则返回 true。如果 price 小于或者等于 9.80，或者 price 大于或者等于 10.00，则返回 false。|
|mod|取模|6 mod 4|2|

## 五. XPath函数
常用
|函数|描述|
|:------------:|:--------:|
|text()|返回节点的文本内容|
|name()|返回节点的名称|
|local-name()|返回节点的本地名称|
|namespace-uri()|返回节点的命名空间 URI|
|position()|返回当前节点在节点集中的位置|
|last()|返回节点集中的最后一个节点的位置|
|count()|返回节点集中的节点数量|
|number()|将值转换为数字|
|string()|将值转换为字符串|
|boolean()|将值转换为布尔值|
|not()|对布尔值取反|
|true()|返回 true 值|
|false()|返回 false 值|
