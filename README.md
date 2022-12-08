# PAM(Proceso Admisión Maestría) // MDAP(Master's Degree Admission Process)

PAM is a web application in which UFPS master's degree applicants can register and view their admission process online. PAM is based on the Django 4.1.2 framework and the Python 3.10.7 interpreter.

## Screenshots

| Log In | Create an account | Name screenshot here |
| -------|--------------|-----------------|
| <img src="./screenshots/login-applicant.jpg" width="200"> | <img src="/screenshots/login-applicant.jpg" width="200"> | <img src="/screenshots/login-applicant.jpg" width="200"> |

| Password reset | Set new password | Password change |
| ---------------|------------------|-----------------|
| <img src="/screenshots/login-applicant.jpg" width="200"> | <img src="/screenshots/login-applicant.jpg" width="200"> | <img src="/screenshots/login-applicant.jpg" width="200"> |

## Functionality

- Master's applicant
  - Register an account as an applicant
  - Login
    - via email & password
    - via Gmail
  - Resend an activation code
  - View master's degrees
  - Enroll in a master's degree
  - Follow up on a master's degree enrollment 
  - Change profile
    - Modify personal information
  - Change email
  - Change password
  - Reset password
  - Logout
- Master's director
  - Login
    - via email & password
    - via Gmail
  - See the master's degrees he directs
  - Evaluate applicants
  - List applicants by degrees
  - Assign interview date and time
  - Change profile
  - Change email
  - Change password
  - Reset password
  - Logout
- Admin
  - Register master's degrees
  - Register master's director
  - Assign directors to their respective master's degrees
- Views
  - Error messages.
## Installing

### Clone the project

```bash
git clone https://github.com/JulianRivers/PAM.git
cd PAM
```

### Install dependencies & activate virtualenv

```bash
pip install -r .\requirements.txt
```

### Apply migrations

```bash
python source/manage.py makemigrations
python source/manage.py migrate
```

### Collect static files (only on a production server)

```bash
python source/manage.py collectstatic
```

### Running

#### A development server

Just run this command:

```bash
python source/manage.py runserver
```
