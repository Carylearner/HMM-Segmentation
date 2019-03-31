
from common.logger import logger
from model.hmm import HMM

logger.info("项目启动")
hmm = HMM()
hmm.train(r".\data\trainCorpus.txt_utf8")
logger.info("项目结束")
text = "这是一个非常棒的方案!"
res = hmm.cut(text)
print(text)
print(str(list(res)))