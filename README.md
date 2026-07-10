# ⚡ DESCO Balance Alert

A Python automation project that monitors DESCO prepaid electricity meter balance and sends alerts when the balance falls below a specified threshold.

The project runs automatically using **GitHub Actions**, allowing users to receive low-balance notifications without keeping their computer running.

---

## 🚀 Features

- 🔍 Automatically checks DESCO prepaid meter balance
- ⚠️ Sends low balance alerts
- ⏰ Scheduled execution using GitHub Actions (Cron Job)
- 🐍 Written in Python
- 📦 Easy dependency management with `requirements.txt`
- ☁️ Runs entirely on GitHub (No local PC required)

---

## 📂 Project Structure

```
desco-balance-alert/
│
├── .github/
│   └── workflows/
│       └── desco.yml          # GitHub Actions Workflow
│
├── desco_check.py             # Main Python Script
├── requirements.txt           # Python Dependencies
└── README.md
```

---

## 🛠 Requirements

- Python 3.10+
- pip

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
python desco_check.py
```

---

## ⚙️ GitHub Actions

This project is configured to run automatically using GitHub Actions.

Workflow location:

```
.github/workflows/desco.yml
```

The workflow will:

1. Set up Python
2. Install dependencies
3. Execute the monitoring script
4. Send notifications if the balance is below the configured threshold

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/Rabbi1067/desco-balance-alert.git
```

Go to the project directory

```bash
cd desco-balance-alert
```

Install required packages

```bash
pip install -r requirements.txt
```

Run

```bash
python desco_check.py
```

---

## 🔧 Configuration

Configure your required credentials or environment variables before running the project.

Examples may include:

- DESCO Account Information
- Meter Number
- Notification Settings
- API Tokens (if applicable)

Store sensitive information using **GitHub Secrets** instead of hardcoding them.

---

## 📋 Dependencies

Dependencies are listed in

```
requirements.txt
```

Install them using

```bash
pip install -r requirements.txt
```

---

## 📈 Future Improvements

- Email Notifications
- Telegram Bot Alerts
- SMS Notifications
- Multiple Meter Support
- Web Dashboard
- Logging System
- Balance History
- Monthly Usage Report

---

## 👨‍💻 Author

**Fazle Rabbi**

GitHub: https://github.com/Rabbi1067

---

## 📄 License

This project is licensed under the MIT License.
