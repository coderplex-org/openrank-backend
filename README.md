OpenRank is a free and open source alternative for websites like HackerRank, HackerEarth etc. Using this software, startups can self-host, create contests and evaluate potential candidates for job openings within their company.

Join the disucssion chatroom for this project on Discord : https://discord.gg/c7pU8Rw

## Running :

You can run the apiserver by using the following command

`openrank/manage.py runserver` 

To run frontend use the following commands in sequence

`cd frontend`

`npm install`

`npm run dev`

open http://localhost:8081/ once the server is started

## Unit tests :

You can run the unit tests by running following command in project folder. Make sure you install pytest module first.

`python3 -m pytest`

## Resources : 
 Vue.js 
 - [Vue.js 2.0 In 60 Minutes](https://www.youtube.com/watch?v=z6hQqgvGI4Y)
 - [Official Vue.js Intro Guide](https://vuejs.org/v2/guide/)
 - [Official Vue.js Style Guide](https://vuejs.org/v2/style-guide/)
 - [More Resources](https://github.com/vuejs/awesome-vue#awesome-vuejs-)

 Django 
 - https://tutorial.djangogirls.org/en/
 - http://www.obeythetestinggoat.com/pages/book.html#toc
 - https://djangobook.com/
 - https://www.youtube.com/watch?v=Ky59C5geOtg
 - https://www.youtube.com/watch?v=yDv5FIAeyoY
 - https://www.youtube.com/playlist?list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy

Awesome beginners-friendly Projects : https://github.com/MunGell/awesome-for-beginners

## Roles 
The application will have different roles for different users. They are as follows :
- User with "creator" role can :         
  1. Create a new contest
  2. Submit questions with inputs and expected output
- User with "Admin" role can :
  1. See the leaderborad (can also decide whether contestants can view or not)
  2. See all code submissions
- User with "Contestant" role can :
  1. Register and participate in contests
  2. Submit their code, and test for custom inputs


## Tech Stack :
1. Django (for backend)
2. Vue.js (for frontend)
3. Docker containers (for testing the submitted code)
4. Celery (distributed computing)


### Deadline: End of December, 2017.

## User Workflow:
- Host on personal server or cloud
- Create a contest:
  1. Provide contest name and other details (Description, Guide, Rules, FAQ, Criteria etc)
  2. Add questions (Challenge name, score, description, sample_input, sample_output, testcases)
  3. Share link generated
- Participate in contest:
  1. Go to link generated for the contest
  2. Register with required details and login
  3. Go through questions and submit code 
  4. Test the code with sample inputs
  5. Test with custom inputs (optional)
  6. Submit for evaluation with all test cases

## Why use this software :
  1. Super easy to deploy to any cloud provider (eg. AWS, AZURE, GCP) or even local servers
  2. It's free. Small companies can use it to conduct coding interviews
  3. Scales really well (automatic evaluataion of code without manual intervention)
