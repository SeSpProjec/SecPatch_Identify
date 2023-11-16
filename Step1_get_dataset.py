import os
import time
import shutil
import random
import numpy as np
import pandas as pd
import  PatchClassify_config as config
rootPath = config.RootPath
githubPath = config.GithubPath
negativePath = config.NegativePath

githubList = [file for root, ds, fs in os.walk(githubPath) for file in fs]

listLen = len(githubList)
listNum = list(range(listLen)) # [0, 1, 2, 3, ...]
random.shuffle(listNum)

cnt = 0
folder = 2
for i in range(listLen):
    index = listNum[i]
    filename = githubList[index]
    src = os.path.join(githubPath, filename)
    fdst = os.path.join(negativePath, 'commit' + str(folder).zfill(2)) #初始的文件没有经过聚类，所以首先首先整体都属于negative
    if not os.path.exists(fdst):
        os.mkdir(fdst)
    dst = os.path.join(fdst, filename)

    shutil.move(src, dst) # 将原始补丁（github） 移动进 目的文件夹（分类）
    print(dst)
    cnt += 1
    if cnt == 100000:
        cnt = 0
        folder += 1
