#!/usr/bin/env python
# -*- coding: utf-8 -*-
# environment settings.
import os
import time
import PatchClassify_config as Classify_config
_FILEFLAG_ = "_patchRNN_"

# Switch_Flag_file = "our2/"  #"OrigPatch_Expriment/"  NVD_Expriment test_error our3
Switch_Flag_file = Classify_config.Switch_Flag_file

_COLAB_ = 0 if (os.getenv('COLAB_GPU', 'NONE') == 'NONE') else 1 # 0 : Local environment, 1 : Google Colaboratory.
# file paths.
RootPath = './drive/My Drive/Colab Notebooks/' if (_COLAB_) else './'
DataPath = RootPath + 'data/'
SecureDatPath = DataPath + Switch_Flag_file+'security_patch/' # security 的补丁是所有数据集公用的，所以不用加Switch字段
PosDatPath = DataPath  + Switch_Flag_file+'positive/'
NegDatPath = DataPath +  Switch_Flag_file+'negative/'
TempPath = RootPath + 'temp/' + Switch_Flag_file
Log_path = RootPath + "Logs/" + Switch_Flag_file + _FILEFLAG_+"train_" +"/" #这里使用时间戳来区分每一次的测试和训练