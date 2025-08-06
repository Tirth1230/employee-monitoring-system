```markdown
# 🖥️ Employee Monitoring System

A background user activity monitoring system built using **Python** and **Django** that captures random screenshots of logged-in users, organizes them securely, and provides an admin interface for review and management.

---

## 🚀 Features

- 🎯 Captures screen at **random intervals**
- 🖼️ Watermarks screenshots with **timestamp and username**
- 🗂️ Saves data in **user-specific hidden folders**
- 📥 Admin panel to:
  - View logs
  - Filter by user and date
  - Preview screenshots
  - Download/Delete images
- 📩 Sends **email alerts** if screenshot capture is interrupted
- 🧠 Uses background scripts integrated with a Django backend

---

## 🛠️ Tech Stack

- **Python 3**
- **Django 4**
- **PyAutoGUI** – for screen capture
- **OpenCV** – image processing (optional compression)
- **SQLite** / MySQL (configurable)
- **SMTP (email)** – for admin notifications

---

## 🗂️ Project Structure
```
employee-monitoring-system/
├── background_script/ # Screenshot capture logic
│ └── screenshot_capture.py
├── admin_panel/ # Django project & admin UI
│ ├── manage.py
│ ├── admin_panel/ # Django settings
│ └── monitoring/ # Django app
├── media/ # Screenshot storage (auto-created)
├── requirements.txt
├── .gitignore
└── README.md

```

---

## ⚙️ Installation

```bash
git clone https://github.com/Tirth1230/employee-monitoring-system.git
cd employee-monitoring-system
pip install -r requirements.txt
```

---

## 📦 Usage

1. Run the **Django server** from `admin_panel`:

   ```bash
   cd admin_panel
   python manage.py runserver
   ```

2. Run the **background screenshot script**:

   ```bash
   cd background_script
   python screenshot_capture.py
   ```

3. Visit the **admin panel** in your browser:

   ```
   http://localhost:8000/
   ```

---

## 🔐 Admin Panel Login

> Create a superuser if you haven’t:

```bash
python manage.py createsuperuser
```

---

## 📧 Email Alert Setup

Make sure to configure your SMTP details in the background script to enable email alerts in case of script interruptions.

---

## 🏁 Status

✅ **In Progress**
More features like screen recording and keyword detection coming soon!

---

## 👨‍💻 Author

**Tirth Belsare**
📧 [tirthbelsare6@gmail.com](mailto:tirthbelsare6@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/tirth1305) | [GitHub](https://github.com/Tirth1230)

---

## 📄 License

This project is licensed under the MIT License.

```
