# OpenRank Milestones

Here is the roadmap and milestones for the development for next couple of weeks.
Here on NRM stands for Not required in MVP.

#Frontend

- Basic UI, that has the following things
    - Welcome view
    - Login/Signup view
        - Basic login that creates a user record in our DB.
        - Social auth (Login using Fb, Google, Apple ID, LinkedIn, Twitter etc., based on our choice) (NRM)
    - User Dashboard, with provision for loggin out
        - User details
        - History of questions/contests attempted (NRM)
        - Achievements (NRM)
    - View contests or questions view
        - List of contest or questions available
        - Filter questions or contests (NRM)
        - Suggest contests based demographics (NRM)
        - Capture user interests and suggest question (NRM)
    - Question Details view (viewed when a user click on a question from above mentioned view)
        - This include the question text provided.
        - Text editor to write code in the language of choice
        - Submission area, where buttons for testing and submitting code will be provided. Under this we have to display test results.
        - Providing tabs to have a look at previous submissions and results (NRM)
        - Tab to view solution (NRM)

#Backend

- Basic ability to fetch data from db and send it to client as JSON, based on the request (either using ORM or by sending queries directly).
    - Fetch data from DB
    - Serialize it to be able to send in response as JSON
- Make requests to docker (which is hosted as another server) to run the code and get the result back so that it can be forwarded to client.
    - Once the basic request-response from node server to server hosting docker is achieved. Try to send some meta data like language, timeout value, memory limits etc.
- Provide authentication for users.
    - Basic login or signup using User model in DB
    - Saving auth details from Social Auth to DB (NRM)
    - Send email verification (NRM)
- Log every request and response to a log db/file. (NRM)

#Database

- Sticking to Postgresql 10, as it has good support than 11.
    - Deciding on how to handle DB. Either by using one of the popular ORMs available for node (or) directly send queries by having templated strings.
- Make changes to the schema from the ER diagram provided from previous devs.
- Creating tables according to the ER diagram.

#Compilations and Runtime

- Choosing a method for containerisation either by using docker or kubernetes.
    - Are we using python or golang? 
- Once, we have the containers test it regarding the compilation and execution of the code in the languages of choice (probably py and js for now).
    - Provide input from file
    - Write output to a file and compare with expected output file
- Provide a functionality to recieve code and metadata(if required) from backend server to compile and run the code inside docker, then test it on test cases provided.
    - Check the meta data to configure the runtime for Timeout, resources that can be used etc.,
- Once we have the above, check if it works for multiple people (2-5 max for now) submitting the code for testing at the same time.
    - Test on decided queue to check if it's working for 2-5 people.
    - Do we need any queue to schedule the jobs? If yes what should we go for? (NRM)
    - Queueing and scheduling the tasks to a worker. (NRM)
- Once we have functionality ready for upto 5 people, think of how to scale it to a larger number of audience. (NRM)