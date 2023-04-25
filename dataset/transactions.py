import os


from typing import Optional, List
from dataset.articles import Articles

import pandas as pd


class Transactions:
    def __init__(self, path_to_data: Optional[str] = None) -> None:
        self.path_to_data = Articles._find_path_to_data(path_to_data)

    def get_full_df(self) -> pd.DataFrame:
        return pd.read_csv(os.path.join(self.path_to_data, "transactions_train.csv"))
