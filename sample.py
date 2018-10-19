from QeuryLoader import QueryLoader

ql = QeuryLoader()
query_format = ql.get_query("query", "get_test")
query = query_format.format(NAME='test')

print("Query String : ", query)
