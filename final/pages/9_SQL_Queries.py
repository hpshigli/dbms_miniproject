import streamlit as st
import pandas as pd
from db import run_query

st.header("📊 Advanced SQL: Joins, Aggregates, Nested Queries")

st.subheader("1️⃣ Assets with their Cloud Providers")
q1 = """
SELECT a.asset_id, a.name, a.type, ca.provider
FROM ASSET a
JOIN CLOUD_ACCOUNT ca ON a.account_id = ca.account_id;
"""
st.dataframe(pd.DataFrame(run_query(q1)))

st.subheader("2️⃣ Vulnerabilities per Severity")
q2 = """
SELECT severity, COUNT(*) AS total_vulns
FROM VULNERABILITY
GROUP BY severity;
"""
st.dataframe(pd.DataFrame(run_query(q2)))

st.subheader("3️⃣ Assets with more than 2 Exposures (nested query)")
q3 = """
SELECT a.asset_id, a.name, ecount.exposures
FROM (
    SELECT asset_id, COUNT(*) AS exposures
    FROM EXPOSURE
    GROUP BY asset_id
) ecount
JOIN ASSET a ON a.asset_id = ecount.asset_id
WHERE ecount.exposures > 2;
"""
st.dataframe(pd.DataFrame(run_query(q3)))
