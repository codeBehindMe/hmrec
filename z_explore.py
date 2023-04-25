# %%
from dataset.transactions import Transactions
from dataset.articles import Articles
import pandas as pd

# %%
articles = Articles("/mnt/disks/dd1/hmrec")
# %%
articles_df = articles.get_full_df()
# %%
articles_df.head(5)
# %%
articles_df.describe()
# %%
transactions = Transactions("/mnt/disks/dd1/hmrec")
# %%
txn_df = transactions.get_full_df()
# %%
txn_df.head(5)
# %%
txn_df["month"] = pd.DatetimeIndex(txn_df["t_dat"]).month
# %%
txn_df.head(3)
# %%
txn_df.groupby(["article_id", "month"]).count()
# %%
