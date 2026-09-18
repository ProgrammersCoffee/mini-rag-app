from .BaseController import BaseController
from fastapi import UploadFile 
from src.models.enums import ResponseSignal 
from .ProjectController import ProjectController 
import re
import os

class DataController(BaseController):
    
    #constructor method 
    def __init__(self):
         super().__init__() # base controller will call his __init__ 
         self.size_scale= 1024*1024 # convert MB to bytes
        
    def validate_uploaded_file(self, file: UploadFile): 
        #FILE ALLOWED TYEPES check 
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False , ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value  #enumeration 
        #FILE MAX SIZE check  
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False  , ResponseSignal.FILE_SIZE_EXCEEDED.value #enumeration  
        
        return True , ResponseSignal.FILE_VALIDATION_SUCCESS.value #enumeration 
    
    
    def generate_unique_filepath(self,orig_file_name:str,project_id:str): 
        random_key=self.generate_random_string() # generate a random string) 
        project_path=ProjectController().get_project_path(project_id=project_id) 
        cleaned_file_name=self.get_clean_file_name(orig_file_name=orig_file_name)
        new_file_path= os.path.join(project_path,random_key + "_" + cleaned_file_name) 
        
        while os.path.exists(new_file_path):
                    random_key=self.generate_random_string() # generate a random string) 
                    new_file_path= os.path.join(project_path,random_key + "_" + cleaned_file_name)

        return new_file_path , random_key + "_" + cleaned_file_name  #updated 
            
          
        
    def get_clean_file_name(self,orig_file_name:str): 
        # remove any special characters from the original file name
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip()) 
        
        #replace spaces with underscores
        cleaned_file_name=cleaned_file_name.replace(" ","_")
        
        return cleaned_file_name