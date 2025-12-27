# 🌦️ Historical Weather Data API

A Flask-powered web application and REST API that processes historical weather datasets, stores them in a local SQLite database, and serves temperature data via a web interface and JSON endpoints.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/vinaykumarkv/Weather_Data_API
cd weather-api
```

### 2. Install dependencies

```bash
pip install pandas flask sqlalchemy
```

### 3. Run the application

```bash
python main.py
```

The app will automatically detect if the database needs to be built from your raw `.txt` files on first launch.

## 🛠️ Tech Stack

- **Backend**: Python 3.12+ with Flask
- **Data Processing**: Pandas (for skipping headers and cleaning fixed-width `.txt` files)
- **Database**: SQLite managed via SQLAlchemy & `sqlite3`
- **Frontend**: HTML5 with Bootstrap 5.3 (for the station dashboard)

## 📁 Project Structure

```
├── data/weather_data.db # Folder containing raw .txt weather files, # SQLite database (auto-generated)
├── templates/          # HTML files for Flask (home.html)
├── main.py              # Main Flask application and routes
├── data_functions.py   # Database extraction, cleaning, and query logic     
└── README.md
```

## 📡 API Usage

The API provides historical temperature data for specific stations and dates.

### Get Station Temperature

**Endpoint**: `/api/v1/<station_id>/<date>`

**Format**: `YYYYMMDD` for the date

**Example Request**:
```
http://127.0.0.1:5000/api/v1/10/19881025
```

**Example Response**:
```json
{
  "date": "19881025",
  "station": "10",
  "temperature": "225"
}
```

> **Note**: Temperature values in this dataset are typically in 0.1°C units, e.g., 225 = 22.5°C

## 🧼 Data Cleaning Highlights

This project automates the following "messy" data tasks:

- **Dynamic Skipping**: Skips 17-20 lines of metadata headers depending on the file type (stations or weather data)
- **Column Sanitization**: Automatically strips leading/trailing whitespace from headers (e.g., `" TG"` becomes `"TG"`)
- **Database Synchronization**: Automatically creates and populates the SQLite tables if the `.db` file is missing

## 🌐 Web Interface

The application includes a web dashboard accessible at the root URL (`http://127.0.0.1:5000/`) that displays:

- List of available weather stations
- Quick access to station data
- Station metadata and information

## 📊 Database Schema

The SQLite database contains weather station tables with the following structure:

- **Station ID**: Unique identifier for each weather station
- **Date**: Date of the observation (YYYYMMDD format)
- **Temperature (TG)**: Daily mean temperature in 0.1°C units
- Additional meteorological parameters as available in source files

## 🔧 Configuration

Customize the application by modifying:

- **Data directory**: Update the path to your raw `.txt` files in `data_functions.py`
- **Port**: Change the Flask port in `main.py` (default: 5000)
- **Database name**: Modify the database filename in the configuration

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using Flask and Python**