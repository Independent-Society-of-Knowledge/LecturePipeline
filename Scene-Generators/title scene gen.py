from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal
from manim import *


def extract_headings(pdf_path, min_font_size=10):
    headings = []
    finallist = []
    finalllist2= []
    with open(pdf_path, 'rb') as file:
        for page_layout in extract_pages(file):
            for element in page_layout:
                if isinstance(element, LTTextBoxHorizontal):
                    for text_line in element:
                        if isinstance(text_line, LTTextLineHorizontal):
                            max_font_size = 0
                            a = False
                            for character in text_line:
                                
                                if hasattr(character, 'size'):
                                    if max_font_size == character.size :
                                        a = True
                                    max_font_size = max(max_font_size, character.size)
                            line_text = text_line.get_text()
                            
                            if max_font_size >= min_font_size and a :

                                headings.append(line_text)
    for i in headings :
        if 'cid:' not in i:
            finallist.append(i)
    for i in finallist:
        try :
            i = int(i)
        except:
            finalllist2.append(i)

    return finalllist2

pdf_path = 'name.pdf' 

class TextToVideo(Scene):
    def construct(self):
        headings = extract_headings(pdf_path)
        for heading in headings:
            text = Text(heading,font_size = 30)
            self.play(Write(text))
            self.wait(2)
            self.play(FadeOut(text))