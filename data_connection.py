def enrich_model_input(data: dict, snowflake_client) -> dict:
    query_result = []
    for rank, city, state in snowflake_client.cursor().execute(f"SELECT RANK, CITY, STATE FROM COMPANIES LIMIT 5"):
        city = city.upper()
        rank += " rank"
        query_result.append([rank, city, state])
    return {"results": query_result}
