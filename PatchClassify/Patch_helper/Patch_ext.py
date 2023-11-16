#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import shutil
import random
import numpy as np
import pandas as pd
from PatchClassify import PatchClassify_config as config

# 定义相关路径
Save_CommitMsgPath = config.Save_CommitMsgPath # commit message的存放路径
PostivePath = config.PostivePath # 当前安全补丁的positive的补丁存放路径
NegativePath = config.NegativePath # 当前非安全补丁的negative的补丁存放路径

def get_commit_msg(patch_buf):
    '''
    该函数是用来提取commit message的内容，用来与补丁的after和ast补丁做配对进行安全补丁的训练
    '''
    temp_i = 1
    for i in range(len(patch_buf)):
        if "Commit" in patch_buf[i] or "Author" in patch_buf[i] or "commit" in patch_buf[i]:
            temp_i = i
            break
    st=temp_i+1
    for i in range(len(patch_buf)):
        if "diff" in patch_buf[i]:
            temp_i = i
            break
        else:
            temp_i = len(patch_buf)
    ed=temp_i-1
    content= patch_buf[st:ed]
    return content

def save_commitmsg(securi_patch_path=PostivePath, save_commitmsg_path=Save_CommitMsgPath):
    '''
    该函数是用来保存commit message的内容，用来与补丁的after和ast补丁做配对进行安全补丁的训练
    '''
    security_patch_buf = []
    # 检查路径的合法性
    if not os.path.exists(securi_patch_path):
        print("The path of security patch is not exist!")
        return
    if not os.path.exists(save_commitmsg_path):
        os.mkdir(save_commitmsg_path)
    for NVD in os.listdir(securi_patch_path):
        for CVE in os.listdir(os.path.join(securi_patch_path, NVD)):
            for commit in os.listdir(os.path.join(securi_patch_path, NVD, CVE)):
                commit_path = os.path.join(securi_patch_path, NVD, CVE, commit)
                # 1.读取commit message
                with open(commit_path, 'r',encoding='ISO-8859-1') as f: # fixme commit 这里的编码格式需要注意
                    security_patch_buf = f.readlines()
                f.close()
                # 2.提取commit message
                message = get_commit_msg(security_patch_buf)
                # 3.保存commit message
                write_empty_commitmsg(commitmsg = message,  commit_CVE = CVE)

                # temp_path = os.path.join(save_commitmsg_path, CVE)
                #
                # if not os.path.exists(temp_path):
                #     os.mkdir(temp_path)
                # temp_path = os.path.join(temp_path, commit)
                # with open(temp_path, 'w') as f:
                #     for line in message:
                #         f.write(line) # 将commit message写入文件
                # break # 一次只提取一个commit message
    return

# 读取commit message为空的commit
def write_empty_commitmsg(commitmsg = None, commit_CVE= None): #
    '''
    该函数是用来读取commit message为空的commit
    '''
    if commitmsg is None or commit_CVE is None:
        return

    # 检查路径的合法性
    if not os.path.exists(PostivePath):
        print("The path of security patch is not exist!")
        return
    if not os.path.exists(NegativePath):
        print("The path of save commit message is not exist!")
        return
    empty_commitmsg = []
    for trans_commit_file in os.listdir(NegativePath):
        if "AFTER" == trans_commit_file or "AST" == trans_commit_file:
            for CVE in os.listdir(os.path.join(NegativePath,trans_commit_file)):
                # 1.读取commit message
                if CVE != commit_CVE:
                    continue
                for commit in os.listdir(os.path.join(NegativePath,trans_commit_file,CVE)):
                    temp_commit_path = os.path.join(NegativePath,trans_commit_file,CVE,commit)
                    # 2.写入commit message
                    with open(temp_commit_path, 'r',encoding='ISO-8859-1') as f: # fixme commit 这里的编码格式需要注意
                        patch_buf = f.readlines()
                    f.close()
                    with open(temp_commit_path, 'w') as f: #w 是覆盖写入
                        f.writelines(commitmsg+patch_buf)
                    f.close()
                    print("CVE: %s, commit: %s, commit message write down!" % (CVE, commit))

    # for NVD in os.listdir(PostivePath): # 遍历NVD
    #     for CVE in os.listdir(os.path.join(PostivePath, NVD)):
    #         for commit in os.listdir(os.path.join(PostivePath, NVD, CVE)):
    #             commit_path = os.path.join(PostivePath, NVD, CVE, commit)
    #             # 1.读取commit message
    #             with open(commit_path, 'r',encoding='ISO-8859-1') as f: # fixme commit 这里的编码格式需要注意
    #                 security_patch_buf = f.readlines()
    #             # 2.提取commit message
    #             message = get_commit_msg(security_patch_buf)
    #             if len(message) == 0:
    #                 empty_commitmsg.append(commit_path)
    # return empty_commitmsg

if __name__ == "__main__":
    save_commitmsg() # 提取并保存commit message #
    #
