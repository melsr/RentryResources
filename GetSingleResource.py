import openai
import pandas as pd
import os

os.chdir('E:\OneDrive - Greenfield Analytics\Development\PythonAnalytics\ChatGPT\County Resources')

openai.api_key = os.environ.get('OPENAI_API_KEY')

Location = 'Hendry County Florida'


Header = "Reentry Resources for " + Location

Resources = (
    "\n Group By County For " + Location + ": " +
    "/n no numbering" +
    "\n- Select 30 answers for each Resource:"
    "\n- Homeless resources" +
    "\n- Housing and Shelters" +
    "\n- Laundry and showers" +
    "\n- Transportation" +
    "\n- Education and Employment" +
    "\n- Food and Nutrition" +
    "\n- Health and Mental Health" +
    "\n- Additional Services" +
    "\n- Food Stamps" +
    "\n- Financial" +
    "\n- Legal Aid" +
    "\n- Courts" +
    "\n- Sheriff or Police Department" +
    "\n- Include descriptions, contact information, addresses and any restrictions" +
    "\n- Use indentation not numbers"
    )

try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": Resources}],
        temperature=0.5,
        max_tokens=3072,
        n=1,
        stop=None,
        frequency_penalty=0.5,
        presence_penalty=0.5

    )
    Content = completion.choices[0]  # .text.strip()
except Exception as e:
    print(
        f"Error occurred while generating content for {Location}: {str(e)}")

Content = completion["choices"][0]["message"]["content"]

OutputFile = Location + '.txt'

file = open(OutputFile, 'w')
file.write(Header)
file.close()

with open(OutputFile, 'a') as modified:
    modified.write(Content)
