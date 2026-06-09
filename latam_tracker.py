from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://www.latamairlines.com/co/es/ofertas-vuelos/?origin=SCL&outbound=2026-08-12&destination=ZCO&inbound=2026-08-15&adt=1&chd=0&inf=0&trip=RT&cabin=Economy&redemption=false&sort=RECOMMENDED",
        wait_until="networkidle",
        timeout=120000,
    )

    print("TITLE:", page.title())

    print("URL:", page.url)

    browser.close()
