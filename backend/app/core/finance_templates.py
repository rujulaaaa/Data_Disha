TEMPLATES = {
    "spends_by_project_donor": """
        SELECT project, donor, SUM(amount) as total_spend
        FROM t
        WHERE quarter = '{quarter}' AND fiscal_year = '{fy}'
        GROUP BY project, donor;
    """,

    "total_donor_spend": """
        SELECT donor, SUM(amount) as total_spend
        FROM t
        GROUP BY donor;
    """,

    "project_summary": """
        SELECT project, SUM(amount) as total_spend, COUNT(*) as records
        FROM t
        GROUP BY project;
    """
}