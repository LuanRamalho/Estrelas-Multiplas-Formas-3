from turtle import *
speed(0)
def  formas(lado, num_lados, angulo):
    #Desenha sequências de segmentos eventualmente produzindo formas fechadas.
    color('black', 'blue')
    begin_fill()
    for i in range(num_lados):
        forward(lado)
        left(angulo)
    end_fill()
formas(200,10,108)
done()
