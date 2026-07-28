# import sqlglot

# compiled_sql="""
#     SELECT
#         BRGEW,
#         GEWEI,
#         ANSWT,
#         WAERS,
#         ANSDT,
#         HERST,
#         HERLD,
#         BAUJJ,
#         BAUMM,
#         TYPBZ,
#         EMATN,
#         SERGE,
#         HANDLE,
#         TSEGTP,
#         FLLB_DUTY,
#         FLLB_HIDE,
#         IFLOT_SRTYPE,
#         IFLOT_SNTYPE,
#         KORTEX_FILE_PATH_NM,
#         KORTEX_FILE_TS,
#         KORTEX_UPLD_TS :: TIMESTAMP_NTZ AS KORTEX_UPLD_TS,
#         KORTEX_DPRCT_TS :: TIMESTAMP_NTZ AS KORTEX_DPRCT_TS,
#         SRC_NM
#     FROM source
# """
# spark_sql = sqlglot.transpile(compiled_sql, read="snowflake", write="spark")

# print(f"spark query: {spark_sql}")
# tree=sqlglot.parse(compiled_sql)
# print(tree)

# import sqlglot
# from sqlglot import exp

# tree = sqlglot.parse_one("SELECT * FROM a JOIN b ON a.id = b.id")
# tables = [t.name for t in tree.find_all(exp.Table)]
# # ['a', 'b']
# print(f"tables: {tables}")
# import sqlglot
# from sqlglot import exp

# def convert_view(snowflake_sql: str, target_dialect: str = "athena") -> str:
#     tree = sqlglot.parse_one(snowflake_sql, read="snowflake")

#     # Find the view identifier being created and add the vw_ prefix
#     create_expr = tree.find(exp.Create)
#     if create_expr and create_expr.this:
#         table_expr = create_expr.this
#         if isinstance(table_expr, exp.Table):
#             ident = table_expr.this  # exp.Identifier
#             if not ident.name.lower().startswith("vw_"):
#                 ident.set("this", f"vw_{ident.name}")

#     return tree.sql(dialect=target_dialect, pretty=True)


# snowflake_view = """
# CREATE OR REPLACE VIEW sales.customer_orders AS
# SELECT
#     c.customer_id,
#     c.name,
#     DATEADD(day, -30, CURRENT_DATE()) AS lookback_date,
#     COUNT(o.order_id) AS order_count
# FROM sales.customers c
# JOIN sales.orders o ON c.customer_id = o.customer_id
# QUALIFY ROW_NUMBER() OVER (PARTITION BY c.customer_id ORDER BY o.order_date DESC) = 1
# """

# print(convert_view(snowflake_view))

from pathlib import Path
import sqlglot
import sys
input_dir = Path(sys.argv[1])
output_dir = Path("models/example/spark")
output_dir.mkdir(parents=True, exist_ok=True)


for sql_file in input_dir.glob("*.sql"):
    sql = sql_file.read_text(encoding="utf-8")

    try:
        converted = sqlglot.transpile(
            sql,
            read="snowflake",
            write="spark"
        )[0]

        (output_dir / sql_file.name).write_text(
            converted,
            encoding="utf-8"
        )

        print(f"Converted {sql_file.name}")

    except Exception as e:
        print(f"Failed: {sql_file.name}: {e}")
