import docx
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import RGBColor
from docx.shared import Cm
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH # shape instead of text
from docx import Document
from pyphen import Pyphen


# read in a document 
document = docx.Document("test_doc/test_file.docx")
# Индекс, чтобы отслеживать количество обработанных страниц
page_count = 0
# Выбор язык для hyphenation
# hyphenator = Pyphen(lang='ru_RU') # Указываем русский язык для hyphenation

# for i, paragraph in enumerate(document.paragraphs):
# 		if i >= 2:
for section in document.sections:
	
	# Условие для изменения только первых двух страниц
	#if page_count > 2:

		# Установка полей
			sections = document.sections
			for section in sections:
				section.left_margin = Cm(3) # Левое поле - 30 мм
				section.right_margin = Cm(1) # Правое поле - 10 мм
				section.top_margin = Cm(2) # Верхнее поле - 20 мм
				section.bottom_margin = Cm(2) # Нижнее поле - 20 мм

			# Проход по всем параграфам в документе
			for paragraph in document.paragraphs:
				# Установка отступов
				paragraph.paragraph_format.left_indent = Pt(0)
				paragraph.paragraph_format.right_indent = Pt(0)
				# Установка выравнивания текста по ширине
				paragraph.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY


			# Удаление стилей
				paragraph.style = None
				paragraph.style = document.styles['Normal']
				# Установка абзацного отступа
				paragraph.paragraph_format.first_line_indent = Pt(35.5) # Абзацный отступ - 1,25 см
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


				# if any('graphicData' in run._r.xml for run in paragraph.runs):
				# 	for run in paragraph.runs:
				# 		if run._element.tag.endswith('drawing') or run._element.tag.endswith('blip'):
				# 			# If the run contains an image
				# 			caption = "Рисунок N.x - "
				# 			if not paragraph.runs[-1].text.endswith("\n"):
				# 					paragraph.insert_run(run._element, "\n" + caption, run.style)
				# 			else:
				# 					paragraph.insert_run(run._element, caption, run.style)
				# 			paragraph.runs[-1].font.size = Pt(30) # Adjust the font size if needed
				# 			paragraph.runs[-1].font.bold = True

				# Проверка наличия изображений в параграфе
				# for run in paragraph.runs:
				# 	if any('graphicData' in run._r.xml for run in paragraph.runs): #run._element.tag.endswith('drawing'):
				# 		# Если это изображение, центрировать его
				# 		run._element.get_or_add_drawing().get_or_add_inline().alignment = WD_ALIGN_PARAGRAPH.CENTER

				# if any('graphicData' in run._r.xml for run in paragraph.runs):
				# 	for run in paragraph.runs:
				# 		paragraph.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

				# if any(run._element.tag.endswith('drawing') for run in paragraph.runs):
					# If the paragraph contains an image, align it to the center
				# 	paragraph.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
				# paragraph_has_image = any('graphicData' in run._r.xml for run in paragraph.runs)
				# if paragraph_has_image:
				# 	for run in paragraph.runs:
				# 		run._element.get_or_add_drawing().get_or_add_inline().alignment = WD_ALIGN_PARAGRAPH.CENTER

				# Полурабочий код работы с изображениями
				if any('graphicData' in run._r.xml for run in paragraph.runs):
					for run in paragraph.runs:
						# Align the paragraph and the next line to the center
						paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
						# Установка абзацного отступа
						paragraph.paragraph_format.first_line_indent = Pt(0) # Абзацный отступ - 1,25 см
						# caption = f"Рисунок {i + 1}.x - "
						# caption = "Рисунок N.x - "
						# run.add_text(caption)
						# Добавляем разрыв страницы
						# run.add_break()



				# # Автоматическая расстановка переносов
				# hyphenated_text = ''
				# for run in paragraph.runs:
				# 	text = run.text
				# 	hyphenated_text += hyphenator.inserted(text) if text else ''

				# # Заменяем текст в параграфе на текст с автоматической расстановкой переносов
				# paragraph.clear()
				# paragraph.add_run(hyphenated_text)

		# Увеличение счетчика обработанных страниц
	#else:
	#	page_count += 1


# keywords = ["Содержание", "Введение", "Заключение", "Список использованных источников"]
# 		# Поиск ключевых слов и вставка разрывов страниц
# for i, paragraph in enumerate(document.paragraphs):
# 			for keyword in keywords:
# 				if keyword.lower() in paragraph.text.lower():
# 					# Добавление разрыва страницы перед параграфом
# 					if i > 0:
# 						document.paragraphs[i - 1].runs[-1].add_break()
# 					document.paragraphs[i].runs[0].add_break()
# 					break

# flag to indicate if the previous paragraph contained an image
# prev_paragraph_had_image = False
# text_after_image = "Рисунок n.x - "
# # iterate over paragraphs in the document
# for paragraph in document.paragraphs:
#     # check if the paragraph contains an image
# 	paragraph_has_image = any('graphicData' in run._r.xml for run in paragraph.runs)

#     # if the previous paragraph had an image, change the font size of the current paragraph
# 	if prev_paragraph_had_image:
# 			for run in paragraph.runs:
# 					run.add_text(text_after_image)
# 					#run.font.size = Pt(8)

# 		# update the flag for the next iteration
# 	prev_paragraph_had_image = paragraph_has_image

document.save('demo.docx')
document.save('demo.doc')














# doc = docx.Document("test_doc/test_file.docx")

#     # Set page margins
# sections = doc.sections
# for section in sections:
#         section.left_margin = Pt(30)
#         section.right_margin = Pt(10)
#         section.top_margin = Pt(20)
#         section.bottom_margin = Pt(20)

#     # Apply text alignment and paragraph formatting
# for paragraph in doc.paragraphs:
#         paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
#         paragraph.paragraph_format.space_after = Pt(12.0)

#         # Set 1.25 cm paragraph indent
#         paragraph.paragraph_format.left_indent = Pt(1.25 * 28.35)

#         # Set 1.5 line spacing
#         paragraph.paragraph_format.line_spacing = 1.5

#         # Remove all styles
#         paragraph.style = doc.styles['Normal']

#         # Set font properties
#         for run in paragraph.runs:
#             run.font.name = 'Times New Roman'
#             run.font.size = Pt(14)
#             run.font.color.rgb = RGBColor(0, 0, 0)  # Black color
#             run.bold = False
#             run.italic = False

#             # Check for specific words and apply additional formatting
#             if any(keyword in run.text for keyword in ['Содержание', 'Введение', 'Заключение', 'Список использованных источников']):
#                 paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
#                 run.add_break()  # Add page break before the keyword

#     # Process images and add "Рисунок N - "
# for paragraph in doc.paragraphs:
# 		for run in paragraph.runs:
# 					if run.inline_shapes:
#                 # Align the image to the center
# 						paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
#                 # Add "Рисунок N - " after the image
# 						run.add_text("Рисунок N - ")
# 						run.add_break()


# # Save the modified document
# doc.save('demo.docx')