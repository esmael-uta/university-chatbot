import pandas as pd
import os
import spacy

# Paths
DATA_PATH = "../data/mydata.txt"
DB_PATH = "../database/data.csv"

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Step 1: Load and preprocess data
def preprocess_data():
    # Read tab-separated data
    df = pd.read_csv(DATA_PATH, sep='\t')
    
    # Save to CSV for easier access
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    df.to_csv(DB_PATH, index=False)
    
    return df

# Step 2: Load data and prepare for similarity matching
def load_data():
    if not os.path.exists(DB_PATH):
        df = preprocess_data()
    else:
        df = pd.read_csv(DB_PATH)
    
    # Precompute spaCy docs for all questions
    df['question_doc'] = df['Question'].apply(lambda x: nlp(x))
    return df

# Step 3: Process user query
def process_query(query, df):
    # Convert query to spaCy doc
    query_doc = nlp(query)
    
    # Compute similarity between query and each question
    similarities = df['question_doc'].apply(lambda x: query_doc.similarity(x))
    
    # Get the index of the most similar question
    best_match_index = similarities.idxmax()
    
    # Get the corresponding answer
    answer = df.iloc[best_match_index]['Answer']
    return answer

# Initialize the data on startup
if __name__ == "__main__":
    df = load_data()
    print("Data loaded and ready for similarity matching.")