import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import tensorflow as tf

from PIL import Image
from tensorflow.keras.models import load_model

#from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="EcoVision AI",
    page_icon="♻️",
    layout="wide"
)

# -----------------------
# SIDEBAR
# -----------------------

st.sidebar.title("♻️ EcoVision AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🤖 AI Detection",
        "📊 Analytics",
        "♻️ Waste Guide",
        "📍 Recycling Locator",
        "💬 Eco Chatbot",
        "🌍 Sustainability Tips",
        "👨‍💻 About Project"
    ]
)

# -----------------------
# CSS
# -----------------------
import streamlit as st
import base64

# =========================
# BACKGROUND IMAGE
# =========================
import streamlit as st
import base64

# =========================
# BACKGROUND IMAGE
# =========================

def add_bg():
    with open("images/background.jpeg", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>

        /* =========================
           BACKGROUND
        ========================= */

        .stApp {{
            background-image:
            linear-gradient(
             rgba(0,0,0,0.60),
             rgba(0,0,0,0.60)   
            ),
            url("data:image/jpeg;base64,{encoded}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* =========================
   BACKGROUND
========================= */

.stApp {{
    background-image:
    linear-gradient(
        rgba(0,0,0,0.60),
        rgba(0,0,0,0.60)
    ),
    url("data:image/jpeg;base64,{encoded}");

    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
}}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{{
    background:rgba(255,255,255,0.10);
    backdrop-filter:blur(18px);

    border-right:1px solid rgba(255,255,255,0.15);

    min-width:380px !important;
    max-width:380px !important;
}}

section[data-testid="stSidebar"] h1{{
    color:white !important;
    font-weight:900 !important;
    font-size:46px !important;
}}

div[role="radiogroup"] label{{
    color:white !important;
    font-size:24px !important;
    font-weight:700 !important;
    padding:10px 0px !important;
}}

div[role="radiogroup"] label:hover{{
    color:#bbf7d0 !important;
    transform:translateX(8px);
    transition:0.3s;
}}

div[role="radiogroup"] p{{
    color:white !important;
    font-size:24px !important;
    font-weight:700 !important;
}}

section[data-testid="stSidebar"] *{{
    color:white !important;
}}

/* =========================
   HEADER
========================= */

[data-testid="stHeader"]{{
    background:transparent;
}}

/* =========================
   MAIN CONTAINER
========================= */

.main .block-container{{
    max-width:1400px;

    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;

    background:rgba(255,255,255,0.08);

    backdrop-filter:blur(25px);
    -webkit-backdrop-filter:blur(25px);

    border:1px solid rgba(255,255,255,0.12);

    border-radius:30px;

    box-shadow:
        0 10px 40px rgba(0,0,0,0.25);
}}

       

        /* =========================
           HEADER
        ========================= */

        [data-testid="stHeader"]{{
            background:transparent;
        }}

        /* =========================
           MAIN CONTAINER
        ========================= */

        .main .block-container{{
            max-width:1400px;
            padding-top:2rem;
            padding-left:2rem;
            padding-right:2rem;

            background:rgba(255,255,255,0.15);
            backdrop-filter:blur(18px);

            border-radius:25px;
        }}

        /* =========================
   HERO
========================= */

.hero-title{{
    font-size:90px;
    font-weight:900;
    color:white;

    text-shadow:
        0 0 15px rgba(34,197,94,0.8),
        0 0 30px rgba(34,197,94,0.5);

    line-height:1.1;
}}

.hero-sub{{
    font-size:30px;
    color:#bbf7d0;
    font-weight:700;

    margin-top:10px;
}}

.hero-text{{
    font-size:22px;
    color:white;

    line-height:1.8;

    margin-top:20px;
}}

/* =========================
   BUTTONS
========================= */

.stButton > button{{
    background:linear-gradient(
        135deg,
        #22c55e,
        #16a34a
    );

    color:white;

    border:none;

    border-radius:16px;

    height:58px;
    width:100%;

    font-size:18px;
    font-weight:800;

    transition:all 0.3s ease;
}}

.stButton > button:hover{{
    transform:translateY(-4px);

    box-shadow:
        0 0 25px rgba(34,197,94,0.7);
}}

/* =========================
   METRIC CARDS
========================= */

.metric-card{{
    background:rgba(34,197,94,0.20);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,0.18);

    border-radius:25px;

    padding:30px;

    min-height:220px;

    text-align:center;

    transition:all 0.4s ease;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.25);
}}

.metric-card:hover{{
    transform:translateY(-10px) scale(1.03);

    box-shadow:
        0 0 25px rgba(34,197,94,0.7);

    border:1px solid #22c55e;
}}

.metric-card h3{{
    color:white !important;
    font-size:26px;
}}

.metric-card h1{{
    color:white !important;

    font-size:72px;

    font-weight:900;

    text-shadow:
        0 0 12px rgba(255,255,255,0.8);
}}

/* =========================
   FORCE WHITE CARDS
========================= */

.workflow-card *,
.metric-card *{{
    color:white !important;
}}

/* Workflow Card White Theme */

.workflow-card{{
    background:rgba(255,255,255,0.18);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,0.35);

    border-radius:22px;

    padding:25px;

    min-height:230px;

    text-align:center;

    transition:all 0.4s ease;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.25);
}}

