from django.db import models

class Role(models.Model):
    role = models.CharField(max_length=100)  

class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length =100)
    password = models.CharField(max_length =100)
    phone_number = models.CharField(max_length =100)

class Position(models.Model):
    job_title = models.CharField(max_length = 100)

class Contest(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    url = models.URLField()
    is_public = models.BooleanField()
    starttime = models.TimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)    
    cutoff_duration = models.IntegerField()
    login_start_time = models.TimeField()
    password = models.CharField(max_length=100)  

class Enrollment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    contest_id = models.ForeignKey(Contest,on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    user_details = models.CharField(max_length=100) #chesinaka already ni!!!

# class Tag(models.Model):
#     tag_description =   models.CharField() 
   
	
class Question(models.Model):                      
    description = models.TextField()            
    total_marks = models.IntegerField()
    # tags = models.ManyToManyField(Tag)

class Tag(models.Model):
    tag_description = models.CharField(max_length=100)     
    questions = models.ManyToManyField(Question)                

class ContestQuestion(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    contest_id = models.ForeignKey(Contest,on_delete=models.CASCADE)
    total_marks  = models.IntegerField()
    time_limit   = models.IntegerField()
    memory_limit = models.IntegerField()  
    variable_constraints = models.CharField(max_length=100)

class Language(models.Model):
    language = models.CharField(max_length = 100)  

class QuestionLanguage(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
    language_id = models.ForeignKey(Language,on_delete=models.CASCADE)
    function_signature =  models.TextField()
    function_parameters = models.CharField(max_length=100)
    starter_code = models.CharField(max_length=100)


class TestCaseBatch(models.Model):
    marks = models.IntegerField()
    title = models.CharField(max_length=100)	

class TestCase(models.Model):
    testcase_input = models.CharField(max_length=100)  
    output = models.CharField(max_length=100)
    testcaseBatch_id = models.ForeignKey(TestCaseBatch,on_delete=models.CASCADE) 
    question_id = models.ForeignKey(Question,on_delete = models.CASCADE)
    is_hidden = models.BooleanField()


class Submission(models.Model):
	score_valuated = models.IntegerField()
	program = models.TextField()
	question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
	enrollment_id = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
	language_id = models.ForeignKey(Language,on_delete=models.CASCADE)

