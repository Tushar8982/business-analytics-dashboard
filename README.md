# 📊 Business Analytics Dashboard

An interactive, cloud-connected sales analytics dashboard built with Python, Streamlit, Plotly, and Supabase. Upload your sales data, analyze performance, track KPIs, and export insights — all in a beautiful web interface.

---

## 🚀 Features

- 📁 Upload custom CSV sales data  
- 🧹 Automatically clean & preprocess data  
- 📊 Key KPIs: Total Revenue, Orders, AOV, Top Product  
- 📈 Interactive visualizations using Plotly  
- 📤 Upload processed data to Supabase PostgreSQL  
- 📥 Export reports to Excel  
- ☁️ Optional deployment to Streamlit Cloud  

---

## 🖼️ Dashboard Preview

<!-- Replace the image path below with your actual screenshot path -->
<p align="center">
  <img src="[C:\Users\tusha\OneDrive\Pictures\Screenshots\Screenshot 2025-05-28 150430.png](https://drive.google.com/file/d/1rbdiAqdpzz2-H-XT-1wyPmlIK7agRXA6/view?usp=drive_link)" alt="Dashboard Screenshot" width="90%">
</p>

---

## 🧰 Tech Stack

| Tool         | Role                                 |
|--------------|--------------------------------------|
| Python       | Core language                        |
| Streamlit    | Web app framework                    |
| Pandas       | Data manipulation & cleaning         |
| Plotly       | Visualizations                       |
| Supabase     | PostgreSQL cloud database            |
| SQLAlchemy   | Database ORM                         |
| dotenv       | Secure configuration management      |

---

## 🛠️ Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/business-analytics-dashboard.git
cd business-analytics-dashboard
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On macOS/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables in a .env file:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_api_key
SUPABASE_DB_HOST=db.your-project.supabase.co
SUPABASE_DB_PORT='XXXX' eg.5432
SUPABASE_DB_NAME=postgxxx
SUPABASE_DB_USER=postgxxx
SUPABASE_DB_PASSWORD=your_password
```

5. Run the app:

```bash
streamlit run app.py
```

---

## 📂 Folder Structure

```bash
business-analytics-dashboard/
│
├── app.py                 # Main Streamlit app
├── config.py              # Environment config loader
├── .env.example           # Sample env file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── utils/
    ├── preprocessing.py   # Data cleaning functions
    ├── kpi.py             # KPI logic
    └── database.py        # Supabase DB connection
```

---

## ☁️ Deploy to Streamlit Cloud

1. Push your code to GitHub  
2. Visit https://streamlit.io/cloud  
3. Connect your GitHub repo  
4. Add your environment secrets (from .env) in the UI  
5. Deploy & share your live dashboard 🚀  

---

## 📝 License


Copyright (c) 2025 Tushar Khandelwal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell    
copies of the Software, and to permit persons to whom the Software is        
furnished to do so, subject to the following conditions:                     

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.                                 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  
IN THE SOFTWARE.


---

## 👨‍💻 Author

Made with ❤️ by Tushar khandelwal
🔗 [LinkedIn]([https://www.linkedin.com/in/tusharkhandelwal77/]) • [GitHub](https://github.com/Tushar8982)


