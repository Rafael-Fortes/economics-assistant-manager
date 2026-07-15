from app.services.manager import ManagerService
from app.schemas.manager import TransactionCreateRequest
from app.schemas.base import BaseResponse
from fastapi import APIRouter

router = APIRouter(
    prefix="/manager",
    tags=["manager"],
)

manager_service = ManagerService()

@router.post("/transaction")
def create_transaction(transaction: TransactionCreateRequest) -> BaseResponse:
    """
    Creates a new transaction

    Args:
        transaction: The transaction to create

    Returns:
        The transaction created
    """
    transaction = manager_service.create_transaction(transaction)
    return BaseResponse(
        message="Transaction created",
        data=transaction.model_dump()
    )