import streamlit as st
import numpy as np
import plotly.graph_objects as go

# تنظیمات صفحه (باید اولین دستور باشد)
st.set_page_config(page_title="کاوش تابع درجه دوم", layout="wide")

# --- بخش طراحی ظاهر (CSS) ---
st.markdown("""
<style>
    /* تغییر فونت به یک فونت زیبا */
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Vazirmatn', sans-serif;
    }
    /* پس زمینه سورمه ای */
    .stApp {
        background-color: #0f172a;
    }
    /* رنگ نوشته ها روشن */
    h1, h2, h3, p, label, .stMarkdown {
        color: #e2e8f0 !important; 
    }
    /* عنوان طلایی */
    h1 {
        color: #fbbf24 !important;
        text-align: center;
        font-weight: 700;
        margin-bottom: 30px;
    }
    /* رنگ طلایی برای اسلایدرها */
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background-color: #fbbf24 !important;
        border-color: #fbbf24 !important;
    }
    .stSlider [data-baseweb="slider"] > div > div {
        background: #fbbf24 !important;
    }
    /* رنگ اعداد بالای اسلایدر */
    .st-ef {
        color: #fbbf24 !important; 
    }
</style>
""", unsafe_allow_html=True)

# --- عنوان اصلی ---
st.title("📈 کاوش تعاملی تابع درجه دوم")

# --- تقسیم صفحه به دو ستون ---
# ستون اول ۱ واحد (برای اسلایدرها) و ستون دوم ۲ واحد (برای نمودار) عرض دارد
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### ⚙️ تنظیم ضرایب")
    a = st.slider("ضریب a (انحنا)", -5.0, 5.0, 1.0, 0.1)
    b = st.slider("ضریب b (شیب)", -10.0, 10.0, 0.0, 0.5)
    c = st.slider("ضریب c (عرض از مبدا)", -10.0, 10.0, 0.0, 0.5)
    
    # محاسبه دلتا
    delta = b**2 - 4*a*c
    st.markdown(f"**دلتا (Δ) =** <span style='color:#fbbf24; font-size:20px;'>{delta:.2f}</span>", unsafe_allow_html=True)

with col2:
    # محاسبه مقادیر x و y
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    # ساخت نمودار با Plotly
    fig = go.Figure()
    
    # اضافه کردن خط نمودار (رنگ طلایی)
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(width=3, color='#fbbf24')))
    
    # تنظیمات ظاهری نمودار
    fig.update_layout(
        title=dict(
            text=f"y = {a}x² + {b}x + {c}",
            font=dict(color='#e2e8f0', size=20)
        ),
        paper_bgcolor='rgba(0,0,0,0)', # پس زمینه شفاف تا رنگ سورمه ای دیده شود
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            title="محور x",
            gridcolor='rgba(255, 255, 255, 0.1)', # خطوط راهنمای محو
            zerolinecolor='#e2e8f0',              # محورهای اصلی روشن
            tickfont=dict(color='#94a3b8')
        ),
        yaxis=dict(
            title="محور y",
            gridcolor='rgba(255, 255, 255, 0.1)',
            zerolinecolor='#e2e8f0',
            tickfont=dict(color='#94a3b8'),
            range=[-30, 30]
        ),
        margin=dict(l=20, r=20, t=50, b=20)
    )

    # نمایش نمودار در ستون دوم
    st.plotly_chart(fig, use_container_width=True)
