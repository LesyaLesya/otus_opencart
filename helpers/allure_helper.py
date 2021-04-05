"""Модуль c вспомогательными методами для allure."""

import allure


def attach(browser):
    return allure.attach(
            body=browser.get_screenshot_as_png(),
            name="screenshot_image",
            attachment_type=allure.attachment_type.PNG)


def add_allure_env(browser_name, browser_version, local):
    with open("allure-results/environment.xml", "w+") as file:
        file.write(f"""<environment>
            <parameter>
                <key>Browser.Name</key>
                <value>{browser_name}</value>
            </parameter>
            <parameter>
                <key>Browser.Version</key>
                <value>{browser_version}</value>
            </parameter>
            <parameter>
                <key>Local</key>
                <value>{local}</value>
            </parameter>
        </environment>
        """)
