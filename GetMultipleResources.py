import openai
import requests
import pandas as pd
import os

os.chdir('E:\OneDrive - Greenfield Analytics\Development\PythonAnalytics\ChatGPT\County Resources')

openai.api_key = os.environ.get('OPENAI_API_KEY')

colnames = ['Location']
df = pd.read_csv('../CountiesToProcess.csv', header=None, names=colnames)
df = df.sort_values(['Location'], ascending=True)

# =============================================================================
# Process any missing counties where ChatCPT may have failed
# =============================================================================
all_files = os.listdir()
if len(all_files) > 0:
    df1 = pd.DataFrame({'Location': all_files})
    df1.columns = ['Location']
    df1['Location'] = df1["Location"].str[:-4]

    dif_list = [x for x in list(df['Location'].unique())
                if x not in list(df1['Location'].unique())]
    dfdif = df[(df['Location'].isin(dif_list))]
else:
        dfdif = df

# =============================================================================
# Process each County
# =============================================================================
for index, row in dfdif.iterrows():
    with requests.Session() as session:
        Location = row[0]
        Header = "Reentry Resources for " + Location
        print(Header)

        Resources = (
            "\n Group By County For " + Location + ": " +
            "/n no numbering" +
            "\n- Select 30 answers for each Resource:"
            "\n- Homeless Resources" +
            "\n- Housing and Shelters" +
            "\n- Laundry and Showers" +
            "\n- Transportation" +
            "\n- Education and Training" +
            "\n- Food and Nutrition" +
            "\n- Health and Mental Health" +
            "\n- Veteran Services" +
            "\n- Veteran Organizations" +
            "\n- Food Stamps" +
            "\n- Financial" +
            "\n- Legal Aid" +
            "\n- Employment and Jobs" +
            "\n- Courts" +
            "\n- Sheriff And Police Department" +
            "\n- Additional Services" +
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
            # Content = completion.choices[0]  # .text.strip()
        except Exception as e:
            print(
                f"Error occurred while generating content for {Location}: {str(e)}")
            continue

        Content = completion["choices"][0]["message"]["content"]

        OutputFile = Location + '.txt'

        file = open(OutputFile, 'w')
        file.write(Header)
        file.close()

        with open(OutputFile, 'a') as modified:
            modified.write(Content)

        # close the connection
        requests.Session().close()
