import openai
import pandas as pd
import os

os.chdir('E:\OneDrive - Greenfield Analytics\Development\PythonAnalytics\ChatGPT\County Resources')

#openai.api_key = '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'

openai.api_key = os.environ.get('OPENAI_API_KEY')

# Location = 'St Johns County Florida'

df = pd.read_csv('../FloridaCounties.csv', header=None)

# Process each County
for index, row in df.iterrows():
    Location = ''
    Location = row[0]
    Header = "Reentry Resources Resources For " + Location

    Resources = (
        "\n Group By County For " + Location + ": " +
        "\n- Select 30 answers for each Resources:"
        "\n- Homeless resources" +
        "\n- Housing and Shelters" +
        "\n- Transportation" +
        "\n- Education and Employment" +
        "\n- Food and Nutrition" +
        "\n- Health and Mental Health" +
        "\n- Food Stamps" +
        "\n- Financial" +
        "\n- Legal Aid" +
        "\n- Courts" +
        "\n- Sheriff or Police Department" +
    	"\n- Veteran Resources" +
        "\n- Include descriptions, contact information, addresses and any restrictions"
    )

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            prompt=Resources,
            temperature=0.7,
            max_tokens=1024,
            n=1,
            stop=None,
            timeout=10,
        )

        Content = completion.choices[0].text.strip()
    except Exception as e:
        print(f"Error occurred while generating content for {Location}: {str(e)}")
        continue

    Content = completion["choices"][0]["message"]["content"]

    OutputFile = Location + '.txt'

    file = open(OutputFile, 'w')
    file.write(Header)
    file.close()

    with open(OutputFile, 'a') as modified:
        modified.write(Content)
