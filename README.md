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

## PyMongo Syntax for Reference
(mongo_helper syntax in comments)

```python
client = MongoClient(host, address)
client.database_names() # use get_db_names()
db = client[db_name]
db.collection_names()  # use get_collection_names(db)
c = db[collection_name]  
df = pd.DataFrame(list(c.find()))  # use convert_db_to_df(db, c)
```
