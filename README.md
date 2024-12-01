# Solar_AQI_Analysis

# Solar Energy Generation Predictor 🌞🌍

This project leverages air quality data to predict solar energy generation and visualizes the impact of pollutants on solar power output. By integrating the Ambee API for real-time air quality data and Chart.js for interactive visualization, this tool provides users with insights into how pollutants affect solar irradiance across various locations.

---

## 🌟 Features
- Fetches real-time air quality data, including **CO**, **NO2**, **Ozone**, **PM10**, **PM2.5**, and **SO2** concentrations.
- Estimates solar energy generation based on pollutant levels and their effect on sunlight penetration.
- Interactive **visualizations**:
  - **Pie chart**: Shows pollutant contributions to solar energy reduction.
  - **Line chart**: Displays the relationship between AQI levels and solar energy generation.
- User-friendly web interface for searching and analyzing city-specific data.
- Dynamic integration with the **Ambee API** for live data updates.

---

## 🛠️ Tools and Technologies
- **Python**: Backend development with Flask for creating a lightweight web application.
- **Flask Framework**: Handles routing, API integration, and template rendering.
- **Ambee API**: Fetches real-time air quality data.
- **Chart.js**: Creates responsive and interactive charts for visualization.
- **HTML/CSS**: Frontend design for a user-friendly interface.
- **Jinja2**: Dynamic rendering of data in the HTML templates.

---

## 🔍 How It Works
1. **Data Collection**:
   - Air quality data is fetched from the **Ambee API** based on the user's city query.
   - Pollutant concentrations and AQI are retrieved and processed.

2. **Data Processing**:
   - Solar energy generation is estimated based on pollutant levels using a predefined mathematical model.

3. **Visualization**:
   - Interactive charts (pie and line) are rendered using **Chart.js**.
   - Pollutant contributions and solar energy generation trends are displayed for better insights.

4. **User Interaction**:
   - Enter the city name in the search bar to get air quality and solar generation predictions.
   - Data is displayed in tabular format along with visualizations.

---

## 🚀 Installation Guide
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/solar-energy-generation-predictor.git
   cd solar-energy-generation-predictor
