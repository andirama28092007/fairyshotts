# Fairyshotts Digital Camera Shop

Welcome to Fairyshotts - Your premier destination for vintage and classic digital cameras. This is a complete business profile website with product listings, categorization, and contact information.

## Features

- Responsive design using Bootstrap 5
- Product categorization by brand (Canon, Sony, Nikon, Casio, BenQ)
- Featured products section
- Image gallery with hover effects
- Mobile-friendly layout
- Easy navigation

## Project Structure

```
Fairyshotts.github.io/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── start_server.bat       # Windows script to start the server
├── static/
│   └── img/              # Product images and logo
├── templates/
│   └── index.html        # Main HTML template
└── README.md            # This file
```

## How to Run

### Option 1: Using the batch file (Windows)
1. Double-click on `start_server.bat`
2. The application will install dependencies and start automatically
3. Open your browser and go to `http://localhost:5000`

### Option 2: Manual setup
1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your browser and go to `http://localhost:5000`

## API Endpoints

The backend provides the following API endpoints:
- `GET /api/products` - Get all products
- `GET /api/products/<id>` - Get a specific product
- `GET /api/products/category/<category>` - Get products by category
- `GET /api/products/featured` - Get featured products
- `GET /api/categories` - Get all unique categories
- `GET /api/products/search?q=<query>` - Search products

## Technologies Used

- Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
- Backend: Python, Flask
- Additional: Font Awesome icons, Google Fonts

## Color Scheme

- Primary: Purple (#a162e8)
- Secondary: Pink (#ff6bcb)
- Accent: Yellow (#ffeb3b)