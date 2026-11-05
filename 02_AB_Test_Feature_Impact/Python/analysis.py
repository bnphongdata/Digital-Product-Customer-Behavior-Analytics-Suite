"""Chạy quy trình phân tích SQL/Python thực tế của dự án này từ bất kỳ thư mục làm việc nào."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from portfolio.run import run_project
if __name__=='__main__':
    print(run_project(ROOT,Path(__file__).resolve().parents[1].name))
