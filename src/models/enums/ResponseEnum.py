from enum import Enum 

class ResponseSignal(Enum):
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS= "file_upload_successfully" 
    FILE_UPLOAD_FAILED= "file_upload_failed" 
    FILE_VALIDATION_FAILED= "file_validation_failed"
    FILE_VALIDATION_SUCCESS= "file_validation_successfully" 
