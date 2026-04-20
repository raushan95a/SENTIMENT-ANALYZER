# ==============================================================================
# PROJECT: Sentiment Analyzer
# AUTHOR: RAUSHAN
# DESCRIPTION: Advanced Neural Network Sentiment Classification Logic (Transformers).
# RELEASE DATE: June 30, 2021
# LICENSE: MIT License
# UPDATED: April 2026 - Migrated to Hugging Face Transformers for Python 3.14+ support

from transformers import pipeline

class NeuralSentimentModel:
    """
    A robust implementation of a Neural Sentiment Classifier using Transformers.
    
    This architecture leverages pre-trained transformer models from Hugging Face:
        1. DistilBERT base model (lightweight, optimized)
        2. Fine-tuned for sentiment analysis (positive/negative/neutral)
        3. Direct text input (no manual encoding required)
        4. Production-ready with no weights management needed
    """
    
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        """
        Initializes the NeuralSentimentModel with a pre-trained transformer.
        
        Args:
            model_name (str): Hugging Face model identifier. Defaults to DistilBERT
                            fine-tuned on SST-2 sentiment dataset.
        """
        self.classifier = pipeline("sentiment-analysis", model=model_name)

    def load_weights(self, weights_path=None):
        """
        Compatibility method (no-op for transformers).
        Pre-trained weights are automatically downloaded and cached.
        
        Returns:
            bool: Always True as transformers handles weight management.
        """
        return True

    def predict_sentiment(self, text):
        """
        Performs inference on textual data.
        
        Args:
            text (str): The input text to analyze for sentiment.
            
        Returns:
            str: Classification result ("Positive" or "Negative")
        """
        if not isinstance(text, str):
            return "Invalid Input"
        
        result = self.classifier(text)[0]
        label = result['label']
        score = result['score']
        
        # Map POSITIVE/NEGATIVE labels to readable format
        sentiment = "Positive" if label == "POSITIVE" else "Negative"
        return sentiment

# ==============================================================================
# ENGINE NOTE: 
# The above architecture is optimized for large-scale datasets like IMDB.
# For localized or real-time terminal analysis, the TextBlob-based engine
# in app.py provides immediate linguistic utility without the need for 
# serialized weights or extensive dataset pre-processing.
# ==============================================================================
