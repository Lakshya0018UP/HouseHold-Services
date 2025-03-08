# Household Services Application

A multi-user platform built with Flask and SQLite that connects customers with service professionals for home maintenance needs. Customers can book services, and professionals can accept or reject requests.

## Features

- **User Authentication**: Customers, Professionals, and Admins can register and log in.
- **Service Management**: Admin can add, update, and delete services.
- **Request Services**: Customers can request services and receive confirmation.
- **Request Handling**: Professionals can accept/reject service requests and mark them as completed.
- **Admin Dashboard**: Admin can manage users, approve professionals, and monitor requests.
- **Flash Messages**: Instant feedback for user actions.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, Bootstrap, Jinja2
- **Caching & Background Jobs**: Redis & Celery (for scheduled jobs)

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/household-services.git
   cd household-services
   ```

2. **Create a Virtual Environment & Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set Up Database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

4. **Run the Flask App**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000`

## Usage

- **Register/Login** as a customer, professional, or admin.
- **Customers** can book services from the services list.
- **Professionals** can accept/reject service requests.
- **Admins** can manage services and users.

## API Endpoints

| Endpoint                     | Method | Description |
|------------------------------|--------|-------------|
| `/`                          | GET    | Home Page |
| `/register`                  | GET/POST | User Registration |
| `/login`                     | GET/POST | User Login |
| `/services`                  | GET    | List All Services |
| `/request_service/<int:id>`   | GET    | Request a Service |
| `/service_requests`          | GET    | View All Service Requests |
| `/accept_request/<int:id>`    | GET    | Accept a Service Request |
| `/reject_request/<int:id>`    | GET    | Reject a Service Request |
| `/complete_request/<int:id>`  | GET    | Mark a Service Request as Completed |
| `/add_service`               | GET/POST | Admin: Add a New Service |

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is open-source and available under the MIT License.
