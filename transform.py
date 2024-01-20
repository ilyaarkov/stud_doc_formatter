import docx
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor
from docx.shared import Cm
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH # shape instead of text
from hyphen import Hyphenator

# read in a document 
document = docx.Document("test_doc/test_file.docx")
# Индекс, чтобы отслеживать количество обработанных страниц
page_count = 0
# Выбор язык для hyphenation
# hyphenator = Hyphenator('en_US')

for section in document.sections:
	# Условие для изменения только первых двух страниц
	#if page_count > 2:

		# Установка полей
		sections = document.sections
		for section in sections:
			section.left_margin = Cm(3)  # Левое поле - 30 мм
			section.right_margin = Cm(1)  # Правое поле - 10 мм
			section.top_margin = Cm(2)  # Верхнее поле - 20 мм
			section.bottom_margin = Cm(2)  # Нижнее поле - 20 мм

		# Проход по всем параграфам в документе
		for paragraph in document.paragraphs:
			# Установка выравнивания текста по ширине
			paragraph.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

			# Проверка наличия изображений в параграфе
			for run in paragraph.runs:
				if run._element.tag.endswith('drawing'):
					# Если это изображение, центрировать его
					run._element.get_or_add_drawing().get_or_add_inline().alignment = WD_ALIGN_PARAGRAPH.CENTER

			# Автоматическая расстановка переносов
			# hyphenated_text = ''
			# for run in paragraph.runs:
			# 	text = run.text
			# 	hyphenated_text += hyphenator.inserted(text) if text else ''

			# # Заменяем текст в параграфе на текст с автоматической расстановкой переносов
			# paragraph.clear()
			# paragraph.add_run(hyphenated_text)

			# Удаление стилей
			paragraph.style = None
			# Установка абзацного отступа
			paragraph.paragraph_format.first_line_indent = Pt(0.63)  # Абзацный отступ - 1,25 см
			# Установка межстрочного интервала
			paragraph.paragraph_format.line_spacing = 1.5 # Полуторный межстрочный интервал

			# Проход по всем объектам-подстрокам в параграфе
			for run in paragraph.runs:
				# Удаление полужирного начертания
				run.font.bold = None
				# Изменение названия шрифта
				run.font.name = "Times New Roman"
				# Изменение размера шрифта
				run.font.size = Pt(14)
				# Цвет текста
				run.font.color.rgb = RGBColor(0, 0, 0)
		# Увеличение счетчика обработанных страниц
	#else:
	#	page_count += 1



# flag to indicate if the previous paragraph contained an image
# prev_paragraph_had_image = False

# iterate over paragraphs in the document
# for paragraph in document.paragraphs:
#     # check if the paragraph contains an image
#     paragraph_has_image = any('graphicData' in run._r.xml for run in paragraph.runs)

#     # if the previous paragraph had an image, change the font size of the current paragraph
#     if prev_paragraph_had_image:
#         for run in paragraph.runs:
#             run.font.size = Pt(8)

#     # update the flag for the next iteration
#     prev_paragraph_had_image = paragraph_has_image

document.save('demo.docx')
document.save('demo.doc')