"""
统一的模型实例管理（单例模式）
用于在多个 agent 之间共享同一个 LLM 模型实例，减少资源消耗
"""

_model_instance = None

def get_model():
    """
    获取统一的模型实例
    延迟初始化，只在第一次调用时创建模型
    """
    global _model_instance
    if _model_instance is None:
        from config.llm_config import llm_model_config
        
        # 检查配置类型，使用对应的模型
        if hasattr(llm_model_config, 'get') and 'model_name' in llm_model_config:
            model_name = llm_model_config.get('model_name', '')
            
            # DeepSeek 模型
            if 'deepseek' in model_name.lower():
                from langchain_deepseek import ChatDeepSeek
                _model_instance = ChatDeepSeek(
                    model=llm_model_config["model_name"],
                    api_key=llm_model_config["api_key"],
                    api_base=llm_model_config.get("base_url", "https://api.deepseek.com")
                )
            else:
                # 默认使用 OpenAI 兼容接口
                from langchain_openai import ChatOpenAI
                _model_instance = ChatOpenAI(
                    model=llm_model_config["model_name"],
                    api_key=llm_model_config["api_key"],
                    base_url=llm_model_config.get("base_url", "")
                )
        else:
            # 默认使用 OpenAI
            from langchain_openai import ChatOpenAI
            _model_instance = ChatOpenAI(
                model=llm_model_config["model_name"],
                api_key=llm_model_config["api_key"],
                base_url=llm_model_config["base_url"]
            )
    return _model_instance
