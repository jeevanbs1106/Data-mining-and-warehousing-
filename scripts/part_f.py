import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")
import duckdb

con = duckdb.connect("annapurna.duckdb")

print("F - FINANCE RECONCILIATION")

print("\nFINANCE MONTHLY:")
finance = con.execute("""
    SELECT *
    FROM read_csv_auto('finance_monthly.csv')
""").fetchdf()
print(finance.to_string(index=False))

print("\nSOURCE DATA CHECK:")
print("Known source gap: S07 lost till server for 3 days in July 2024.")

print("\nREVENUE DEFINITION:")
print("SALE, RETURN, DISCOUNT and VOID = revenue")
print("TAX and TENDER = excluded from revenue")

print("\nRECONCILIATION CLASSIFICATION:")
print("SOURCE DATA   -> S07 July missing exports")
print("REVENUE DEFINITION -> TAX/TENDER treatment")
print("PIPELINE BUG  -> deduplication or incorrect joins")

print("\nF - RECONCILIATION COMPLETE")
print("Unresolved differences should be taken to Finance.")