import duckdb

con = duckdb.connect("annapurna.duckdb")

con.execute("""
CREATE OR REPLACE VIEW sales_with_historical_price AS
SELECT
    f.bill_no,
    f.line_no,
    f.product_sk,
    f.qty,
    f.date_sk,
    p.product_code,
    p.product_name,
    pr.unit_price AS historical_price,
    pr.effective_from,
    pr.effective_to
FROM fact_sales f
JOIN dim_product p
    ON f.product_sk = p.product_sk
JOIN price_revisions pr
    ON p.product_sk = pr.product_sk
   AND CAST(
        strptime(CAST(f.date_sk AS VARCHAR), '%Y%m%d')
       AS DATE
   ) >= pr.effective_from
   AND CAST(
        strptime(CAST(f.date_sk AS VARCHAR), '%Y%m%d')
       AS DATE
   ) < COALESCE(pr.effective_to, DATE '9999-12-31');
""")

print("D - HISTORICAL PRICE VIEW CREATED")
print("Price source: price_revisions")
print("Price matched using product_sk + effective dates")
print("March 2024 uses March-effective prices")
print("Same query works for any report period")