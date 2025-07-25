#  Login Test Automation using Selenium

This project automates UI testing of a login page using **Python** and **Selenium WebDriver**. It runs positive and negative login scenarios on a sample website to validate functionality.

---

  Website Under Test

🔗 [https://practicetestautomation.com/practice-test-login/](https://practicetestautomation.com/practice-test-login/)

---

  Test Cases Covered

 ✅ 1. Positive Login Test
- **Username:** `student`
- **Password:** `Password123`
- **Expected:** Redirect to success page and show “Logged In Successfully”.

 ❌ 2. Invalid Username Test
- **Username:** `incorrectUser`
- **Password:** `Password123`
- **Expected:** Show error message “Your username is invalid!”.

 ❌ 3. Invalid Password Test
- **Username:** `student`
- **Password:** `incorrectPassword`
- **Expected:** Show error message “Your password is invalid!”.

---

 Technologies Used

- Python
- Selenium
- WebDriverWait
- ChromeDriver

---

 How to Run

### 1. Install Selenium
```bash
pip install selenium
