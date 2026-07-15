from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    """
    Transaction model
    """
    amount: float = Field(..., description="The amount of the transaction")
    description: str = Field(..., description="The description of the transaction")
    category: Optional[str] = Field(None, description="The category of the transaction")
    location: Optional[str] = Field(None, description="The location of the transaction")
    payment_method: Optional[str] = Field(None, description="The payment method of the transaction")
    notes: Optional[str] = Field(None, description="The notes of the transaction")
    date: Optional[datetime] = Field(datetime.now(), description="The date of the transaction")


class TransactionCreateRequest(Transaction):
    """
    Request to create a new transaction
    """
    pass

class TransactionCreateResponse(BaseModel):
    """
    Response to create a new transaction
    """
    transaction: Transaction = Field(..., description="The transaction created")