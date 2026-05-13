class QuickSaleLocator:

    QUICK_SALE_PANEL = "#quick-sale-scale-size"

    SALON_CENTER_BUTTON = "#side-bar-append-thumbtack .salon-center"

    QUICK_SALE_BUTTON = "#side-bar-append-thumbtack .quick-sale"

    TECH_CARD = 'div:nth-child(3) > .tech-card_text'

    MANICURE_BUTTON = 'button:has-text("manicure")'

    SERVICE_BUTTON = 'button:has-text("GEL - SWEET ESCAPE")'

    CONTINUE_BUTTON = 'text=Continue'

    DISCOUNT_BUTTON = 'button:has-text("Discount $")'

    BILL_DISCOUNT_BUTTON = '//*[@id="quick-sale-scale-size"]/div/div[2]/payment/div[2]/button[2]'

    DISCOUNT_PERCENTAGE_BUTTON = '.select-discount_btn[data-type="percent"]'

    ADD_DISCOUNT_BUTTON = '//*[@id="discount-item_label"]/div[6]/button[2]'

    TIP_BUTTON = 'button:has-text("Tips $")'

    TIPS_MANAGEMENT_PANEL = 'div:has-text("Tips Management")'

    TIPS_SAVE_BUTTON = '//*[@id="quick-sale-scale-size"]/div/div[2]/splittip/div/div/div[1]/div[2]/div[2]/div'

    TIPS_SAVE_BUTTON_FALLBACK = ".btn-save-label-tip"

    ADD_BUTTON = 'button:has-text("Add")'

    SAVE_BUTTON = "#btn-qsSave"

    FULL_CASH_BUTTON = 'payment button.quickCharge-btn[data-payment="cash"]:visible'

    FULL_CASH_ACTIVE_BUTTON = 'payment button.quickCharge-btn[data-payment="cash"].active:visible'

    CHARGE_BUTTON = '//*[@id="quick-sale-scale-size"]/div/div[2]/payment/div[3]/div[2]/div[1]/div/button/span'

    CLOSE_BILL_BUTTON_AT_RECEPT = 'button#cmdReceipt.btn-exit-receipt:has-text("CLOSE BILL")'
