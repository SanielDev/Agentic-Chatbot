# Reads the uiconfigfile.ini
from configparser import ConfigParser # 'ConfigParser' class which helps to read the .ini file

class Config:
    def __init__(self, config_file="src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        # 'config' is an object which will be able to read the config files (eg: .ini')
        self.config.read(config_file)

    # As soon as the Config class is called, the constructor "__init__" runs and reads the configuration files
    # Based on our configuration file (uiconfigfile.ini), there are PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS, GROQ_MODEL_OPTIONS that we can pick
    # So, for all of these components, we will create a separate function

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(', ')
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(', ')
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(', ')

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")