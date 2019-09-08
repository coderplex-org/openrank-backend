---
title: "Openrank - Discussion Gist"
output: pdf_document
---

# OpenRank - Gist of discussions

This document is use to record the gist of discussion that the devlopers/contributors have periodically.

### August 2019

- **Week 2**:

	- We decided the stack to work on as PENN (Postgres-Express.js-Next.js-Node.js) for below mentioned reasons.

		- Postgres DB - This was made a choice because the data that we need to store in DB, like code submissions, user details, results, etc., were mostly structured and we can have a relational schema built for the kind of data we wanted to store in db. Hence we didn't go for a NoSQL db and wanted to reply on relational databases. The choice of postgres was made because it had good community support and supports wide range of variety of data types. Also it was already in use for popular web applications.
		
		- Express.js - From the developer's suggestion we had two choices either to go for Django(Python) or Express(JavaScript). One of the reasons we had to chose express was it's non blocking execution nature(event loop) which made it popular for usage in backend for most of the web applications today. Other reason is that we have good community support for Express and most of the developers also voted for Express tp work with.
		
		- Next.js - One major reason was we wanted the frontend to be written in Vue or React. As the votes for React were more we though of having React. Then Next.js popped up into the list of suggestions. According to some sources on internet we felt that Next.js is server-side rendering and it is light. As it was based on React most of the devs were okay with it.
		
		- Node.js - I think no explanation needed for this 😜

	- Online judge/Execution and evaluation of user submitted code. Following are the alternatives we thought of:
		
		- By looking at most of the open-source projects that tried to implement the online judge or code execution environment we decided to have the execution environment in a container.
		
		- We thought of having docker containers to run the code submitted by the user and compare the stdout with the testcase outputs provided.
		
		- Next question after this decision was, how do we carry out the execution, we had following two questions?
			
			- Do we have to copy the file with code to docker container and pass the commands required to docker itself so that the compilation & execution is performed and output is captured?
			
			- Do we have to run a node server which accepts the code and meta data regarding the programming language and use the provided data to spawn a child process to run the code?
	

* **Week 3**:

	After discussing about the decisions made in the last week there were few suggestions for the changes. The suggestions are:

	- Using dockers for execution can have two types:

		- Dedicate a container for a single language and pick jobs from queue whose language meta is same as which the docker is configured for.

		- Make a container that can run code of all the languages supported by the platform and pick the job from queue. Based on the meta data provided along with the job run the code accordingly.

	- Use AWS Lambda instead of containers. This will be helpful for easy scaling and costs less server time. Lambdas can live upto 90s which is more than enough for our use-case. To scale with containers we have to deploy container images on new servers and should take care of load balancing. Lamdas has no such overhead setup, we have the lambda function written once and have it instantiated based on our requirements.
	
	- As everyone was okay with React, it would be good to have React itself than Next.js because it can have the load distributed to client for rendering. If all the execution, API server and rendering are server based then it's a huge burden on servers. We can cut it off by having client side rendering.

	- Use Microsoft's open-source code editor Monaco, for rich code editing experience.

	- To have a CDN to deliver test cases for a given question in form of files (not required in the MVP version).