from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
import os

class pdf:

    def create(self, name, emotion, specific_emotion, activity,  text):


        # os.remove('../Website_Flask/Moody.pdf')
        pdf_name = '../Website_Flask/Moody.pdf'
        c = canvas.Canvas(pdf_name)
        
        c.setFont("Helvetica", 24)
        c.setFillColor(HexColor(0x00bff30))
        c.drawString(120, 710, "Moodys result for "+name)

        c.setFont("Helvetica", 16)
        c.setFillColor(HexColor(0x000))
        c.drawString(60, 600, "Emotion: ")
        c.drawString(130, 600, emotion)
        c.drawString(60, 550, "Specific Emotion: ")
        c.drawString(190, 550, specific_emotion)
        c.drawString(60, 500, "Activity: ")
        c.drawString(120, 500, activity)
        c.drawString(60, 450, "Journal Entry:")
        #c.drawString(60, 450, text)
        
        line = ""
        height= 400
        n = 0
        l = 0
        for i in text:
            line= line+i
            n = n+1
            l = l+1
            if n >= 60 and i == " ":
                c.drawString(60, height, line)
                height = height-20
                line = ""
                n = 0
            elif l >= len(text):
                c.drawString(60, height, line)

        if(emotion == 'happy' or emotion == 'excited'):
            c.drawInlineImage("MoodyImage/MoodyHappy.png", 190, 30, 200, 230)
        elif(emotion == 'sad' or emotion == 'lonely'):
            c.drawInlineImage("MoodyImage/MoodySad.png", 190, 30, 200, 230)
        elif(emotion == 'angry'):
            c.drawInlineImage("MoodyImage/MoodyAngry.png", 190, 30, 200, 230)
        elif(emotion == 'serene' or emotion == 'connected' or emotion == 'surprised'):
            c.drawInlineImage("MoodyImage/MoodyChill.png", 190, 30, 200, 230)

        c.save()


if __name__ == "__main__":
     d = pdf()
     d.create('Antonia', 'Happy', 'Proud', 'learning', 'I am proud of our work and we make such a good process and I am also happy about that its almost the weekend and I can get a bit sleep maybe.')
