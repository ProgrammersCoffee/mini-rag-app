from .BaseController import BaseController 
#from .DataController import DataController 
#from src.models.enums import ResponseSignal 
import os 

class ProjectController(BaseController): 
    def __init__(self):
        super().__init__()  # base controller will call his __init__ 
    
    def get_project_path(self,project_id:str):# retrive the path that i put inside it the file..  
        project_dir=os.path.join(self.files_dir,project_id)             
        
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        
        return project_dir
