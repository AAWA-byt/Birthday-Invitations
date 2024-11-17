# 🎉 Birthday Invitation App

Welcome to the **Birthday Invitation App**! 🥳 This project provides a web application to create, manage, and view personalized birthday event invitations. 
Built with Flask, SQLAlchemy, and Flask-Login, this app makes managing event invitations simple and efficient.
I developed this little app for my birthday. It's not perfect and there are bound to be a few mistakes here and there. Feel free to open an issue if you find any errors.

---

## ✨ Features

- 🔒 **User Authentication**: Secure login system for managing invitations.
- 🎁 **Invitation Management**: Create, view, and delete event invitations from a user-friendly dashboard.
- 📧 **Unique Invitation Links**: Generate unique, shareable invitation links.
- 🗺️ **Event Details**: Include Google Maps links for event locations.
- 📱 **Reponsive Design**: The app can be used to its full extent with your mobile phone

---

## 🚀 Tech Stack

- **Flask**: Web framework.
- **Flask-SQLAlchemy**: Database integration.
- **Flask-Login**: User session management.
- **MySQL**: Database backend.
- **Docker**: Containerization for seamless deployment.

---

## 🛠️ Installation Guide

Follow these steps to get started:

### Prerequisites

1. 🐍 Install Python (>= 3.8).
2. 🐋 Install Docker and Docker Compose.
3. 📂 Clone this repository:
   
   ```bash
   git clone https://github.com/AAWA-byt/Birthday-Invitations
   cd birthday-invitation-app
5. ⚙️ Configure the app
   
   ```bash
   cd app
   nano example.env
   cp example.env .env
7. 🎉 Return to root directory of the app and launch the app
   
   ```bash
   cd ..
   docker-compose up -d --build
8. 💻 Visit the app at ``your_domain_or_ip_adress:2683``

### Language

The language of the invitation page is german. If you want to change it just go to ``app/templates/invitation.html`` and change the text to your liking.

---

## 🖼️ Preview 

Here are few screenshots of the app:

### Login page

![login_page](https://github.com/user-attachments/assets/05622c5a-8084-4fe0-aa75-650508807710)

### Dashboard page

![dashboard_page](https://github.com/user-attachments/assets/c49be8a4-bc21-4b93-9471-b496a2d79be5)

### Invitation page

![firstpage_invitation](https://github.com/user-attachments/assets/93f6b034-f9e2-49bb-b46a-e2708120a848)

Credits to: [https://codepen.io/euro__bby/pen/ExBwNNN](https://codepen.io/euro__bby/pen/ExBwNNN)

![secondpage_invitation](https://github.com/user-attachments/assets/20f2512b-1502-486d-a545-e95b630d981c)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/AAWA-byt/Birthday-Invitations/LICENSE) file for details.

---

## 🌟 Star the repository if you like it! ⭐
