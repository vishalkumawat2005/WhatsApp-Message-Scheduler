# WhatsApp-Message-Scheduler
This is automatic whatsapp-Message-Scheduler
# 📱 Automatic WhatsApp Scheduler Using Twilio

An automated WhatsApp messaging application that allows users to schedule messages for a specific date and time. The application uses the **Twilio WhatsApp API** to send messages automatically at the scheduled time.

## 🚀 Features

- 📩 Send WhatsApp messages using the Twilio API.
- ⏰ Schedule messages for a specific date and time.
- 🤖 Automatically send messages when the scheduled time arrives.
- 👤 Send messages to WhatsApp numbers in the required international format.
- 🔐 Securely manage Twilio credentials using environment variables.
- 📋 Manage scheduled messages and track their status.
- ⚠️ Handle errors and failed message deliveries.

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Twilio API** – WhatsApp messaging service
- **Python Scheduler** – For executing scheduled tasks
- **python-dotenv** – For managing environment variables
- **Git & GitHub** – Version control and project hosting

## 📂 Project Structure

```text
whatsapp-scheduler/
│
├── app.py                 # Main application
├── scheduler.py           # Message scheduling logic
├── requirements.txt       # Project dependencies
├── .env                   # Twilio credentials
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

*Note: Adjust the file structure according to your actual project files.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate to the project directory:

```bash
cd whatsapp-scheduler
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install the packages used by your application:

```bash
pip install twilio python-dotenv APScheduler
```

### 4. Configure Twilio

1. Create an account on [Twilio](https://www.twilio.com/).
2. Open the Twilio Console.
3. Configure the WhatsApp Sandbox or an approved WhatsApp sender.
4. Obtain your Account SID and Auth Token.
5. Configure your sender and recipient WhatsApp numbers.

### 5. Configure Environment Variables

Create a `.env` file in the root directory:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

Replace the example sender number with the WhatsApp sender configured in your Twilio account.

**Important:** Never upload your `.env` file or expose your Twilio Auth Token on GitHub.

### 6. Run the Application

Run the main Python application:

```bash
python app.py
```

Your application should start according to its implementation and scheduling configuration.

## 🔄 How It Works

1. The user enters the recipient's WhatsApp number.
2. The user writes a message.
3. The user selects the scheduled date and time.
4. The scheduler stores or tracks the scheduled task.
5. At the specified time, the application requests Twilio to send the WhatsApp message.
6. The application records or displays the message status, depending on the implementation.

## 🔒 Security and Best Practices

- Keep credentials in environment variables.
- Add `.env` and virtual environment folders to `.gitignore`.
- Use valid international phone number formats.
- Obtain appropriate recipient consent before sending messages.
- Follow Twilio's WhatsApp messaging policies and applicable opt-in requirements.
- Use persistent storage if scheduled messages must survive application restarts.
- Keep the scheduler running or deploy it on a suitable server for continuous operation.

## ⚠️ Important Notes

- Twilio WhatsApp Sandbox is intended for testing and requires recipients to join the sandbox.
- Production messaging may require an approved WhatsApp sender and approved message templates, depending on the message type and applicable WhatsApp rules.
- A scheduled message is not guaranteed to be delivered at an exact second; delivery depends on the application, Twilio, and WhatsApp.
- The scheduler must be running at the scheduled time unless you use a persistent or externally managed scheduling service.

## 🔮 Future Improvements

- Add a web interface for scheduling messages.
- Store scheduled messages in a database.
- Support recurring messages.
- Add message status tracking and delivery reports.
- Implement authentication and user-specific schedules.
- Deploy the application to a cloud server.

## 👨‍💻 Author

**Vishal Kumawat**

GitHub: [vishalkumawat2005](https://github.com/vishalkumawat2005)

## 📄 License

This project is available for educational and personal use. Add a suitable open-source license if you want others to reuse, modify, and distribute the code.
