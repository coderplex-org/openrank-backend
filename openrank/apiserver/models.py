from django.db import models

# Create your models here.
#All the Comments and doc-strings may contain Opinionated Views.
#These are not the final docs. Constructive Negation is welcome!  ex  you may find the comments too-verbose

class Contest(models.Model):
    name=models.CharField()
    description=models.TextField()
    url = models.URLField()
    is_public = models.BooleanField()
    starttime = models.TimeField()
    user_id = models.ForeignKey(User)
    position = models.ForeignKey(Position)
    cutoff_duration = models.IntegerField()
    login_start_time = models.TimeField()
    password = models.charField(max_length=45)


class Position(models.models):
	job_title = models.charField()





class User(models.Model):
	'''Currently these fiels are planned
	1)name -eh just the name.     should there be a max length? for name? 
	2)email - email of the contestant.  BuiltIn  EmailField from django is being used.
	3)password-
	4)phone_number- an IntegerField.    how will we validate this? is there any Buildin  (like how it is for Email)

'''

    role = models.OneToOneField()  # A Role can oprionally be assigned to a User. But a User MUST be assigned to SOME ROLE
	name  = models.CharField(max_length=60)
	email = models.EmailFiel(dmax_length=60)
	pasword = models.CharField(max_length=50)
	phone_number = models.charField(max_length=10)


class Enrollment(models.Model)
    user_id =    models.ForeignKey(User)
    contest_id = models.ForeignKey(Contest,on_delete=models.CASCADE)
    marksobtained = models.IntegerField()
    userDetails = models.charField()

class Role(models.Model):
	role = model.charField()


class Question(models.Model):

	description = models.TextField()
	total_marks = models.IntegerField()
	tags = models.manyToMany(Tag)

	 


class ContestQuestion(models.Model):
	question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
	contest_id = models.ForeignKey(Contest,on_delete=models.CASCADE)
	total_marks  = models.IntegerField()
	time_limit   = models.IntegerField()
	memory_limit = models.IntegerField()  
	variable_constraints = models.CharField(max_length=45)


class Language(models.Model):
	language = models.charField()


class QuestionLanguage(models.Model):
	question_id = models.ForeignKey(Question,on_delete=models.CASCADE)
	language_id = models.ForeignKey(Language,on_delete=models.CASCADE)
	function_signature =  models.TextField()
	function_parameters = models.charField()
	starter_code =        models.charField()


class Tag(models.Model):
	tag_description =   models.charField()  #A charField
	questions = models.manyToMany(Question)
    

class TestCase(models.Model):
	_input = models.charField()
	output = models.charField()
	testcaseBatch_id = models.ForeignKey(TestCaseBatch,on_delete=models.CASCADE)
	question_id = models.ForeignKey(Question,on_delete = models.CASCADE)
	is_hidden = models.BooleanField()

class TestCaseBatch(models.Model):
	marks = models.IntegerField()
	title = models.charField()




class Submission(models.Model):
	''' Currently these fields are planned
	Note  three stars before fieldName if it is a RelationshipField
	1)***enrolment_id - will help identify which user submitted this sumission
	             - It will relate to the Users model in a ManyToOne Relation (definately Not manyToMany because One  same submission can't be made by two distinct users )
	
	2)***contest_id - will help identify as part of which Contest this submission was made.
	                  - It  will Relate to the Contest model

	
	3)scorevaluated -just an integer for now (atleast)  given by the scoringEngine for this sumission'

	4)program   - a .py file  which is the code submited (Just For Now)
	'''
	#submitedby = 
	#whichcontest= #Dropped instead this will be found from relation to Enrollment table
	               #So there is no direct relation between Contest and Submission??  @Bhanu @Kapil
	

	scorevaluated = models.IntegerField()
	program  =  models.TextField()
	question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
	enrollment_id = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
    language_id = models.ForeighKey(Language,on_delete=models.CASCADE)

