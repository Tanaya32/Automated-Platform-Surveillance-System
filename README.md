# 🖥️ Automated Platform Surveillance System (Python)

This project is a **Automated Platform Surveillance System ** built using Python.
It captures system performance and process details and stores them in log files.

---

## 🚀 Features

### 🔹 Basic Version

* Displays running processes
* Shows:

  * Process ID (PID)
  * Process Name
  * Status

### 🔹 Advanced Version

* Generates automated log files
* Captures:

  * CPU usage
  * RAM usage
  * Disk usage
  * Network usage
* Stores detailed process info:

  * PID
  * Name
  * Username
  * Status
  * Start Time
  * CPU %
  * Memory %

---

## 🛠️ Technologies Used

* Python
* psutil
* os
* sys
* time
* schedule

---

## 📂 Project Structure

System-Monitoring-Tool/
│── basic_version/
│── advanced_version/
│── sample_logs/
│── README.md

---

## ▶️ How to Run

### Basic Version

```bash
python System_monitor_basic.py
```

### Advanced Version

```bash
python System_monitor_Advanced.py 5 Logs
```

* `5` → Time interval (minutes)
* `Logs` → Folder name for log files

---

## 📌 Example Output

* CPU Usage: 35%
* RAM Usage: 60%
* Disk Usage: C Drive → 40%
* Process List with detailed metrics

---

## 📈 Learning Outcome

This project demonstrates:

* System monitoring using Python
* Working with OS-level processes
* File handling and logging
* Automation using scheduling
* Code evolution from basic to advanced implementation

---

## 👩‍💻 Author

**Tanaya Vikram Gokhale**
