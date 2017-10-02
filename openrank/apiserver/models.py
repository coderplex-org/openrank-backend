from django.db import models

# Create your models here.
#All the Comments and doc-strings may contain Opinionated Views.
#These are not the final docs. Constructive Negation is welcome!  ex  you may find the comments too-verbose

class Contest(models.Model):
    name=models.CharField()
    description=models.TextField()
    url = models.URLField()
    ispublic = models.BooleanField()
    duration =  #which Buildin FIeld to use? TimeField?
    starttime = models.TimeField()



class Users(models.Model):
	'''Currently these fiels are planned
	1)name -eh just the name.     should there be a max length? for name? 
	2)email - email of the contestant.  BuiltIn  EmailField from django is being used.
	3)password-
	4)phone_number- an IntegerField.    how will we validate this? is there any Buildin  (like how it is for Email)

'''
	name  = models.CharField(max_length=60)
	email = models.EmailFiel(dmax_length=60)
	passord = models.CharField(max_length=)
	phone_number = models.IntegerField()



class Question(models.Model):

	description = models.TextField()
	totalmarks = models.IntegerField()

	solution = 



class Submission(models.Model):
	''' Currently these fields are planned
	Note  three stars before fieldName if it is a RelationshipField
	1)***SubmitedBy - will help identify which user submitted this sumission
	             - It will relate to the Users model in a ManyToOne Relation (definately Not manyToMany because One  same submission can't be made by two distinct users )
	
	2)***WhichContest - will help identify as part of which Contest this submission was made.
	                  - It  will Relate to the Contest model

	
	3)scorevaluated -just an integer for now (atleast)  given by the scoringEngine for this sumission'

	4)program   - a .py file  which is the code submited (Just For Now)
	'''
	submitedby = 
	whichcontest=
	scorevaluated = models.IntegerField()
	program  =  # it has to be  a  FileField()?

class Solution(models.Model):
# I don't see the point in haveng a seperate solution table

#I think Submission is the generic thing 
# and only  something done by the Problem Setter or A Tester should be officially Recognized as a solution 
#Rest all are simply Submissions (generic!)