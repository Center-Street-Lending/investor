import docx
import html
import re

doc = docx.Document('/Users/gregmontoya/.gemini/antigravity/brain/9d721591-535b-4651-ba85-9e6a1aa3b496/.user_uploaded/media_1791303197568.docx')

table = doc.tables[0]
table_data = []
for i, row in enumerate(table.rows):
    cells = [cell.text.strip() for cell in row.cells]
    table_data.append(cells)

print("Table rows:", len(table_data))
