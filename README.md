# PubMed Article Summarizer 

This project aims to create a web application for summarizing PubMed articles using Natural Language Processing (NLP) models. The development process encompasses data exploration, model selection, fine-tuning, and web application development.

## Table of Contents

- [Introduction](#introduction)
- [Data Exploration](#data-exploration)
- [Model Selection and Fine-Tuning](#model-selection-and-fine-tuning)
- [Web Application Development](#web-application-development)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Conclusion](#conclusion)

## Introduction

The PubMed Article Summarizer is a tool that leverages advanced NLP techniques to provide concise summaries of scientific articles. This project uses the T5 transformer model for text summarization and offers an interactive web interface for users to upload articles and receive summaries.

## Data Exploration

The dataset used for this project is the PubMed summarization dataset from Hugging Face's `datasets` library. This dataset consists of pairs of articles and their corresponding abstracts. Key steps in data exploration included:

- Loading the dataset using the `datasets` library.
- Examining the structure and content of the dataset to understand its format.
- Performing initial data preprocessing to clean the text data, which involved:
  - Removing multiple spaces
  - Removing references
  - Removing parentheses
  - Removing punctuation
  - Converting the text to lowercase

## Model Selection and Fine-Tuning

For the summarization task, we selected the T5 transformer model, which is well-suited for text generation tasks. The process included:

- Initializing the T5 model and tokenizer.
- Preprocessing the text data to ensure it is in a suitable format for the model.
- Fine-tuning the model parameters to optimize performance for brief and detailed summaries. This involved adjusting parameters such as:
  - Maximum length
  - Minimum length
  - Length penalty
  - Number of beams
  - Early stopping criteria

## Web Application Development

The web application was developed using Streamlit, a Python library that enables the creation of interactive web apps for data science projects. The application features:

- **User Authentication**: Implemented using MongoDB and bcrypt for secure password hashing and verification. 
  - Users can sign up, log in, and manage their summaries.
- **Article Input**: Users can either upload a text file or enter the article text directly into a text area.
- **Summary Style Selection**: Users can choose between a brief or detailed summary style.
- **Summary Generation**: The application generates the summary based on the selected style and displays it to the user.
- **Summary Storage**: Generated summaries are stored in MongoDB for each user, allowing them to view their past summaries.

### MongoDB Integration

The application uses MongoDB Atlas for database management. Key aspects included:

- Setting up a MongoDB Atlas cluster and obtaining the connection string.
- Ensuring the current IP address is whitelisted in MongoDB Atlas for access.
- Using MongoDB collections to store user information and summaries.

### Streamlit Application Flow

The application flow consists of the following main sections:

1. **Login Section**: Users enter their credentials to log in. If they don't have an account, they can navigate to the sign-up section.
2. **Sign-Up Section**: New users can create an account by providing a username and password. The password is securely hashed before storage.
3. **Summarization Section**: Logged-in users can upload an article or enter text, choose the summary style, and generate a summary. The summary is then displayed and saved to their account.
4. **Saved Summaries**: Users can view all their saved summaries, including details like the original article text and the selected summary style.

## Setup and Installation

1. **Clone the Repository**: Clone this repository to your local machine using Git.
   ```sh
   git clone https://github.com/username/repository.git