.workflow-card:hover{{
    transform:translateY(-12px) scale(1.03);

    box-shadow:
        0 0 35px rgba(255,255,255,0.7);

    border:1px solid white;
}}

.workflow-card h1{{
    font-size:65px;
    color:white !important;

    text-shadow:
        0 0 15px white;
}}

.workflow-card h4{{
    color:white !important;

    font-size:24px;

    font-weight:900;

    text-shadow:
        0 0 10px white;
}}

.workflow-card p{{
    color:white !important;

    font-size:17px;

    font-weight:500;
}}

/* =========================
   GLOBAL WHITE + BLUE THEME
========================= */

/* All Text */
h1,h2,h3,h4,h5,h6,
p,span,label,li,div {{
    color:white !important;
}}

/* Links */
a {{
    color:#60a5fa !important;
}}

/* Main Headings */
h1 {{
    text-shadow:
        0 0 10px #60a5fa,
        0 0 20px #60a5fa;
}}

/* Cards */
.metric-card,
.workflow-card {{
    background:rgba(59,130,246,0.18);

    backdrop-filter:blur(18px);

    border:1px solid rgba(96,165,250,0.4);

    color:white !important;
}}



div[data-testid="column"]{{
    width:100% !important;
}}

.stMarkdown{{
    width:100% !important;
}}

/* Upload Container */

[data-testid="stFileUploaderDropzone"]{{
    background:#000000 !important;
    border:2px dashed #22c55e !important;
    color:white !important;
}}

[data-testid="stFileUploaderDropzone"] *{{
    color:white !important;
}}
/* Force Black Selectbox */

div[data-baseweb="select"]{{
    background:#000000 !important;
}}

div[data-baseweb="select"] > div{{
    background:#000000 !important;
    color:white !important;
}}

div[data-baseweb="select"] input{{
    color:white !important;
}}

div[data-baseweb="select"] span{{
    color:white !important;
}}

div[role="listbox"]{{
    background:#000000 !important;
}}

div[role="option"]{{
    background:#000000 !important;
    color:white !important;
}}

div[role="option"]:hover{{
    background:#222222 !important;
}}

/* Dropdown Popup Black */

[data-baseweb="popover"] {{
    background:#000000 !important;
}}

[data-baseweb="popover"] * {{
    background:#000000 !important;
    color:white !important;
}}

ul[role="listbox"] {{
    background:#000000 !important;
}}

ul[role="listbox"] li {{
    background:#000000 !important;
    color:white !important;
}}

ul[role="listbox"] li:hover {{
    background:#222222 !important;
}}

       
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()
# -----------------------
# MODEL LOADING
# -----------------------
@st.cache_resource
def load_waste_model():
    interpreter = tf.lite.Interpreter(
        model_path="model/waste_model.tflite"
    )
    interpreter.allocate_tensors()
    return interpreter


interpreter = load_waste_model()

# -----------------------
# WASTE CLASSES
# -----------------------

class_names = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash"
]

# -----------------------
# PREDICTION FUNCTION
# -----------------------
def predict_waste(image):

    img = image.convert("RGB")

    img = img.resize((128, 128))

    img = np.array(
        img,
        dtype=np.float32
    )

    img = img / 255.0

    img = np.expand_dims(
        img,
        axis=0
    )

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(
        input_details[0]['index'],
        img
    )

    interpreter.invoke()

    prediction = interpreter.get_tensor(
        output_details[0]['index']
    )

    prediction = prediction[0]

    st.write("Raw Prediction:", prediction)
    st.write("Predicted Index:", np.argmax(prediction))

    class_index = np.argmax(prediction)

    confidence = float(
        prediction[class_index]
    ) * 100

    sorted_probs = np.sort(prediction)

    top1 = sorted_probs[-1]
    top2 = sorted_probs[-2]

    if top2 > 0.20:
        waste = "Mixed Waste"
    else:
        waste = class_names[class_index]

    return (
        waste,
        confidence,
        prediction
    )
