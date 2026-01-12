from .llm_engine import llm
from .data_query_engine import run_data_query
from .finance_templates import TEMPLATES

class AnalyticsAgent:
    def __init__(self):
        pass

    def generate_sql(self, user_query: str):
        prompt = f"""
        You are an AI financial data analyst. Convert the following natural language query
        into a clean SQL instruction that will be run on a table named 't'.

        Query: "{user_query}"

        Only output SQL, nothing else.
        """

        sql = llm.generate(prompt)
        return sql.strip()

    def run(self, query_text: str):
        sql = self.generate_sql(query_text)
        df = run_data_query(query_text, sql)

        return {
            "output": df.to_dict(orient="records"),
            "metadata": {
                "sql_used": sql,
                "rows": len(df)
            }
        }

analytics_agent = AnalyticsAgent()
