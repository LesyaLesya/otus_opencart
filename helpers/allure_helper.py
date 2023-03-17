"""Модуль c вспомогательными методами для allure."""

import allure
import json


def attach(browser):
    return allure.attach(
            body=browser.get_screenshot_as_png(),
            name="screenshot_image",
            attachment_type=allure.attachment_type.PNG)


def attach_capabilities(browser):
    return allure.attach(
            body=browser.session_id,
            name=json.dumps(browser.desired_capabilities),
            attachment_type=allure.attachment_type.JSON)


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
