import math
MAX_RESOLUTION=8192


# 这是啊程自制的数学算法，适用于各种通用算的变量运算
# 变量
class X_AC:

    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{"X":("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),"tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "整数变量X"}
                ),
                }}
    
    RETURN_TYPES = ("STRING","INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "x_ac"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def x_ac(self,X,tips=None):
        return(str(X), X)

# 变量Y
class Y_AC:

    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{"Y":("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),"tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "浮点数变量Y"}
                ),
                }}
    
    RETURN_TYPES = ("STRING","FLOAT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "y_ac"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def y_ac(self,Y,tips=None):
        return(str(Y), Y)

        
#加法 
class Sum_AC:

    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_1": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_2": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                
            }}

    RETURN_TYPES = ("STRING", "INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "mathematical"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def mathematical(self,int_1,int_2 ):
        x = int_1 + int_2
        result = int(x)
        return(str(result), result)
  


# 减法
class Sub_AC:

    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_1": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_2": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                
            }}

    RETURN_TYPES = ("STRING", "INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "sub"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def sub(self,int_1,int_2 ):
        x = int_1 - int_2
        result = int(x)
        return (str(result), result)

# 乘法
class Mul_AC:

    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_1": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_2": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                
            }}

    RETURN_TYPES = ("STRING", "INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "mul"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def mul(self,int_1,int_2 ):
        x = int_1*int_2
        result = int(x)
        return (str(result), result) 
# 除法
class Div_AC:

    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_1": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "int_2": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" ,# Cosmetic only: display as "number" or "slider"
                }),
                    "tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "得出的结果取整数值,当结果小于0,则最小取到0,且除数的最小值不能小于1"}
                ),
                
            }}

    RETURN_TYPES = ("STRING", "INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "div"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def div(self,int_1,int_2,tips=None):
        if int_2 != 0:
                x = int_1/ int_2
                return (str(x), int(x))
        else:
            print("ZeroError")
            
# 平方
class Square_AC:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "x": ("FLOAT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": MAX_RESOLUTION, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),                
            }}

    RETURN_TYPES = ("STRING", "INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "square_ac"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def square_ac(self,x):
        y = x**2
        return (str(y), int(y))

# 数值转换
class Translate_Float_AC:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "float": ("FLOAT",{"forceInput": True}),
                    #       {
                    # "default": 0, 
                    # "min": 0, #Minimum value
                    # "max": MAX_RESOLUTION, #Maximum value
                    # "step": 1, #Slider's step
                    # "display": "number"},), # Cosmetic only: display as "number" or "slider" ),
                "tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "转换浮点数为整数"}),
                        }}

    RETURN_TYPES = ("STRING", "INT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "translate_digits_ac"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def translate_digits_ac(self,float,tips=None):
        y  = int(float)
        return (str(y), y)

# 整数转浮点数
class Translate_INT_AC:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int": ("INT",{"forceInput": True}),
                    #       {
                    # "default": 0, 
                    # "min": 0, #Minimum value
                    # "max": MAX_RESOLUTION, #Maximum value
                    # "step": 1, #Slider's step
                    # "display": "number"},), # Cosmetic only: display as "number" or "slider" ),
                "tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "整数转换成浮点数"}),
                        }}

    RETURN_TYPES = ("STRING", "FLOAT")
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "translate_int_ac"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def translate_int_ac(self,int,tips=None):
        y  = float(int)
        return (str(y), y)

# 数字转文字
class Translate_STR_AC:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "float": ("FLOAT",{"forceInput": True}),
                # "int": ("INT",{"forceInput": True}),
                "tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "数字转文字"}),
                        }}

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "translate_str_ac"
    #OUTPUT_NODE = False
    CATEGORY = "AC_FUN/🔯MathTool"

    def translate_str_ac(self,float=None,tips=None):
        x = str(float)
        return (x,)

 # 查看结果
class ShowText_AC:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify_ac"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "AC_FUN/🔯MathTool"

    def notify_ac(self, text, unique_id = None, extra_pnginfo=None):
        if unique_id and extra_pnginfo and "acwork" in extra_pnginfo[0]:
            acwork = extra_pnginfo[0]["acwork"]
            node = next((x for x in acwork["nodes"] if str(x["id"]) == unique_id[0]), None)
            if node:
                node["widgets_values"] = [text]
        return {"ui": {"text": text}, "result": (text,)}

# 累加数学运算
class Mathaddtion:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_1": ("INT", {"forceInput": False}),
                "int_2": ("INT", {"forceInput": False}),
                "tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "int_1必须大于int_2才能运行"}),
                }
            }
    RETURN_TYPES = ("STRING","INT")
    FUNCTION = "mathaddtion"
    OUTPUT_NODE = True
    CATEGORY = "AC_FUN/🔯MathTool"

    def mathaddtion(self, int_1,int_2,tips=None):
        x = 0
        y = 0
        z = int_1 - int_2
        if z <=0:
            pass
        else:
            while x<=z:
             y += x
             x += 1
            #  print(y)
        return (str(y),y)

