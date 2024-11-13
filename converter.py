import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_article(file_path):
    """Reads content from a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_output(file_path, content):
    """Writes content to an HTML file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_article_with_openai(article_text, prompt):
    """Sends the article content to OpenAI for processing and returns the response."""
    response = ""
    return response


def main():
    # Read the content of artykul.txt
    article_text = read_article('artykul.txt')

    # Define your prompt to guide the OpenAI model
    prompt = ""

    # Pass the content to OpenAI for processing
    html_content = process_article_with_openai(article_text, prompt)

    # Save the generated HTML to artykul.html
    write_output('artykul.html', html_content)
    print("The HTML content has been saved to artykul.html")


if __name__ == "__main__":
    main()