from playwright.sync_api import sync_playwright

import time

def classify(prompt):
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        page = browser.contexts[0].pages[0]

        if 'chat.openai.com' not in page.url:
            page.goto('https://chat.openai.com/')

        page.wait_for_selector('textarea', state='visible', timeout=600000)
        page.fill('textarea', prompt)
        page.keyboard.press('Enter')

        page.wait_for_selector('.markdown.prose', timeout=100000000)  # انتظار ظهور الرد

        # الآن نراقب النص ليكون مستقر لمدة 2 ثانية (يعني انتهى من الكتابة)
        previous_text = ""
        stable_start = None
        while True:
            current_text = page.locator('.markdown.prose').last.inner_text()
            if current_text == previous_text:
                if stable_start is None:
                    stable_start = time.time()
                elif time.time() - stable_start >= 2:
                    break  # النص مستقر 2 ثانية => انتهى الرد
            else:
                stable_start = None
                previous_text = current_text
            time.sleep(0.5)  # ننتظر نصف ثانية قبل التحقق مجدداً

        return previous_text

