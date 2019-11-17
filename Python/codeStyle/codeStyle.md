一、函数式编程
模块化，每个小模块做好unittest，然后再做evaluation
做unittest常用两个包 ddt unittest（后者为python自带）
先写test 确定自己要比较什么值 再去写函数的实现 否则用自己想好的逻辑算出来的数值去通过自己想好的逻辑 等于没有test
一般test三个值 中间 开头 结尾值

二、命名规则：
驼峰式，不加下划线
函数、变量：首字母小写
类（class）：首字母大写
class中 变量（值已固定）在前 函数在后

三、使用list comprehension列表解析
不单独使用for循环，会降低计算效率（当计算量大的时候，可以在计算时长上体现出来）
list[]和tuple()：list中的值可改变 tuple中的值不可改变

四、其他
使用相对路径
少用注释（函数功能在命名上直接体现出来）
import中 先导入第三方库 再导入自己写的函数
Linux系统上，推荐使用sublime编译
zip（python自带函数）用于将两个list里对应位置的元素两两配对 形成新的list
关于坐标的运算，很多函数都是numpy里有的，要擅长使用它们来提高效率
