# Customer Database App

A secure, web-based customer database application with email authentication and a spreadsheet-like interface. Built with FastAPI (Python backend) and React (frontend).

## Features

- 🔐 **Secure Authentication**: Email/password login with JWT tokens
- 📧 **Email Verification**: Automatic email verification for new accounts
- 📊 **Spreadsheet-like Interface**: Excel-like grid for managing customer data
- 🔍 **Advanced Search**: Search across name, email, and company fields
- 📤 **Export Functionality**: Download customer data as CSV
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile
- 🚀 **Fast & Modern**: Built with modern technologies for optimal performance

## Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Robust, open-source database
- **JWT** - Secure authentication tokens
- **Pydantic** - Data validation and settings management

### Frontend
- **React 18** - Modern React with hooks
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client for API calls
- **React Router** - Client-side routing
- **Lucide React** - Beautiful icons

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL (or SQLite for development)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd customer-db-app
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp env.example .env

# Edit .env with your configuration
# DATABASE_URL=postgresql://username:password@localhost/customer_db
# SECRET_KEY=your-super-secret-key
# SMTP settings for email verification
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 4. Start Backend

```bash
cd backend
uvicorn main:app --reload
```

The app will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost/customer_db

# Security
SECRET_KEY=your-super-secret-key-change-in-production

# Email Configuration (for verification emails)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# App Configuration
BASE_URL=http://localhost:8000
```

### Database Setup

1. **PostgreSQL** (Recommended for production):
   ```sql
   CREATE DATABASE customer_db;
   CREATE USER customer_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE customer_db TO customer_user;
   ```

2. **SQLite** (For development):
   - Just change DATABASE_URL to: `sqlite:///./customer.db`

## Usage

### 1. Create Account
- Navigate to `/register`
- Enter your email and password
- Check your email for verification link

### 2. Login
- Navigate to `/login`
- Enter your credentials
- You'll be redirected to the dashboard

### 3. Manage Customers
- **Add Customer**: Click "Add Customer" button
- **Edit Customer**: Click the edit icon on any row
- **Delete Customer**: Click the delete icon on any row
- **Search**: Use the search bar to filter customers
- **Export**: Click "Export CSV" to download data

## API Endpoints

- `POST /register` - User registration
- `POST /token` - User login
- `GET /customers` - List customers (with search/filtering)
- `POST /customers` - Create new customer
- `PUT /customers/{id}` - Update customer
- `DELETE /customers/{id}` - Delete customer
- `GET /verify/{user_id}` - Verify email

## Security Features

- **Password Hashing**: Bcrypt for secure password storage
- **JWT Tokens**: Secure, time-limited authentication
- **Email Verification**: Prevents unauthorized account creation
- **CORS Protection**: Configured for secure cross-origin requests
- **Input Validation**: Pydantic schemas for data validation

## Deployment

### Backend (FastAPI)
```bash
# Production server
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Frontend (React)
```bash
npm run build
# Serve the build folder with nginx or similar
```

### Docker (Optional)
```bash
# Build and run with Docker
docker build -t customer-db-app .
docker run -p 8000:8000 customer-db-app
```

## Development

### Backend Development
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
cd frontend
npm start
```

### Database Migrations
```bash
cd backend
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions:
- Create an issue in the repository
- Check the API documentation at `/docs` when running the backend

## Roadmap

- [ ] Bulk import/export functionality
- [ ] Advanced filtering and sorting
- [ ] Customer activity tracking
- [ ] Email marketing integration
- [ ] Mobile app
- [ ] Multi-tenant support
- [ ] Advanced analytics dashboard

