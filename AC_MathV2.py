# ===============================================================
class AC_FUN_Expression:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "Expression": ("STRING", {
                    "multiline": True, 
                    "default": '数学表达式'}),
            "tips": ("STRING", {
                    "multiline": False, 
                    "default": '分母不能为0,不然会报错'}),
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING',)
    
    # 返回节点命名
    RETURN_NAMES = ('STRING',)
    FUNCTION = "math_expression" 
    CATEGORY = "🌌AC_FUNV1.0/🔯MathTool" 

    def math_expression(self,Expression,tips=None):
        result = eval(Expression)
        return (result,)   