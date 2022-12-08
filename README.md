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

- Master's director
  - Register an account as an applicant
  - Resend an activation code
  - View master's degrees
  - Enroll in a master's degree
  - Follow up on a master's degree enrollment
  - Change profile
  - Change email
  - Change password
- Master's director
- Admin
  - Register master's degrees
- Login
  - via email & password
  - via Gmail
  - Logout
  - Reset password

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
