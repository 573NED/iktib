import tensorflow as tf
import tensorflow_text as text
import re 
 
marks = '''!()-[]}{;?@#$%:'"\,./^&amp;*_'''  
#Чтение статьи преподавателя-----------------------------------------
artSens=open("article comparsion/articles/article_sens.txt")
artSensRead = artSens.read()
for x in artSensRead:
    if x in marks:  
        opt_str = artSensRead.replace(x, "")   


#Чтение статьи студента----------------------------------------------
artStud=open("article comparsion/articles/article_student.txt")
artStudRead = artStud.read()
for x in artStudRead:
    if x in marks:  
        opt_str = artStudRead.replace(x, "")  

#-------------------------------------------------------------------
artSensRead = artSensRead.split()
artStudRead = artStudRead.split()


#--------------------------------------------------------------------
hypotheses = tf.ragged.constant([artSensRead])
references = tf.ragged.constant([artStudRead])
#Далее сравниваем два подготовленных тензора, используя метрику Rouge-L. 
#Которая показывает от 0 до 1 на сколько похожи два входных тензора. 
#Где 0 – это совсем разные, а 1 – одинаковые.


result = text.metrics.rouge_l(hypotheses, references, alpha=0.5)
print('F-Measure: %s' % result.f_measure)
print('P-Measure: %s' % result.p_measure)
print('R-Measure: %s' % result.r_measure)
