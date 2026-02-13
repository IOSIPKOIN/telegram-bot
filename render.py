from playwright.async_api import async_playwright
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).parent
TEMPLATES = BASE_DIR / "templates"
IMAGES = BASE_DIR / "images"
IMAGES.mkdir(exist_ok=True)

# Jinja environment
env = Environment(loader=FileSystemLoader(TEMPLATES))


async def render_html(template: str, output: str, **context) -> str:
    # 1️⃣ Рендерим HTML с переменными
    template_obj = env.get_template(template)
    rendered_html = template_obj.render(**context)

    temp_html_path = TEMPLATES / "_temp_rendered.html"
    temp_html_path.write_text(rendered_html, encoding="utf-8")

    # 2️⃣ Делаем скрин
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox"])
        page = await browser.new_page(viewport={"width": 390, "height": 844})

        await page.goto(f"file://{temp_html_path}")
        await page.wait_for_timeout(700)

        output_path = IMAGES / output
        await page.screenshot(path=output_path, full_page=True)

        await browser.close()

    temp_html_path.unlink(missing_ok=True)

    return str(output_path)
