import torch

import os
import sys

from PIL import Image, ImageOps
from PIL.PngImagePlugin import PngInfo
import numpy as np


sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))


import comfy.diffusers_load
import comfy.samplers
import comfy.sample
import comfy.sd
import comfy.utils

import comfy.clip_vision

import comfy.model_management
from comfy.cli_args import args

import folder_paths


def before_node_execution():
    comfy.model_management.throw_exception_if_processing_interrupted()

def interrupt_processing(value=True):
    comfy.model_management.interrupt_current_processing(value)

MAX_RESOLUTION=8192



class CLIPLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "clip_name": (folder_paths.get_filename_list("clip"), ),
                             }}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "load_clip"

    CATEGORY = "🌌AC_FUNV1.0/📗TextTool"

    def load_clip(self, clip_name):
        clip_path = folder_paths.get_full_path("clip", clip_name)
        clip = comfy.sd.load_clip(ckpt_paths=[clip_path], embedding_directory=folder_paths.get_folder_paths("embeddings"))
        return (clip,)
    

class AC_Notebook:
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{"text":("STRING", {
                    "multiline": True,})
                 }}
    
    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "notebook"
    #OUTPUT_NODE = False
    CATEGORY = "🌌AC_FUNV1.0/📗TextTool"
    def notebook(self,text):
        tokens = str(text)
        return (tokens,)
      
# 啊程文本提示框
class CLIPTextEncode_AC:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True,
                                                 "default":"啊程提示!请用英文的形式描述你心中所想"}), "clip": ("CLIP", )}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode_ac"

    CATEGORY = "🌌AC_FUNV1.0/📗TextTool"

    def encode_ac(self, clip, text):
        tokens = clip.tokenize(text)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {"pooled_output": pooled}]], )

# 外置文本输入
class Text_AC:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                 "tips": ("STRING", {"multiline": False,
                 "default":"请选择你输入的text文件后缀的文本"}),}
                 }
    RETURN_TYPES = ("CONDITIONING","positve","negative",)
    FUNCTION = "text_ac"

    CATEGORY = "🌌AC_FUNV1.0/📗TextTool"

    def text_ac(self,tips=None,):
        file = open('D/:text.text', 'r',encoding='UTF-8')
        str(file.read())
        print(str)
        return (str,)
# 跳过图层设置
class CLIPSetLastLayer_AC:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "clip": ("CLIP", ),
                              "stop_at_clip_layer": ("INT", {"default": -1, "min": -24, "max": -1, "step": 1}),
                              "tips": ("STRING", {"multiline": False,
                              "default":"-1则为跳过最后一层,-2是跳过最后倒数第二层"}),
                              }}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "set_last_layer_ac"

    CATEGORY = "🌌AC_FUNV1.0/📗TextTool"

    def set_last_layer_ac(self, clip, stop_at_clip_layer,tips=None):
        clip = clip.clone()
        clip.clip_layer(stop_at_clip_layer)
        return (clip,)


NODE_CLASS_MAPPINGS = {
    "提示词文本框": CLIPTextEncode_AC,
    "文本模型加载":CLIPLoader,
    "啊程记事本":AC_Notebook,
    "嵌入式文本":Text_AC,
    "跳过CLIP文本层":CLIPSetLastLayer_AC,
}

NODE_DISPLAY_NAME_MAPPINGS = {
}
if __name__ == "__main__":
    pass