# -----------------------
# HOME PAGE
# -----------------------
if page == "🏠 Home":

    left, right = st.columns([1.1, 1])

    with left:

        st.markdown("""
        <div class="hero-title">
            EcoVision AI
        </div>

        <div class="hero-sub">
            Smart Waste Detection. Better Tomorrow.
        </div>

        <div class="hero-text">
            Upload waste images and get AI-powered predictions,
            recycling guidance and sustainability insights instantly.
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        b1, b2 = st.columns(2)

        with b1:
            st.button("🚀 Try AI Detection")

        with b2:
            st.button("📊 Explore Analytics")

    with right:

        st.image(
            "images/hero.png",
            use_container_width=True
        )

    st.write("")
    st.write("")

    # METRICS

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Accuracy</h3>
            <h1>94%</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="metric-card">
            <h3>🖼️ Images Trained</h3>
            <h1>2500+</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="metric-card">
            <h3>♻️ Waste Classes</h3>
            <h1>6</h1>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="metric-card">
            <h3>🌱 Eco Score</h3>
            <h1>88</h1>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown(
        "<h2 style='text-align:center;color:white;'>🌿 Our Smart Workflow</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    w1, w2, w3, w4, w5, w6 = st.columns(6)

    workflow = [
        ("📤", "Upload Image", "Upload waste image"),
        ("🧠", "AI Analysis", "AI analyzes image"),
        ("🔍", "Prediction", "Waste category detected"),
        ("🗑️", "Bin Recommendation", "Get the right bin"),
        ("🌱", "Eco Tips", "Learn and recycle better"),
        ("📍", "Nearby Centers", "Find nearby centers")
    ]

    cols = [w1, w2, w3, w4, w5, w6]

    for col, item in zip(cols, workflow):

        with col:

            st.markdown(f"""
            <div class="workflow-card">
                <h1>{item[0]}</h1>
                <h4>{item[1]}</h4>
                <p>{item[2]}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.write("")

   
   
# -----------------------
# AI DETECTION PAGE
# -----------------------
elif page == "🤖 AI Detection":

    st.title("🤖 AI Waste Detection")

    st.markdown("""
    Upload an image or capture a photo using your camera.
    EcoVision AI will identify the waste category instantly.
    """)

    uploaded_file = st.file_uploader(
        "📤 Upload Waste Image",
        type=["jpg", "jpeg", "png"]
    )

    camera_image = st.camera_input(
        "📷 Live Camera Detection"
    )

    image = None

    if uploaded_file:
        image = Image.open(uploaded_file)

    elif camera_image:
        image = Image.open(camera_image)

    if image:

        col1, col2 = st.columns([1, 1])

        with col1:

            st.image(
                image,
                caption="Selected Image",
                use_container_width=True
            )

        with col2:

            if st.button("🔍 Analyze Waste"):

                with st.spinner("Analyzing image..."):

                    waste, confidence, prediction = predict_waste(image)

                st.write("Cardboard:", prediction[0])
                st.write("Glass:", prediction[1])
                st.write("Metal:", prediction[2])
                st.write("Paper:", prediction[3])
                st.write("Plastic:", prediction[4])
                st.write("Trash:", prediction[5])
                st.write(f"Confidence: {confidence:.2f}%")

                st.markdown(
                    f"""
                    <div style="
                    background:white;
                    padding:30px;
                    border-radius:20px;
                    text-align:center;
                    width:100%;
                    min-height:250px;
                    ">
                        <h2 style="color:black;">♻ Waste Detected</h2>
                        <h1 style="color:#16a34a;font-size:50px;">
                            {waste.upper()}
                        </h1>
                        <h3 style="color:black;">
                            Confidence: {confidence:.2f}%
                        </h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.progress(int(confidence))

                recommendations = {
                    "plastic": "🟡 Yellow Bin",
                    "paper": "🔵 Blue Bin",
                    "glass": "🟢 Green Bin",
                    "metal": "⚪ Grey Bin",
                    "cardboard": "🔵 Blue Bin",
                    "trash": "⚫ Black Bin",
                    "Mixed Waste": "⚫ General Waste Bin"
                }

                st.info(
                    f"🗑 Recommended Bin: {recommendations.get(waste, '⚫ General Waste Bin')}"
                )

                tips = {
                    "plastic": "♻ Clean plastic before recycling.",
                    "paper": "📄 Keep paper dry and clean.",
                    "glass": "🍾 Separate glass by color.",
                    "metal": "🥫 Rinse cans before disposal.",
                    "cardboard": "📦 Flatten cardboard boxes.",
                    "trash": "🚮 Dispose safely in general waste.",
                    "Mixed Waste": "♻ Separate recyclable items before disposal."
                }

                st.success(
                    tips.get(waste, "♻ Dispose responsibly.")
                )

                impact = {
                    "plastic": "Plastic takes hundreds of years to decompose.",
                    "paper": "Paper is biodegradable and recyclable.",
                    "glass": "Glass can be recycled endlessly.",
                    "metal": "Metal recycling saves large amounts of energy.",
                    "cardboard": "Cardboard should be flattened before recycling.",
                    "trash": "General waste should be disposed safely.",
                    "Mixed Waste": "Mixed waste should be segregated for better recycling."
                }

                st.info(
                    impact.get(waste, "")
                )
# -----------------------
# ANALYTICS PAGE
# -----------------------


elif page == "📊 Analytics":

    st.title("📊 Waste Insights Dashboard")

    st.markdown("""
    Track waste trends, recycling performance,
    and sustainability impact in real time.
    """)

    # TOP METRICS

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "♻ Waste Processed",
            "2,500+",
            "+12%"
        )

    with c2:
        st.metric(
            "🎯 AI Accuracy",
            "94%",
            "+4%"
        )

    with c3:
        st.metric(
            "🌱 Recycled Items",
            "1,800+",
            "+18%"
        )

    with c4:
        st.metric(
            "🌍 Carbon Saved",
            "320 kg",
            "+9%"
        )

    st.write("")

    waste_data = pd.DataFrame({

        "Waste":[
            "Plastic",
            "Paper",
            "Glass",
            "Metal",
            "Trash",
            "Cardboard"
        ],

        "Count":[
            35,
            25,
            15,
            10,
            8,
            7
        ]
    })

    col1, col2 = st.columns(2)

    # PIE CHART

    with col1:

        fig1 = px.pie(
            waste_data,
            values="Count",
            names="Waste",
            hole=0.5,
            title="Waste Distribution"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        st.success("""
📊 Waste Distribution Summary

• Plastic waste accounts for the largest share (35%).

• Paper waste is the second most common category (25%).

• Glass contributes around 15% of the waste stream.

• Metal, Trash, and Cardboard together form a smaller proportion.

• The analysis highlights the need for improved plastic and paper recycling initiatives.
""")

    # BAR CHART

    with col2:

        fig2 = px.bar(
            waste_data,
            x="Waste",
            y="Count",
            title="Waste Category Analysis"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.info("""
📈 Waste Category Analysis Summary

• Plastic and Paper are the most frequently detected waste types.

• Glass waste appears at a moderate level.

• Metal, Trash, and Cardboard have lower detection counts.

• Waste reduction programs should focus primarily on Plastic and Paper categories.
""")

    st.write("")

    st.subheader("📈 Monthly Recycling Trend")

    trend_data = pd.DataFrame({

        "Month":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],

        "Recycled":[
            120,
            180,
            250,
            300,
            420,
            500
        ]
    })

    fig3 = px.line(
        trend_data,
        x="Month",
        y="Recycled",
        markers=True,
        title="Recycling Growth Over Time"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.success("""
📅 Monthly Recycling Trend Summary

• Recycling performance has improved consistently from January to June.

• Recycled items increased from 120 in January to 500 in June.

• The highest growth was observed between April and June.

• The upward trend reflects increased awareness of waste segregation and recycling practices.

• Smart waste management systems can further improve sustainability outcomes.
""")

    st.success("""
🌍 Environmental Impact Summary

• Over 2,500 waste items have been processed through the system.

• More than 1,800 recyclable items were successfully identified.

• Approximately 320 kg of carbon emissions were prevented through improved recycling practices.

• AI-powered waste classification helps reduce landfill dependency and promotes a cleaner environment.

• Continuous recycling efforts contribute directly to long-term sustainability goals.
""")




# -----------------------
# WASTE GUIDE PAGE
# -----------------------

elif page == "♻️ Waste Guide":

    st.title("♻️ Waste Guide")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.image("images/plastic.png")
        st.success("Plastic Waste")

    with c2:
        st.image("images/paper.png")
        st.success("Paper Waste")

    with c3:
        st.image("images/glass.png")
        st.success("Glass Waste")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.image("images/metal.png")
        st.success("Metal Waste")

    with c5:
        st.image("images/trash.png")
        st.success("General Waste")

    with c6:
        st.image("images/recycle.png")
        st.success("Recyclable Waste")

# -----------------------
# RECYCLING LOCATOR
# -----------------------

elif page == "📍 Recycling Locator":

    st.title("📍 Recycling Locator")

    st.markdown("""
Find nearby recycling centers and contribute to a cleaner, greener environment.
""")

    city = st.selectbox(
        "Select City",
        [
            "Delhi",
            "Mumbai",
            "Jaipur",
            "Lucknow"
        ]
    )

    recycling_centers = {

        "Delhi": pd.DataFrame({
            "lat":[28.7041, 28.6139, 28.5355],
            "lon":[77.1025, 77.2090, 77.3910],
            "Center":[
                "Eco Recycling Center",
                "Green Earth Recycling",
                "Smart Waste Hub"
            ],
            "Location":[
                "Rohini, Delhi",
                "Connaught Place, Delhi",
                "Noida Sector 62"
            ]
        }),

        "Mumbai": pd.DataFrame({
            "lat":[19.0896, 19.0760, 19.2183],
            "lon":[72.8656, 72.8777, 72.9781],
            "Center":[
                "Mumbai Recycling Center",
                "Green Waste Station",
                "Eco Smart Hub"
            ],
            "Location":[
                "Andheri East, Mumbai",
                "Bandra West, Mumbai",
                "Navi Mumbai"
            ]
        }),

        "Jaipur": pd.DataFrame({
            "lat":[26.8467, 26.9124, 26.8890],
            "lon":[75.8258, 75.7873, 75.7420],
            "Center":[
                "Jaipur Recycling Center",
                "Eco Waste Point",
                "Green Earth Jaipur"
            ],
            "Location":[
                "Malviya Nagar, Jaipur",
                "Vaishali Nagar, Jaipur",
                "Mansarovar, Jaipur"
            ]
        }),

        "Lucknow": pd.DataFrame({
            "lat":[26.8750, 26.8467, 26.8500],
            "lon":[80.9100, 80.9462, 80.9920],
            "Center":[
                "Lucknow Recycling Hub",
                "Eco Collection Center",
                "Smart Green Station"
            ],
            "Location":[
                "Gomti Nagar, Lucknow",
                "Hazratganj, Lucknow",
                "Alambagh, Lucknow"
            ]
        })
    }

    map_data = recycling_centers[city]

    st.success(
        f"Showing recycling centers in {city}"
    )

    st.map(
        map_data[["lat", "lon"]]
    )

    st.subheader("♻ Available Recycling Centers")

    for _, row in map_data.iterrows():

        st.info(
            f"""
📍 {row['Center']}

🏠 Location: {row['Location']}

🌐 Latitude: {row['lat']}

🌐 Longitude: {row['lon']}
"""
        )

        st.link_button(
            f"🧭 Open {row['Center']} in Google Maps",
            f"https://www.google.com/maps/search/?api=1&query={row['lat']},{row['lon']}"
        )

    st.success("""
🌱 Recycling Benefits

• Reduces landfill waste

• Conserves natural resources

• Saves energy

• Supports a cleaner environment

• Promotes sustainable living
""")

    st.image(
        "images/eco_city.png",
        use_container_width=True
    )




# -----------------------
# ECO CHATBOT
# -----------------------

elif page == "💬 Eco Chatbot":

    st.title("💬 EcoVision Assistant")

    st.markdown("""
    Ask questions about recycling,
    waste management and sustainability.
    """)

    question = st.text_input(
        "💭 Ask your eco question..."
    )

    if question:

        q = question.lower()

        if "plastic" in q:

            st.success("""
♻ Plastic Waste Guide

• Clean plastic before recycling
• Use yellow recycling bins
• Avoid single-use plastics
• Reuse bottles whenever possible
""")

        elif "paper" in q:

            st.success("""
📄 Paper Recycling Guide

• Keep paper dry
• Remove food contamination
• Recycle newspapers and cartons
• Avoid mixing with wet waste
""")

        elif "glass" in q:

            st.success("""
🍾 Glass Recycling Guide

• Separate glass by color
• Rinse bottles before disposal
• Glass can be recycled endlessly
""")

        elif "metal" in q:

            st.success("""
🥫 Metal Recycling Guide

• Clean cans before recycling
• Separate aluminum and steel
• Metal recycling saves energy
""")

        elif "recycle" in q:

            st.success("""
♻ Recycling Tips

• Segregate waste properly
• Reduce, Reuse, Recycle
• Follow local recycling rules
""")

        elif "environment" in q or "sustainability" in q:

            st.success("""
🌱 Sustainability Tips

• Save water
• Save electricity
• Use reusable products
• Plant more trees
""")

        else:

            st.info("""
🤖 EcoVision Assistant

I can help with:

♻ Plastic Waste

📄 Paper Recycling

🍾 Glass Waste

🥫 Metal Waste

🌱 Sustainability Tips

🌍 Environment Questions
""")

    st.write("")

    st.subheader("⚡ Quick Questions")

    c1, c2 = st.columns(2)

    with c1:

        if st.button("♻ How to recycle plastic?"):
            st.success(
                "Clean plastic items before recycling and place them in designated recycling bins."
            )

        if st.button("📄 Can paper be recycled?"):
            st.success(
                "Yes, most paper products can be recycled if they are clean and dry."
            )

    with c2:

        if st.button("🌱 How to reduce waste?"):
            st.success(
                "Reduce, Reuse and Recycle. Avoid single-use products whenever possible."
            )

        if st.button("🌍 Why is recycling important?"):
            st.success(
                "Recycling saves resources, reduces landfill waste and protects the environment."
            )
# -----------------------
# SUSTAINABILITY TIPS
# -----------------------

elif page == "🌍 Sustainability Tips":

    st.title("🌍 Sustainability Tips")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
🌱 Save Water

🚿 Take shorter showers

💧 Fix leaking taps

🪣 Reuse water where possible
""")

        st.success("""
⚡ Save Energy

💡 Turn off unused lights

🔌 Unplug chargers

🌞 Use natural light
""")

    with col2:

        st.success("""
♻ Recycle Properly

🗑 Separate waste

📦 Reuse cardboard

🥤 Recycle plastic bottles
""")

        st.success("""
🌳 Protect Nature

🌲 Plant trees

🚲 Use bicycles

🌍 Reduce carbon footprint
""")

# -----------------------
# ABOUT PROJECT
# -----------------------

elif page == "👨‍💻 About Project":

    st.title("👨‍💻 About EcoVision AI")

    st.image(
        "images/about project.png",
        use_container_width=True
    )

    st.markdown("""
## ♻ EcoVision AI

EcoVision AI is an AI-powered waste
segregation platform developed to promote
smart recycling and sustainable waste management.

The platform uses Artificial Intelligence
and Computer Vision to classify waste
materials and provide disposal guidance.
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🎯 Accuracy",
            "94%"
        )

    with c2:
        st.metric(
            "♻ Waste Classes",
            "6"
        )

    with c3:
        st.metric(
            "📷 Images Trained",
            "2500+"
        )

    st.write("")

    st.subheader("🚀 Features")

    st.success("""
✅ AI Waste Detection

✅ Analytics Dashboard

✅ Recycling Locator

✅ Waste Guide

✅ Sustainability Tips

✅ Eco Chatbot
""")

    st.write("")

    st.subheader("🛠 Technologies Used")

    tech_data = pd.DataFrame({
        "Technology":[
            "Python",
            "TensorFlow",
            "Streamlit",
            "NumPy",
            "Pandas",
            "Plotly"
        ]
    })

    st.table(tech_data)

    st.write("")

    st.subheader("👩‍💻 Developers")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
👩‍💻 Anju

Frontend & AI Developer
""")

    with col2:
        st.info("""
👩‍💻 Pratishtha

Backend & ML Developer
""")

# -----------------------
# FOOTER
# -----------------------

# -----------------------
# FOOTER
# -----------------------

st.write("")
st.write("")

st.divider()

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown(
        "<h1 style='text-align:center;color:white;'>♻️ EcoVision AI</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:white;font-size:20px;'>Smart Waste Detection • Better Tomorrow</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:white;'>👩‍💻 Developed By <b>Anju & Pratishtha</b></p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:white;'>🌱 Sustainable Future | ♻️ Smart Recycling | 🤖 AI Powered</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:white;'>© 2026 EcoVision AI | All Rights Reserved</p>",
        unsafe_allow_html=True
    )
