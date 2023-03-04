import openai

openai.api_key = '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'

Location = 'St Johns County Florida'

Resources = (
    "\n Group By County and Resources For " + Location + ": " +
    "\n Indent Resources " +
    "\n- Select 30 ansers for each Resources:"
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
    "\nInclude descriptions, contact information, addresses and any restrictions"

)


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": Resources}]
)


content = completion["choices"][0]["message"]["content"]
print(content)
