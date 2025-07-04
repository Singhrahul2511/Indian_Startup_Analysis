# 🚀 Indian Startup Funding Analysis

This Streamlit web app analyzes Indian startup funding trends using interactive visualizations. It provides insights from both startup and investor perspectives.

---

## 📊 Features

- ✅ **Overall Analysis:** Total funding, MoM trends, top cities/sectors/rounds
- ✅ **Startup POV:** Funding rounds, investors, timeline
- ✅ **Investor POV:** Recent investments, sectors, YoY graph
- ✅ **Top Startups:** Year-wise highest funded startups
- ✅ **Funding Heatmap:** Visualizes funding activity over time

---


## 📁 Project Structure

```bash
📦 Indian_Startup_Analysis/
├── app.py                     # Streamlit app
├── startup_cleaned_updated.csv  # Cleaned dataset
├── requirements.txt           # Required packages
├── render.yaml                # Render deployment config
├── README.md                  # Project overview
└── demo/                      # Screenshots for README
    ├── overview.png
    ├── overview2.png
    ├── startup_funding.png
    ├── startup_info.png
    └── top_funded_startup.png
```



---

## 🖥️ Demo

🌐 Hosted on: [https://your-render-url.onrender.com](#)  
*(Replace this with your actual URL)*


## 🖼️ Demo Screenshots

### 📊 Dashboard Overview
![Dashboard](demo/overview.png)

### Overview Part 2
![overview](demo/overview2.png)

### 🔥 Startup Funding
![Funding Graph](demo/startup_funding.png)

### 💰 Startup Information
![Information](demo/startup_info.png)

### 💰 Top Funded Startup YOY
![Top Funded Startup](demo/top_funded_startup.png)


---

---

## 🚀 How to Run the Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Singhrahul2511/Indian_Startup_Analysis.git
   cd Indian_Startup_Analysis

   ```
2. **Create a virtual environment**
    ```bash
    python -m venv venv
    venv\\Scripts\\activate   # For Windows
    source venv/bin/activate  # For Linux/Mac

    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

    ```

4. **Run the Streamlit app**
    ```bash
    streamlit run app.py

    ```

5. **Open your browser**
    ```bash
    http://localhost:8501

    ```

6. **🌐 Live Demo(You can also check the live version here:)**
    ```bash
    🔗 https://indian-startup-analysis-57rq.onrender.com/

    ```