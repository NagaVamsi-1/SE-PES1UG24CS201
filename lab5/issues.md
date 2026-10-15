\# Lab 5: Static Code Analysis — Issue Report



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---:|---|---|

| SQL injection risk | Security — Medium | 8 | SQL query is constructed using an f-string with user-provided values. | Use parameterized SQL queries. |

| Unsafe eval | Security — Medium | 14 | `eval()` evaluates an expression supplied as a string. | Accept a numeric salary limit instead of evaluating a string. |

| Silent exception handling | Security / Reliability — Low | 27–29 | A broad exception is caught and ignored, hiding failures. | Catch specific SQLite errors and report them. |

| Missing documentation | Code quality | 1, 7, 12, 24, 31, 38 | The module and functions lack docstrings. | Add module and function docstrings. |

| Non-standard function names | Code quality | 7, 24, 31, 38 | Functions use camelCase rather than snake\_case. | Rename functions using snake\_case. |

| Unused variable | Code quality | 15 | `total\_seen` is assigned but never used. | Remove the unused variable. |

| Inconsistent return | Code quality | 12–21 | `shortlist()` can return a list or implicitly return `None`. | Always return a list. |

| Unsafe SQL construction | Security | 8 | User-provided values are inserted directly into SQL. | Bind values using SQL placeholders. |

| File resource handling | Code quality | 32–35 | The report file is opened without an encoding or context manager. | Use `with open()` and specify UTF-8 encoding. |

| Formatting violations | Style | 4, 8, 13, 15, 26, 31, 39 | Long lines, trailing whitespace, and spacing violations were reported. | Format the code to satisfy Flake8. |





