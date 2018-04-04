# MongoDB Helpers

## Installation
1. Clone the repo.
  * `git clone git@github.com:mnguyenngo/mongo-helpers.git`
2. Go to the cloned repo.
  * `cd mongo-helpers`
3. Install the package.
  * `pip install .`

## Example

![screenshot]

[screenshot]: /images/screenshot.png

## PyMongo Syntax for reference
(mongo_helper syntax in comments)

```python
client = MongoClient(host, address)
db = client[db_name]  # use get_db_names()
c = db[collection_name]  # use get_collection_names(db)
df = pd.DataFrame(list(c.find()))  # use convert_db_to_df(db, c)
```