# 等差数列
class Series_AC:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "start": ("INT", {"forceInput": False}),
                "step": ("INT", {"forceInput": False}),
                "count": ("INT", {"forceInput": False}),
                "tips": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "等差数学数列"}),
                }
            }
    RETURN_TYPES = ("STRING","INT")
    FUNCTION = "series"
    OUTPUT_NODE = True
    CATEGORY = "AC_FUN/🔯MathTool"

    def series(self, start, step, count, tips=None):
        y = 0
        min = 0
        while min <=count:
         y = start
         start += step
         min += 1
        return (str(y),y)
# 随机数选择========================================================
class AC_randomize:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": 
                       {"int":("INT",{"min":0,"max":9999999999999}),
                        "tips": ("STRING", {
                        "multiline": False,
                        "default": "随机选择数字的区间返回随机区间"}),
         
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING','INT','FLOAT')
    
    # 返回节点命名
    # RETURN_NAMES = ()
    FUNCTION = "ac_randomize"
    CATEGORY = "AC_FUN/🔯MathTool" 

    def ac_randomize(self,int,tips=None):
            import random
            num = random.randint(0,int)
            return (num,str(num),float(num))

# 求数学运算的绝对值======================================================
class AC_ABS:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": 
                       {"int":("INT",{"min":-9999999999999,"max":9999999999999}),
                        "tips": ("STRING", {
                        "multiline": False,
                        "default": "绝对值"}),
         
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING','INT','FLOAT')
    
    # 返回节点命名
    # RETURN_NAMES = ()

    FUNCTION = "ac_abs"
    CATEGORY = "AC_FUN/🔯MathTool" 

    def ac_abs(self,int,tips=None):
            int = abs(int)
            return (int,str(int),float(int))
        
# 求平方根===========================================================
class AC_Sqrt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": 
                       {"int":("INT",{"min":-9999999999999,"max":9999999999999}),
                        "tips": ("STRING", {
                        "multiline": False,
                        "default": "求平方根"}),
         
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING','INT','FLOAT')
    
    # 返回节点命名
    # RETURN_NAMES = ()

    FUNCTION = "ac_sqrt"
    CATEGORY = "AC_FUN/🔯MathTool" 

    def ac_sqrt(self,int,tips=None):
            int = math.sqrt(int)
            return (int,str(int),float(int))

# 求立方根===========================================================
class AC_Pow:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": 
                       {"int":("INT",{"min":-9999999999999,"max":9999999999999}),
                        "tips": ("STRING", {
                        "multiline": False,
                        "default": "求立方根"}),
         
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING','INT','FLOAT')
    
    # 返回节点命名
    # RETURN_NAMES = ()

    FUNCTION = "ac_pow"
    CATEGORY = "AC_FUN/🔯MathTool" 

    def ac_pow(self,int,tips=None):
            num = int **(1/3)
            return (num,str(num),float(num))


        

#do some processing on the image, in this example I just invert it   
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "加法运算": Sum_AC,
    "减法运算": Sub_AC,
    "乘法运算": Mul_AC,
    "除法运算": Div_AC,
    "平方运算": Square_AC,
    "数学累加": Mathaddtion,
    "等差数列": Series_AC,
    "X变量值" : X_AC,
    "Y变量值" : Y_AC,
    "浮点数转整数":Translate_Float_AC,
    "整数转浮点数": Translate_INT_AC,
    "数字转STR文字":Translate_STR_AC,
    "文字显示面板":ShowText_AC,
    "随机数区间": AC_randomize,
    "绝对值": AC_ABS,
    "平方根": AC_Sqrt,
    "立方根": AC_Pow,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Sum_AC": "加法运算",
    "Sub_AC": "减法运算",
    "Mult_AC": "乘法运算",
    "DIV_AC": "除法运算",
    "Square_AC": "平方运算",
    "Mathaddtion": "数学累加",
    "Series_AC": "等比数列",
    "X_AC" :"X变量值",
    "Y_AC": "Y变量值",
    "Translate_Float_AC": "浮点数转整数",
    "Translate_INT_AC": "整数转浮点数",
    "Translate_STR_AC": "数字转STR文字",
    "ShowText_AC": "文字显示面板",
}

if __name__ == "__main__":
    acfun = Sub_AC()
    print(acfun.sub(1,2))
    abfun = Div_AC()
    print(abfun.div(10,10))
    fun = Square_AC()
    print(fun.square_ac(10))
    x = X_AC()
    print(x.x_ac(10))
    x = Mathaddtion()
    x.mathaddtion(100,0)





