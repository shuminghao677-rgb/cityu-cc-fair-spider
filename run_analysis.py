"""
STEM Fair 2026 数据分析 - 一键运行
依次执行：学历分析 → 技术栈分析 → 合并仪表盘 JSON
"""
import os
import json
import subprocess
import sys

def run_script(name, path):
    print(f"\n{'='*50}")
    print(f"▶ 运行: {name}")
    print('='*50)
    result = subprocess.run(
        [sys.executable, path],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        capture_output=False,
    )
    if result.returncode != 0:
        print(f"错误: {name} 执行失败")
        sys.exit(1)

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base)

    # 1. 学历分析
    run_script("学历分析 (departure_analysis.py)", "departure_analysis.py")

    # 2. 技术栈分析
    run_script("技术栈分析 (techinical_analysis.py)", "techinical_analysis.py")

    # 3. 合并为统一仪表盘 JSON（供 v0 一次性加载）
    os.makedirs("output/dashboard", exist_ok=True)
    dashboard = {}
    for fname in ["education_analysis.json", "technical_analysis.json"]:
        path = f"output/dashboard/{fname}"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                dashboard.update(data)
    out_path = "output/dashboard/dashboard_data.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(dashboard, f, ensure_ascii=False, indent=2)
    print(f"\n✓ 已合并仪表盘数据: {out_path}")

    # 生成可离线打开的仪表盘 HTML
    import generate_dashboard
    generate_dashboard.main()

    print("\n" + "="*50)
    print("全部分析完成！")
    print("  - Excel: output/excel/")
    print("  - JSON:  output/dashboard/")
    print("  - 仪表盘入口: output/dashboard/dashboard_data.json")
    print("="*50)

if __name__ == "__main__":
    main()
