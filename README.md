# university-chatbot
A chatbot system designed to assist AIU students by automatically answering common questions related to academics, admissions, campus services, and more using Natural Language Processing (NLP) techniques.

# AIU Chatbot

A university chatbot built for an NLP course project using Flask, spaCy, and a front-end with HTML, CSS, and JavaScript.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd university-chatbot

   ## Project Structure
university-chatbot/
├── .venv/ # Virtual environment (created manually)
├── backend/
│ ├── data/
│ │ └── mydata.txt # Provided dataset
│ ├── database/
│ │ └── data.csv # Processed dataset
│ ├── model/ # Empty (no model training with spaCy)
│ ├── nlp/
│ │ └── nlp.py # NLP logic with spaCy
│ └── app.py # Flask server
├── frontend/
│ ├── index.html # Chat UI
│ ├── script.js # Front-end logic
│ └── styles.css # Styling
├── .gitignore # Git ignore file
├── README.md # Project documentation
└── requirements.txt # Python dependencies