#!/usr/bin/env python3
"""Kiểm thử khói (smoke test) ngoại tuyến bằng Chromium cho trình khám phá 5 dự án phân tích.

Kiểm tra hành vi tương tác, điều hướng bàn phím, giao diện di động và lỗi JavaScript khi chạy.
Đây không phải là chứng nhận khả năng tiếp cận hay kiểm thử BI gốc.
"""
from __future__ import annotations

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo" / "analytics-explorer.html"
REPORTS = ROOT / "reports"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    REPORTS.mkdir(exist_ok=True)
    errors: list[str] = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        page.route("http://**/*", lambda route: route.abort())
        page.route("https://**/*", lambda route: route.abort())
        page.goto(DEMO.as_uri(), wait_until="load")
        check(page.title().startswith("Analytics Explorer"), "Thiếu tiêu đề dashboard")
        check(page.locator("#project option").count() == 5, "Phải hiển thị đủ 5 dự án")
        check(page.locator("#bars .bar-row").count() == 5, "Thiếu các thanh mặc định của SaaS")
        page.screenshot(path=str(REPORTS / "analytics-desktop.png"), full_page=True)
        page.select_option("#project", "1")
        check(page.locator("#metric option").count() >= 2, "Chuyển đổi chỉ số A/B test thất bại")
        check(page.locator("#bars .bar-row").count() == 2, "Số dòng thử nghiệm A/B không đúng")
        page.fill("#search", "UNMATCHED-SMOKE-SEARCH")
        check(page.get_by_text("Không tìm thấy kết quả nào phù hợp.").count() == 1,
              "Thiếu thông báo trạng thái rỗng")
        page.fill("#search", "")
        page.select_option("#project", "2")
        page.select_option("#limit", "all")
        check(page.locator("#bars .bar-row").count() == 10, "Số dòng Ecommerce chưa đủ")
        page.locator("#project").focus()
        page.keyboard.press("Tab")
        check(page.evaluate("document.activeElement.id") == "metric",
              "Điều hướng phím Tab giữa các bộ lọc thất bại")
        page.set_viewport_size({"width": 390, "height": 844})
        page.screenshot(path=str(REPORTS / "analytics-mobile.png"), full_page=True)
        overflowing = page.evaluate(
            "document.documentElement.scrollWidth > window.innerWidth + 2"
        )
        check(not overflowing, "Tràn ngang trên giao diện di động")
        check(not errors, "Có lỗi runtime: " + "; ".join(errors))
        browser.close()
    print("PASS: Biểu đồ mặc định, chuyển đổi, bộ lọc, bàn phím, giao diện mobile, không có lỗi JS")


if __name__ == "__main__":
    main()
