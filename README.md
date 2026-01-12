☁️ Cloud Security Simulator (IAM-Based CLI)

A Python-based Cloud Security Simulator that mimics core cloud concepts such as IAM roles, EC2, S3, access policies, key rotation, and session-based access control.
This project is designed to demonstrate security-first cloud architecture thinking, not just basic scripting.
🚀 Project Overview
This project simulates a cloud environment through a CLI interface, where users authenticate and interact with cloud resources based on their assigned roles.
It focuses on:
Identity & Access Management (IAM)
Least Privilege principle
Secure credential handling
Clear separation between compute (EC2) and storage (S3)
The goal is learning + job readiness, not real cloud deployment.
--------------------------------------
👥 User Roles & Permissions
--------------------------------------
🔑 Admin
Create / delete EC2 instances
Create / delete S3 buckets
Create / delete users
View audit logs
Define per-resource policies
Enforce key rotation
---------------------------------------
👨‍💻 Developer
Create EC2 instances
Write & execute code inside EC2
Create S3 buckets
Write non-executable files only in S3
Cannot access logs
Subject to key rotation
--------------------------------------
🧪 Tester
Read-only access
View logs
Read test scripts
Navigate folders (policy-based)
❌ No write / no execute access
✔ Implements Least Privilege Access strictly.
--------------------------------------
🔐 Security Features
Password Hashing using SHA-256
Key Rotation Enforcement
Admin-defined rotation window (15–90 days)
Manual or automatic rotation
Session-Based Access
Infinite loop with explicit exit (logout)
Audit Logging
Timestamped access logs
Zero Trust Model
Missing or invalid policy = access denied
-------------------------------------
EC2 vs S3 Enforcement
Resource	Behavior
EC2 -	Code execution allowed (.py, .cpp)
S3 -	Execution blocked, only file storage
Policy - Enforced via policy.json
Each resource uses per-folder policies to clearly define allowed actions.
-------------------------------------
📂 Project Structure
Copy code

cloud-security-simulator/
│
├── cloud.py
├── db.json
├── polcy.json
├── logs.txt
│
├── EC2/
│   └── vm1/
│       └── policy.json
│
└── S3/
    └── bucket1/
        └── policy.json
-------------------------------------
📜 Policy Model
Each resource (EC2 / S3) contains its own policy.json, defining:
Allowed file types
Execution permissions
Access boundaries
This approach improves:
Clarity
Debugging
Security isolation
Future versions may centralize policies for large-scale environments.
-----------------------------------
⚠️ Known Limitations
This is a local simulator, not a real cloud service
Policies are file-based (not network-enforced)
No real virtualization or containers
Designed for learning and demonstration purposes
-----------------------------------
🔮 Future Improvements
Centralized policy engine
Session timeout / inactivity logout
Policy inheritance
Cloud SDK integration (AWS-style simulation)
Container-based EC2 simulation
----------------------------------
🧠 Key Learnings Demonstrated
IAM role design
Secure authentication flows
Access control enforcement
Cloud security mindset
CLI-based system design
-----------------------------------
🧑‍💻 Tech Stack
Python 3
JSON (policy & database)
Standard libraries (hashlib, secrets, subprocess, os)
-----------------------------------
📌 Author
Dipanshu
Cybersecurity | Cloud Security | Python
📍 India


