import os
from typing import Optional, List
import pandas as pd


class Articles:
    def __init__(self, path_to_data: Optional[str] = None) -> None:
        self.path_to_data = self._find_path_to_data(path_to_data)

    @staticmethod
    def _find_path_to_data(path_to_data: Optional[str] = None) -> str:
        if path_to_data is None:
            return os.environ["DATA_PATH"]

        return path_to_data

    def get_full_df(self) -> pd.DataFrame:
        return pd.read_csv(os.path.join(self.path_to_data, "articles.csv"))

    def get_images_for_article(self, article_id: int) -> List[object]:
        raise NotImplementedError()

    def _construct_basepath_for_images(self, article_id: int) -> str:
        folder_key = str(article_id)[0:3]

        return os.path.join(self.path_to_data, "images/", folder_key)
