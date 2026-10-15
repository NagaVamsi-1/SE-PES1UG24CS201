\# Lab 5: Static Code Analysis — Reflection



\### 1. What is static code analysis, and why is it useful?



Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, and coding-style violations early, improving code quality and maintainability.



\### 2. What issues did you identify and fix?



I identified SQL injection risk caused by string-based SQL construction, unsafe use of `eval()`, broad exception handling, missing documentation, inconsistent function naming, an unused variable, inconsistent return values, and formatting issues. I used parameterized SQL queries, removed `eval()`, handled database errors specifically, and improved documentation and formatting.



\### 3. What did Pylint, Bandit, and Flake8 contribute?



Pylint helped identify code-quality and maintainability issues. Bandit detected potentially insecure coding patterns. Flake8 identified formatting and style violations. Using all three tools provided complementary checks.



\### 4. What did you learn from this lab?



I learned that code can execute successfully and still contain security, quality, and style problems. After fixing the issues, my program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 produced no output. This demonstrated how static analysis helps improve Python code.



