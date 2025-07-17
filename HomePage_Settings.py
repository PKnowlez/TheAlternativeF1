import streamlit as st
import pandas as pd
from PIL import Image
import base64
from io import BytesIO
import os

def HomePageSettings():
    racelength = Image.open("./Images/stopwatch.png")
    rules = {
        "icon": [   
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
                pil_image_to_base64(racelength, format="PNG"),
            ],
        "Setting":  [   
                        'Race Length',
                        'Qualifying Length',
                        'Sprint Length',
                        'Sprint Qualifying Length',
                        'Traction Control',
                        'Racing Line',
                        'Gearbox',
                        'Damage',
                        'Safety Car & Flags',
                        'Weather',
                        'Corner Cutting'
                    ],
        "Parameter":[   
                        '50%',
                        'Full',
                        'SPRINT LENGTH',
                        'Short',
                        'Full Allowed',
                        'Corners Only',
                        'Automatic Allowed',
                        'Simulation',
                        'Increased',
                        'Accurate',
                        'Strict'
                    ]
    }
    df = pd.DataFrame(rules)

    st.dataframe(
        df,
        column_config={
            "icon": st.column_config.ImageColumn(
                "",
                width="small",
            )
        },
        hide_index=True,
        use_container_width=False
    )

# Helper function to convert a PIL Image object to a Base64 data URL
def pil_image_to_base64(pil_img, format="PNG"):
    buffered = BytesIO()
    pil_img.save(buffered, format=format)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/{format.lower()};base64,{img_str}"