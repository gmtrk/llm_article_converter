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
    full_prompt = f"{prompt}\n\n{article_text}"

    # Call OpenAI's GPT-4 API to generate HTML using the new ChatCompletion method
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that formats text into HTML."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=1500,
        temperature=0  # Setting temperature to 0 for more deterministic output
    )

    # Extract the HTML from the response
    html_content = response.choices[0].message.content
    return html_content


def main():
    # Read the content of artykul.txt
    article_text = read_article('artykul.txt')

    # Enhanced prompt with detailed guidelines for the OpenAI model
    prompt = """
    Convert the following plain text article into a structured HTML format according to these guidelines:

    - Use appropriate HTML tags to create a well-structured layout (e.g., <h1> for titles, <p> for paragraphs, etc.).
    - Identify sections where graphics could be logically inserted and mark these locations with an <img> tag. Set the `src` attribute to "image_placeholder.jpg" and include an `alt` attribute with a descriptive prompt for generating the image. The alt text should describe the image content based on the surrounding text context.
    - Place captions under each graphic using an appropriate HTML tag (e.g., <figcaption>).
    - The output should only contain HTML that goes inside the `<body>` section. Exclude `<html>`, `<head>`, or `<body>` tags.
    - Do not include any CSS or JavaScript code.

    Text:
    """

    # Pass the content to OpenAI for processing
    html_content = process_article_with_openai(article_text, prompt)

    # Save the generated HTML to artykul.html
    write_output('artykul.html', html_content)
    print("The HTML content has been saved to artykul.html")


if __name__ == "__main__":
    main()