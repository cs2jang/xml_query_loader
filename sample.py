from QeuryLoader import QueryLoader

ql = QeuryLoader()
query_format = ql.get_query("query", "get_name")  # get_query(xml file name, id tag name)
query = query_format.format(NAME='test')

print("Query String : ", query)
