import os

source_dir = r"C:\Users\nay\.claude\skills\wq-alpha-assistant\references\data_fields_txt"
target_dir = r"C:\Users\nay\.claude\skills\wq-alpha-assistant\references\fields_simple"

for universe in ["TOP3000", "TOP1000", "TOP200", "TOP500", "TOPSP500"]:
    src_path = os.path.join(source_dir, universe)
    tgt_path = os.path.join(target_dir, universe)
    os.makedirs(tgt_path, exist_ok=True)

    for f in os.listdir(src_path):
        if f.endswith(".txt"):
            src_file = os.path.join(src_path, f)
            simple_name = f.replace(f"{universe}_", "")
            tgt_file = os.path.join(tgt_path, simple_name)

            with open(src_file, "r", encoding="utf-8") as fin:
                with open(tgt_file, "w", encoding="utf-8") as fout:
                    for line in fin:
                        parts = line.split("\t")
                        if len(parts) >= 1:
                            fout.write(f"{parts[0]}\n")  # 只保留字段名
            print(f"Created: {tgt_file}")

print("Done!")
