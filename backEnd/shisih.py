# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import ltp
import transformers
import tokenizers
from ltp import LTP
import torch


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    ltp = LTP()
    seg, hidden = ltp.seg(["你今天吃饭了吗？"])
    dep = ltp.dep(hidden)
    print(seg)
    print(dep)
    # print(torch.__version__)
    # # print(ltp.__version__)
    # print(tokenizers.__version__)
    # print(transformers.__version__)

# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
# ltp==4.1.5.post2
# pygtrie==2.4.2
# sacremoses==0.0.45
# tokenizers==0.10.3
# transformers==4.7.0

##Here is the test code execution

# ltp = LTP()
#  seg, hidden = ltp.seg(["你今天吃饭了吗？"])
#  dep = ltp.dep(hidden)
#  print(seg) ##[['你', '今天', '吃饭', '了', '吗', '？']]
#  print(dep) ##[[(1, 3, 'SBV'), (2, 3, 'ADV'), (3, 0, 'HED'), (4, 3, 'RAD'), (5, 3, 'RAD'), (6, 3, 'WP')]]