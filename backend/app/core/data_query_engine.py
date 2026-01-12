import duckdb
import numpy as np
from .data_indexer import encoder, index, METADATA, TABLE_REGISTRY

def semantic_search(query: str, top_k=3):
    q_emb = encoder.encode([query])[0].astype("float32")
    D, I = index.search(np.array([q_emb]), top_k)
    return [METADATA[i]["table"] for i in I[0]]

def aggregate_query(table_key: str, sql_instruction: str):
    df = TABLE_REGISTRY[table_key]
    con = duckdb.connect()
    con.register("t", df)
    return con.execute(sql_instruction).df()

def run_data_query(query_text: str, sql_instruction: str):
    tables = semantic_search(query_text)

    results = []
    for t in tables:
        try:
            df_result = aggregate_query(t, sql_instruction)
            results.append(df_result)
        except Exception:
            continue

    if not results:
        raise ValueError("No valid results found.")

    return results[0] if len(results) == 1 else results
