from googletrans import Translator

translator = Translator()

input_file = open("input.txt", "r")
paragraphs = input_file.readlines()

output_file = open("output.txt", "w")


for paragraph in paragraphs:
	result = translator.translate(str(paragraph), dest='es')
	translated_text = result.text
	output_file.write(translated_text)
	output_file.write('\n')
	print(translated_text)

output_file.close()
