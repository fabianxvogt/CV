import base64
import json
from xhtml2pdf import pisa
import asyncio
from pyppeteer import launch

async def generate_pdf_from_html(html_content, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    await page.addStyleTag(path='styles.css')
    await page.setContent(html_content)
    
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    
    await browser.close()

async def generate_pdf_from_url(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    await browser.close()

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        
    return not pisa_status.err

# # Base HTML content
# html_content = open('CV.html').read()

# # Render personal data 
# personal_data = json.loads(open('personal_data.json').read())
# personal_data_html_str = ""
# for k, v in personal_data.items():
#     personal_data_html_str += f'<tr><td style="width: 30%;"><b>{k}</b></td><td>{v}</td></tr>'
# #personal_data_html_str += '</table>'

# html_content = html_content.replace("[PERSONAL_DATA]", personal_data_html_str)
# print(html_content)

# Generate PDF
pdf_path = "example.pdf"
url = 'http://127.0.0.1:5000/'
asyncio.get_event_loop().run_until_complete(generate_pdf_from_url(url, 'from_html.pdf'))

# if convert_html_to_pdf(html_content, pdf_path):
#     print(f"PDF generated and saved at {pdf_path}")
# else:
#     print("PDF generation failed")
