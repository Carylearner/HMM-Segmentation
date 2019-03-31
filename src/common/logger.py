# coding:utf-8
"""
日志配置模块
"""

import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S-',filename='hmmSt.log',filemode='a')


#设置日志的控制台输出


formatter = logging.Formatter('%(asctime)s %(name)6s: %（levelname)-6s %(message)s')
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)