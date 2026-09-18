import duckdb

con = duckdb.connect("annapurna.duckdb")

con.execute("""
CREATE OR REPLACE TABLE dim_date AS
SELECT
    CAST(strftime(d, '%Y%m%d') AS INTEGER) AS date_sk,
    d AS calendar_date,
    strftime(d, '%A') AS day_of_week,
    CAST(strftime(d, '%m') AS INTEGER) AS month,
    CAST(strftime(d, '%Y') AS INTEGER) AS year
FROM generate_series(
    DATE '2024-01-01',
    DATE '2024-12-31',
    INTERVAL 1 DAY
) AS t(d);
""")

con.execute("""
CREATE OR REPLACE TABLE dim_store AS
SELECT DISTINCT
    store_id,
    store_id AS store_sk
FROM read_csv_auto('sales_landed/store=*/month=*/*.csv',
    union_by_name=true,
    filename=true);
""")

con.execute("""
CREATE OR REPLACE TABLE dim_category (
    category_sk INTEGER,
    category_name VARCHAR
);
""")

con.execute("""
CREATE OR REPLACE TABLE dim_product (
    product_sk VARCHAR,
    product_code VARCHAR,
    product_name VARCHAR,
    category_sk INTEGER,
    valid_from DATE,
    valid_to DATE
);
""")

con.execute("""
CREATE OR REPLACE TABLE fact_sales (
    bill_no VARCHAR,
    line_no INTEGER,
    store_sk VARCHAR,
    product_sk VARCHAR,
    date_sk INTEGER,
    qty DOUBLE,
    unit_price DOUBLE,
    revenue DOUBLE
);
""")

print("C - STAR SCHEMA CREATED")
print("TABLES:")
print("dim_store")
print("dim_product")
print("dim_category")
print("dim_date")
print("fact_sales")
print("Product identity: product_code + sale date")
print("Revenue excludes TAX and TENDER")
print("Revenue includes SALE, RETURN, DISCOUNT and VOID")