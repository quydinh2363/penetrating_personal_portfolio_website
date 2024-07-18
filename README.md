# Penetrating personal portfolio website

This repository contains the source code for my designing of personal portfolio website. 
- Link for my webstie: https://portfolio-website-ten-sigma-22.vercel.app/
- usename: admin 
- password: 123

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [SQL Injection Vulnerability](#sql-injection-vulnerability)
  - [Discovery](#discovery)
  - [Exploitation](#exploitation)
  - [Mitigation](#mitigation)
- [Lessons Learned](#lessons-learned)
- [Reference](#reference)

## Introduction

This project showcases my personal portfolio website which I developed to demonstrate my skills and projects. During development, I performed a security assessment and discovered an SQL Injection vulnerability, which I then successfully mitigated.

## Technologies Used

- HTML
- CSS
- JavaScript
- Python (Flask) or your back-end framework
- SQLite (or your database of choice).

## SQL Injection Vulnerability

### Discovery

During the security assessment, I identified an SQL Injection vulnerability in the login functionality. Deliberately,I leave the `login input` not clean and correct, allowing attackers to inject malicious SQL code.
For example, `admin'-- or 1=1`

<div <div align="center">
    <img src="https://github.com/quydinh2363/penetrating_personal_portfolio_website/blob/main/images/loginpage.png" alt="Centered Image">
</div>

### Exploitation

For more details
You can find in the <a href="https://github.com/quydinh2363/bypass_login_web/tree/main/images">images folder</a>.


### Mitigation

To mitigate this vulnerability, I implemented prepared statements and parameterized queries below. This ensures that user input is properly sanitized and prevents SQL Injection attacks.

**Before Mitigation:**
```python
query = f"SELECT username FROM userData WHERE username = '{username}' and password ='{password}'"
cur.execute(query)
```
**After Mitigation:**
```python
query = "SELECT username FROM users WHERE username = ? and password = ?"
cur.execute(query,(username,password))
```
## Lessons Learned
 - Importance of validating and sanitizing user inputs.
 - Implementation of secure coding practices to prevent common vulnerabilities like SQL Injection.
 - Hands-on experience in identifying and mitigating security issues in web applications.

## Reference

https://www.youtube.com/@ryan_phdsec
https://www.youtube.com/@codehal

![HobbyProject](https://img.shields.io/badge/version-1.0-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

© | 2024 quydinh2363


   




