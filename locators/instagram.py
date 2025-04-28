from appium.webdriver.common.appiumby import AppiumBy


instagram_icon = (AppiumBy.ID,'com.sec.android.app.launcher:id/iconview_imageView' )
username_input_field = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
password_input_field = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
login_button = (AppiumBy.XPATH,'//android.widget.Button[@content-desc="Log in"]/android.view.ViewGroup')
log_in_error_message = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Unable to log in")')
log_in_error_description = (AppiumBy.ID,'android:id/message')
log_in_error_ok_button = (AppiumBy.ID,'android:id/button1')
log_in_error_pop_up = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout')