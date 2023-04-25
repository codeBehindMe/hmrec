#%%
from dataset.articles import Articles
# %%
articles = Articles("/mnt/disks/dd1/hmrec")
# %%
articles_df = articles.get_full_df()
# %%
articles_df.head(5)
# %%
articles_df.describe()
# %%
