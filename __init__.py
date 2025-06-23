from .AC_Math import *
from .AC_Controlnet import *
from .AC_Picture import *
# from .AC_Sample import *
from .AC_TextTool import*
from .AC_MathV2 import *




NODE_CLASS_MAPPINGS = {
    # 啊程的数学运算器
    "Math_加法运算": Sum_AC,
    "Math_减法运算": Sub_AC,
    "Math_乘法运算": Mul_AC,
    "Math_除法运算": Div_AC,
    "Math_平方运算": Square_AC,
    "Math_数学累加": Mathaddtion,
    "Math_等差数列": Series_AC,
    "Math_X变量值" : X_AC,
    "Math_Y变量值" : Y_AC,
    "Math_浮点数转整数":Translate_Float_AC,
    "Math_整数转浮点数": Translate_INT_AC,
    "Math_数字转STR文字":Translate_STR_AC,
    "Math_文字显示面板":ShowText_AC,
    "Math_随机数区间": AC_randomize,
    "Math_绝对值": AC_ABS,
    "Math_平方根": AC_Sqrt,
    "Math_立方根": AC_Pow,
    "Math_数学表达式":AC_FUN_Expression,
    # 啊程的控制网格
    "Control_控制器加载": ControlNetLoader_AC,
    "Control_高级控制网格": ControlNetApplyAdvanced_AC,
    "Control_区域网格绘图控制": ConditioningSetArea_AC,
    "Control_条件合并": ConditioningCombine_AC,
    "Control_条件平均值":ConditioningAverage_AC,
    "Control_合并多组条件":ConditioningConcat_AC,
    "Control_条件遮罩":ConditioningSetMask_AC,
    "Control_高级条件遮罩":ConditioningSetTimestepRange_AC,
    "Control_一般控制网格": ControlNetSimple_AC,
    "Control_网格加载": UNETLoader_AC,
    # 啊程的图片工具
    "Pciture_图像预览": SaveImage_AC,
    "Pciture_分辨率设置": EmptyLatentImage_AC,
    "Pciture_重置数量": RepeatLatentBatch_AC,
    "Pciture_获取尺寸": Picturetool_AC,
    "Pciture_反转图像":ImageInvert_AC,
    "Pciture_双图合并": ImageBatch_AC,
    "Pciture_多图像合并": ImageBatch_MUT,
    "Pciture_加载图片遮罩": LoadImageMask_AC,
    "Pciture_加载图片": LoadImage_AC,
    "Pciture_图像放大": ImageScale_AC,
    "Pciture_图像放大(模型)": ImageScaleB_AC,
    "Pciture_获取白板": Mirrorpicture,
    "Pciture_选择模式": AC_Picture_Select,
    # 啊程的文本工具
    "Nodepad_提示词文本框": CLIPTextEncode_AC,
    "Nodepad_文本模型加载":CLIPLoader,
    "Nodepad_啊程记事本":AC_Notebook,
    "Nodepad_嵌入式文本":Text_AC,
    "Nodepad_跳过CLIP文本层":CLIPSetLastLayer_AC,


}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {

}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]