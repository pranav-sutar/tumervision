import streamlit as st
import tensorflow as tf
import numpy as np
import os

# Tensorflow model prediction
model = tf.keras.models.load_model('./trained_manoj.h5')

def model_prediction(test_image):
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(150, 150))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

# Tumor descriptions
glioma_tumor = """Gliomas are a type of tumor that originates in the glial cells of the brain or spinal cord. They can vary in severity from benign to malignant. Gliomas are categorized based on the type of glial cell they affect, such as astrocytes, oligodendrocytes, or ependymal cells. Symptoms of gliomas may include headaches, seizures, nausea, and changes in cognitive function. Diagnosis often involves imaging tests like MRI or CT scans, followed by biopsy for confirmation. Treatment options depend on the type, location, and grade of the tumor and may include surgery, radiation therapy, chemotherapy, or targeted therapy. Prognosis varies widely and depends on factors like tumor grade, size, and location. Glioblastoma multiforme (GBM) is the most aggressive and common type of malignant glioma, with a particularly poor prognosis. Research into new treatments and therapies for gliomas is ongoing to improve outcomes for patients."""

meningioma_tumor = """Meningiomas are typically slow-growing tumors that originate in the meninges, the protective membranes surrounding the brain and spinal cord. They are often benign, but can occasionally be malignant. Meningiomas are more common in women and tend to occur in older individuals. Symptoms of meningiomas vary depending on their size and location but may include headaches, seizures, changes in vision or hearing, and focal neurological deficits. Diagnosis usually involves imaging tests like MRI or CT scans, followed by biopsy for confirmation. Treatment options for meningiomas include observation, surgery, radiation therapy, and sometimes chemotherapy. The prognosis for meningiomas is generally favorable, especially for benign tumors that can be completely surgically removed. However, the recurrence rate varies depending on factors such as tumor grade and completeness of resection. Ongoing research aims to improve understanding of meningiomas and develop more effective treatments."""

no_tumor = """Congratulations on your clear scan! Your recent brain image analysis did not detect any signs of a tumor. This is great news and a positive step towards ensuring your continued health and well-being.
While this result is reassuring, it’s important to maintain regular health check-ups and consult with your healthcare provider for any concerns or symptoms you may experience. Remember, early detection and prevention are key to managing your health effectively.
If you have any questions or need further assistance, please do not hesitate to reach out to your medical professional. Stay healthy and take care!"""

pituitary_tumor = """Pituitary tumors are growths that develop in the pituitary gland, a pea-sized gland located at the base of the brain. They can be benign (non-cancerous) or malignant (cancerous) and are classified based on their size and hormone-secreting properties. Symptoms of pituitary tumors may include headaches, vision problems, hormonal imbalances leading to issues like abnormal growth, infertility, and changes in menstrual cycles. Diagnosis typically involves imaging tests like MRI or CT scans, along with hormone level assessments. Treatment options for pituitary tumors depend on factors such as tumor size, type, and symptoms, and may include medication, surgery, radiation therapy, or a combination of these approaches. Prognosis for pituitary tumors is generally favorable, especially for benign tumors that are effectively managed. However, some tumors may require ongoing monitoring and treatment. Research continues to improve understanding and treatment outcomes for pituitary tumors."""

arr_sol = [glioma_tumor, meningioma_tumor, no_tumor, pituitary_tumor]

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Detection"])

# Home page
if app_mode == "Home":
    st.header("TumorVision")
    st.write("Just Upload image... & get detect tumor...")
    image_path = "Designer.png"
    st.image(image_path, use_column_width=True)

# About page
elif app_mode == "About":
    st.header("Welcome to TumorVision: Your Brain Tumor Detection Solution")
    st.markdown("""
    TumorVision is an advanced online platform designed to provide swift and accurate detection of brain tumors through the simple upload of MRI images. Our innovative technology harnesses the power of artificial intelligence and machine learning algorithms to analyze MRI scans with exceptional precision, enabling early detection and prompt intervention.
    
    With just a few clicks, users can securely upload their MRI images to our platform. Our sophisticated algorithms then meticulously scrutinize these images, identifying subtle anomalies and patterns indicative of brain tumors. Within moments, users receive comprehensive reports outlining the presence or absence of tumors, along with detailed insights into the findings.
    
    At TumorVision, we prioritize user experience, ensuring a seamless journey from image upload to result delivery. Our intuitive interface is user-friendly, making it accessible to both healthcare professionals and individuals seeking peace of mind about their neurological health.
    
    Early detection is key in the effective management of brain tumors, and TumorVision empowers individuals and healthcare providers alike to take proactive steps towards timely diagnosis and treatment. Our commitment to cutting-edge technology and unwavering accuracy sets us apart as a trusted ally in the fight against brain tumors.
    
    Join us in the mission to revolutionize brain tumor detection and transform outcomes for patients worldwide. Experience the power of TumorVision today.""")
    st.markdown("step 01: Upload Image: ")
    st.image("upload.png")
    st.markdown("step 02: Cross check:  ")
    st.image("crosscheck.jpeg")
    st.markdown("step 03: View Detection: ")
    st.image("detection.jpeg")

# Detection page
else:
   k = 'a'
   st.header("Just Upload image : ")
   test_image = st.file_uploader("Choose image: ")
   if st.button("Show image"):
      st.image(test_image, use_column_width=True)
   # Detection
   if st.button("Predict"):
      st.write("Prediction: ")
      st.write(os.path.isfile("./trained_manoj.h5"))
      result_index = model_prediction(test_image)
      class_name = ['glioma tumor', 'meningioma tumor', 'no tumor', 'pituitary tumor']
      st.write("Predicted result is: ")
      st.success("{}".format(class_name[result_index]))
      for i in range(0,4):
       if(i == result_index):
          st.write(arr_sol[result_index])
      
