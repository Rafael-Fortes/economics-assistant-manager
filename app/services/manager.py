from app.schemas.manager import TransactionCreateRequest, TransactionCreateResponse
from fastapi import HTTPException
from pathlib import Path
import pandas as pd


class ManagerService:
    def __init__(self):
        transactions_file_path = Path(__file__).resolve().parent.parent / "data" / "transactions.csv"
        self.transactions_file_path = transactions_file_path
        self.initialize_dataset()

    def initialize_dataset(self) -> None:
        """
        Initializes the dataset
        """
        if not self.transactions_file_path.exists():
            df = pd.DataFrame(columns=["amount", "description", "category", "location", "payment_method", "notes", "date"])
            df.to_csv(self.transactions_file_path, index=False)
            print(f"Dataset initialized in {self.transactions_file_path}")
        else:
            print(f"Dataset already initialized in {self.transactions_file_path}")


    def create_transaction(self, transaction: TransactionCreateRequest) -> TransactionCreateResponse:
        """
        Creates a new transaction

        Args:
            transaction: The transaction to create

        Returns:
            The transaction created
        """
        try:
            print(f"Creating transaction in {self.transactions_file_path}")
            print(f"Transaction: {transaction.model_dump()}")
            df = pd.read_csv(self.transactions_file_path)

            new_row = pd.DataFrame([transaction.model_dump()])
            df = pd.concat([df, new_row], ignore_index=True)

            df.to_csv(self.transactions_file_path, index=False)
            print(f"Transaction created in {self.transactions_file_path}")

            return TransactionCreateResponse(
                transaction=transaction.model_dump()
            )
        except Exception as e:
            print(f"Error creating transaction: {e}")
            raise HTTPException(status_code=500, detail=f"Error creating transaction: {e}")