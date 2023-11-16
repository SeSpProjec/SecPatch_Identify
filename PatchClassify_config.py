#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
root_path = os.path.dirname(os.path.abspath(__file__)) # 获取当前文件的根目录


Switch_Flag_file = "our2/" # "test_924_partfea2"
#'PatchDB_Expriment(contra)_partfea1/' #"OrigPatch_Expriment/"  'NVD_Expriment/'  'PatchDB_Expriment/' test_error/ our3/用来切换不同样本数据集

RootPath = root_path + "/PatchClassify/" # './PatchClassify' #代表本目录
GithubPath = RootPath + '/github_commit/'
PostivePath = RootPath +  '/security_patch/'+Switch_Flag_file #NVD_Expriment/' # '/security_patch'
# PostivePath = RootPath + '/test_traindata/'
NegativePath = RootPath + '/negative_patch/' + Switch_Flag_file
# NegativePath = RootPath + '/test_traindata/' + Switch_Flag_file
Featurecsv_Path = RootPath + '/featuresfiles/' + Switch_Flag_file
Temp_Path = RootPath + "/temp/" + Switch_Flag_file
CandiPath = root_path + '/data/' + Switch_Flag_file # 直接将分类的结果复制到训练文件夹下
#judgement path
JudPath = RootPath + "/judged/" + Switch_Flag_file
JudPosPath = JudPath + '/positives/' + Switch_Flag_file
JudNegPath = JudPath + '/negatives/' + Switch_Flag_file

# commit message path 该路径用来提取cve相应的commit message，用来与补丁的after和ast补丁做配对进行安全补丁的训练
Save_CommitMsgPath = PostivePath + '/commit_msg/' # commit message 的存放路径就和对应的安全补丁在一起

# 特征输入模板list
secfea_list_1 = [ # 保留全部的特征
    'keyword definition','arithmetic operations','relational operations',"logical operations","bit operations",
    "memory keywords","if keywords","loop keywords","jump keywords","C keywords","C++ keywords",
    "dictionary keywords","race keywords","not keywords","line count","chat count","preprocess count",
    "diff count","hunk count","func count"
]

secfea_list_2 = [ # 保留部分的特征组合
    'keyword definition',
    "memory keywords","if keywords","loop keywords","jump keywords"
]

secfea_list_3 = [ # 保留部分的特征组合
    'keyword definition',
    "memory keywords","if keywords","loop keywords","jump keywords",
    "logical operations","race keywords","not keywords"
]

