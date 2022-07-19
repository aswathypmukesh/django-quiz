from django.db import models
 
# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question

class Question(models.Model):
    score = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    correct = models.IntegerField(null=True, blank=True)
    wrong = models.IntegerField(null=True, blank=True)
    percen = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)


# models.py
# class Quiz(models.Model):
#     title = models.CharField(max_length=20)
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     set = models.ForeignKey(Quiz,on_delete=models.CASCADE)
#     question_txt = models.CharField(max_length=100)

#     def __str__(self):
#         return self.question_txt

# class Choice(models.Model):
#     question = models.ForeignKey(Question,on_delete=models.CASCADE)
#     choice_txt = models.CharField(max_length=20)
#     boolean = models.BooleanField(default=False)

#     def __str__(self):
#         return self.choice_txt

# view.py
# def detail(request,pk):
#     quiz = get_object_or_404(Quiz,pk=pk)
#     questions = quiz.question_set.all()
#     return render(request,'App/appdetail.html',{'questions':questions,'quiz':quiz})