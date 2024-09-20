# Mutual Fund Dashboard Backend

This is the backend server for the Mutual Fund Dashboard application built using FastAPI. It provides authentication, integration with RapidAPI for fetching mutual fund data, and endpoints to manage mutual fund purchases.

## Features

- FastAPI-based backend with CORS support.
- Authentication with dummy credentials.
- Integration with RapidAPI to fetch mutual fund data.
- API to purchase mutual fund units.
- All endpoints secured with token-based authentication.

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn (for running the FastAPI app)
- `python-dotenv` (for environment variable management)
- Requests (for API requests to RapidAPI)
- JWT for token-based authentication

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/rishabh6398/mutual-fund-dashboard-server.git
cd mutual-fund-dashboard-server
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scriptsctivate`
```

### 3. Install dependencies

If you have a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Otherwise, you can install the necessary packages manually:

```bash
pip install fastapi uvicorn python-dotenv requests jose
```

### 4. Setup Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```
DUMMY_USERNAME=your_dummy_username
DUMMY_PASSWORD=your_dummy_password
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
RAPIDAPI_KEY=your_rapidapi_key
```

- Replace `your_dummy_username` and `your_dummy_password` with the dummy credentials for testing login.
- Replace `your_secret_key` with a secure key for JWT encoding.
- Add your RapidAPI key in the `RAPIDAPI_KEY` variable.

### 5. Running the Server

To run the FastAPI server, use Uvicorn:

```bash
uvicorn main:app --reload
```

By default, the server will run on `http://localhost:8000`.

### 6. API Endpoints

- **POST /login**: Login using dummy credentials. Returns an access token.
- **GET /fund-families**: Fetch a list of available fund families.
- **GET /schemes/{fund_family}**: Fetch schemes for the selected fund family.
- **POST /purchase**: Purchase mutual fund units.

### 7. Testing with Dummy Credentials

You can test the login by sending a POST request to `/login` with the username and password from your `.env` file.

For example:

```bash
curl -X 'POST'   'http://localhost:8000/login'   -H 'Content-Type: application/x-www-form-urlencoded'   -d 'username=your_dummy_username&password=your_dummy_password'
```

### 8. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
