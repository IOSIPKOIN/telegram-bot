from playwright.async_api import async_playwright
from pathlib import Path

BASE_DIR = Path(__file__).parent
TEMPLATES = BASE_DIR / "templates"
IMAGES = BASE_DIR / "images"
IMAGES.mkdir(exist_ok=True)

async def render_html(template: str, output: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            args=["--no-sandbox"]
        )

        page = await browser.new_page(
            viewport={"width": 390, "height": 844}
        )

        html_path = TEMPLATES / template
        await page.goto(f"file://{html_path}")
        await page.wait_for_timeout(700)

        output_path = IMAGES / output
        await page.screenshot(path=output_path, full_page=True)

        await browser.close()
        return str(output_path)
