import duckdb

con = duckdb.connect("annapurna.duckdb")

con.execute("INSTALL postgres;")
con.execute("LOAD postgres;")

con.execute("""
ATTACH 'host=localhost port=5432 dbname=annapurna user=postgres password=postgres'
AS pg (TYPE POSTGRES, READ_ONLY);
""")

result = con.execute("""
EXPLAIN
SELECT
    s.store_id,
    SUM(f.revenue) AS revenue
FROM read_parquet(
    'sales_landed/store=*/month=*/*.parquet',
    hive_partitioning=true
) f
JOIN pg.public.stores s
    ON f.store_id = s.store_id
GROUP BY s.store_id;
""").fetchall()

print("E - CROSS-SYSTEM QUERY")
print("Object store: sales Parquet")
print("Relational system: PostgreSQL")
print("Join performed by analytical engine: DuckDB")
print("No data copied between systems")
print("EXPLAIN PLAN:")
for row in result:
    print(row[1])