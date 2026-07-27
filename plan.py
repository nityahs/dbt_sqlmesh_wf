import json
from pathlib import Path
import os
from sqlmesh.core.context import Context
from sqlmesh.core.lineage import lineage

project_dir = Path(__file__).resolve().parent
context = Context(paths=str(project_dir))

column_lineage = {}
dir = os.environ.get("DBT_PROFILES_DIR", profiles_dir or "")
path = Path(project_root, dir, cls.PROFILE_FILE)
for name, model in context.models.items():
    model_cols = {}
    for column in model.columns_to_types or {}:
        try:
            node = lineage(column, model)

            # Walk the node tree to pull out upstream source references
            def walk(n, depth=0):
                results = []
                for child in n.downstream:
                    results.append(str(child.name))
                    results.extend(walk(child, depth + 1))
                return results

            model_cols[column] = walk(node)
        except Exception as e:
            model_cols[column] = f"ERROR: {e}"
    column_lineage[name] = model_cols

with open(project_dir / "column_lineage.json", "w", encoding="utf-8") as f:
    json.dump(column_lineage, f, indent=2)
