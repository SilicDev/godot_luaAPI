def can_build(env, platform):
        return True

def configure(env):
        pass

def get_doc_classes():
    return [
        "Lua",
        "LuaThread",
        "LuaError",
    ]

def get_doc_path():
    return "docs"