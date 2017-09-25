OpenRank is a free and open source alternative for websites like HackerRank, HackerEarth etc. Using this software, startups can self-host, create contests and evaluate potential candidates for job openings within their company.

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
