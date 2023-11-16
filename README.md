# SecurityPatchIdentificationRNN

**Task**: Security Patch Identification using RNN model.

**Developer**: Jincheng Yang

**Date**: 2023.10.02

**Description**: patch identification using both commit messages and normalized diff code.By different ratios of different security patch datasets, test the effectiveness of the SbSpDB security patch datasets for machine learning tasks.

**File Structure**:

    |-- SecurityPatchIdentificationRNN
        |-- README.md                               # this file.
        |-- Step1_get_dataset.py                    # get dataset.
        |-- Step2_PatchFeatures.py                  # extract features.
        |-- Step3_PatchClassify.py                  # classify patches.
        |-- Step4_patchrnn_train.py                 # train RNN model.
        |-- Log                                     # log files.
        |-- PatchClassify
                |-- candidates              # found samples need to be judged.
                |-- featurefiles            # feature files.
                        |-- feature00.csv   # positive feature file.
                        |-- feature01.csv   # negative feature file.
                |-- judged                  # already judged samples.
                        |-- negatives
                        |-- positives
                |-- security_patch          # positive patches.
                |-- temp                    # temporary stored variables.
                        |-- distMatrix.npy
                        |-- outIndex.npy
                |-- main.py                 # main entrance.
    
        |-- analysis                                # task analysis.
        |-- data                                    # data storage.
                |-- negatives                           # negative samples.
                |-- positives                           # positive samples.
                |-- security_patch                      # positive samples. (official)
        |-- temp                                    # temporary stored variables.
                |-- data.npy                            # raw data. (important)
                |-- props.npy                           # properties of diff code. (important)
                |-- msgs.npy                            # commit messages. (important)
                |-- ...                                 # other temporary files. (trivial)

**Dependencies**:

```shell script
pip install clang == 6.0.0.2
pip install torch == 1.2.0 torchvision == 0.4.0
pip install nltk  == 3.3
or
pip install -r requirements
```

**Usage**:

- Step1_get_dataset.py

- Step2_PatchFeatures.py

  - 特征定义

    - 例如在文件的开头中通过列表定义MI_keyword特

  - 安全补丁特征组合：

    - ./PatchClassify_config.py

      `该文件的secfea_list_*变量定义了不同的安全补丁的特征组合，目的是为了通过不同的特征组合来测试不同的安全补丁特征对于安全补丁分类任务的影响。`

  - run example:
        positive patch:'python Step2_PatchFeatures.py 1'
        negative patch:'python Step2_PatchFeatures.py 0'

  - output file：`数据集的特征文件存储在./PatchClassify/featurefiles/目录下，文件名为feature*.csv（1为postive，0为negative），分别对应不同的安全补丁特征组合。`

- Step3_PatchClassify.py
      ``这个文件的通过预定义的安全补丁特征，在非安全补丁数据集（negative）中找到与安全补丁（postive）相似的安全补丁，然后将相似的安全补丁存储到./PatchClassify/candidates/目录下，以便后续的人工判断。``

  - 特征定义:

    ``例如在文件的开头中通过列表定义MI_keyword特征``

  - 安全补丁特征组合：

    - ./PatchClassify_config.py
      secfea_list_*变量定义了不同的安全补丁的特征组合，目的是为了通过不同的特征组合来测试不同的安全补丁特征对于安全补丁分类任务的影响

    - run example:
      `python Step3_PatchClassify.py`

- Step4_patchrnn_train.py
      `这个文件是训练安全补丁数据集和非安全补丁数据集，测试不同安全补丁数据集配比下对安全补丁分类任务的影响`

  - process：

       1. 读取安全补丁数据集和非安全补丁数据集

    2. 处理diff文件 `这些步骤用于准备训练RNN模型所需的数据和标签，并将它们转换为适当的格式。`

       - 获取diff标记词汇表：使用`GetDiffVocab()`函数获取diff标记词汇表，该函数接受diff属性列表作为输入，并返回diff标记词汇表和diff标记的数量。

          - 获取diff标记字典：使用`GetDiffDict()`函数获取diff标记字典，该函数接受diff标记词汇表作为输入，并返回diff标记字典。
            练的嵌入层权重：使用`GetDiffEmbed()`函数获取预训练的嵌入层权重，该函数接受diff标记字典和嵌入维度作为输入，并返回预训练的嵌入层权重。 
          - 将diff代码分为版本之前和版本之后的代码：使用`DivideBeforeAfter()`函数将diff代码分为版本之前和版本之后的代码，并返回分割后的diff代码列表和最大长度。
          - 获取diff文件的版本之前和版本之后的代码长度：如果版本之前和版本之后的代码长度都大于最大长度，则将最大长度设置为`_TwinMaxLen_`，否则将最大长度设置为版本之前和版本之后的代码长度中的最大值。
          - 获取特征数据和标签的映射：使用`GetTwinMapping()`函数获取特征数据和标签的映射，该函数接受分割后的diff代码列表、最大长度和差异标记字典作为输入，并返回特征数据和标签的映射。

      3.  处理commit message
         - 获取commit message：使用`GetCommitMsgs()`函数获取commit message，该函数接受数据作为输入，并返回commit message列表。
         - 获取commit message的token词汇表：使用`GetMsgVocab()`函数获取commit message标记词汇表和最大token长度，该函数接受commit message列表作为输入，并返回commit message token词汇表和最大token长度。
         - 获取commit message token字典：使用`GetMsgDict()`函数获取commit message token字典，该函数接受commit message token词汇表作为输入，并返回commit message token字典。
         - 获取预训练的嵌入层权重：使用`GetMsgEmbed()`函数获取预训练的嵌入层权重，该函数commit message token字典和嵌入维度作为输入，并返回预训练的嵌入层权重。
         - 获取特征数据和标签的映射：使用`GetMsgMapping()`函数获取特征数据和标签的映射，该函数接受commit message列表、最大标记长度和commit message token作为输入，并返回特征数据和标签的映射。
         - 将diff数据与commit message数据组合：使用`CombineTwinMsgs()`函数将diff数据与commit message数据组合，并返回组合后的数据和标签。
         - 将数据分为训练集和测试集：使用`SplitData()`函数将数据和标签分为训练集和测试集，并返回训练集数据、训练集标签、测试集数据和测试集标签。

  - run example:
        `python Step4_patchrnn_train.py`