def query_transform_data(block_input: dict, client) -> dict:
    query_result = []
    limit = 1
    if block_input and 'limit' in block_input:
        limit = block_input['limit']
    for rank, city, state in client.cursor().execute(f"SELECT RANK, CITY, STATE FROM COMPANIES LIMIT {limit}"):
        city = city.upper()
        rank += " rank"
        query_result.append([rank, city, state])
    return {"results": query_result}