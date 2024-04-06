import streamlit as st

st.set_page_config(page_title="About Us", page_icon=":tada:", layout="wide")

# Header section
with st.container():
    st.title("ABOUT US")
    st.markdown("<hr>",unsafe_allow_html=True)
    st.title("AI-Powered Misinformation Combat Platform: TruthMesh")
    st.write("We are passionate about finding an AI-Powered solution")

# Introduction section
with st.container():
    st.header("What We Do")
    st.write("##")
    st.write(
            """
            Our platform prioritizes enhanced media literacy, offering users tools to discern between reliable and unreliable 
            information. Community engagement is central, fostering collective responsibility in combating misinformation. We 
            emphasize swift correction through user contributions and advanced machine learning, maintaining a dynamic space for 
            continuous improvement against evolving misinformation tactics.
            """
        )

# Main Projects section
with st.container():
    st.write("---")
    st.header("Our Works")
    st.header("Team Name: ZenMinds")
    st.write("##")
    st.write(
        """
        *Team Members:* Yashwenth, Roshan, Abhinanth, Abijith, Yuvashree  

        *Abstract:* AI-Powered Misinformation Combat Platform  

        *Executive Summary:*  
        In response to the escalating threat of online misinformation, our team presents an innovative solution — an AI-driven 
        platform leveraging Natural Language Processing (NLP) techniques. This platform aims to identify, verify, and counteract 
        misinformation across diverse online platforms and social media channels.

        *Problem Statement:*  
        "Combatting Online Misinformation: AI and NLP Solutions for a Digital Age. Create a sustainable solution to combat 
        misinformation and disinformation online. In today's digital age, the spread of false information poses a significant threat 
        to societal discourse, public trust, and democratic processes." (Source: WEF)

        *Key Features:*  
        1. Multifaceted Misinformation Detection:
            - Utilizes advanced NLP models to analyse textual content for potential misinformation.
            - Incorporates image recognition algorithms to identify misleading visuals and avoid them.
        2. Related News Suggestion Engine:
            - Implements a related news suggestion engine which suggests related news from credible sources.
        3. User-Friendly Interface:
            - Develops an intuitive and accessible user interface for seamless interaction.
            - Provides clear indicators for verified content and potential misinformation.
        4. Crowdsourced Fact-Checking:
            - Engages users in the verification process, allowing them to contribute and vote on content authenticity.
            - Implements gamification elements to encourage active user participation.
            - Enables users to report suspicious content directly from their social media accounts / websites.
        5. Adaptive Learning Algorithms:
            - Utilizes machine learning algorithms to adapt and evolve with emerging misinformation trends.
            - Regularly updates the system based on user feedback and technological advancements.

        *Conclusion:*  
        The TruthMesh platform strives to create a resilient defence against online misinformation, promoting a digitally 
        informed and empowered society. This abstract provides a glimpse into our multifaceted approach, ensuring a holistic 
        solution to one of the most pressing challenges of our digital age.
        """
    )

# CSS Styling
st.markdown("""
<style>
/* CSS Snippet from W3schools: https://www.w3schools.com/howto/howto_css_contact_form.asp */
/* Style inputs with type="text", select elements and textareas */
input[type=message], input[type=email], input[type=text], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
    background-color: white;
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
  background-color: #45a049;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Get in Touch with Us section
with st.container():
    st.write("---")
    st.header("Get in Touch with Us")
    st.write("##")

    contact_form =  """
    <form action="https://formsubmit.co/abijithsv321@gmail.com" method="POST">
                <input type ="hidden" name ="_capcha" value = "false">
             <input type="text" name="name" placeholder = "Your name"  required>
             <input type="email" name="email" placeholder = "Your email" required>
             <textarea name = "message" placeholder = "Your message here" required></textarea>
             <button type="submit">Send 📩</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)