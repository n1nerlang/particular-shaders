import os
import json
import shutil

def process_assets(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".png") and not file.endswith("_mer.png") and not file.endswith("_normal.png"):
                base_name = os.path.splitext(file)[0]
                color_path = os.path.join(root, file)
                mer_file = f"{base_name}_mer.png"
                mer_path = os.path.join(root, mer_file)

                # Relative path from dest_dir
                rel_root = os.path.relpath(root, src_dir)
                out_root = os.path.join(dest_dir, rel_root)
                if not os.path.exists(out_root):
                    os.makedirs(out_root)

                shutil.copy2(color_path, os.path.join(out_root, file))

                texture_set = {
                    "format_version": "1.16.100",
                    "minecraft:texture_set": {
                        "color": base_name
                    }
                }

                if os.path.exists(mer_path):
                    shutil.copy2(mer_path, os.path.join(out_root, mer_file))
                    texture_set["minecraft:texture_set"]["metalness_emissive_roughness"] = f"{base_name}_mer"

                with open(os.path.join(out_root, f"{base_name}.texture_set.json"), 'w') as f:
                    json.dump(texture_set, f, indent=4)

                print(f"Processed: {base_name}")

if __name__ == "__main__":
    process_assets("src_assets/textures/blocks", "textures/blocks")
