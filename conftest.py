# conftest.py

import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        # =====================================================
        # Launch Persistent Browser
        # =====================================================
        # Benefits:
        # - Keep login session
        # - Keep cookies
        # - Keep local storage
        # - Keep permission allow
        # - Faster rerun
        # =====================================================

        context = p.chromium.launch_persistent_context(

            # Folder lưu session browser
            user_data_dir="user_data",

            # Always open browser
            headless=False,

            # Run slower for easier debugging
            slow_mo=300,

            # Open full screen
            no_viewport=True,

            # Browser args
            args=[
                "--start-maximized"
            ]
        )

        # =====================================================
        # Grant Permissions
        # =====================================================
        # Avoid popup:
        # "Access other apps and services on this device"
        # =====================================================

        context.grant_permissions(

            permissions=[
                "notifications"
            ],

            origin="https://pos.swiftpos.us"
        )

        # =====================================================
        # Create Page
        # =====================================================

        page = context.new_page()

        # =====================================================
        # Default Timeout
        # =====================================================

        page.set_default_timeout(30000)

        # =====================================================
        # Start Test
        # =====================================================

        yield page

        # =====================================================
        # End Test
        # =====================================================

        context.close()