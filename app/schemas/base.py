from pydantic import BaseModel, Field
from typing import Optional, Dict

class BaseResponse(BaseModel):
    """
    Base response model
    """
    message: str = Field(..., description="The message of the response")
    data: Optional[Dict] = Field(None, description="The data of the response")